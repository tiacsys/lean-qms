#!/usr/bin/env python3
# Copyright (c) 2026 TiaC Systems
# SPDX-License-Identifier: Apache-2.0
"""build.py — Build Sphinx sub-projects (HTML / PDF).

Sub-project ids, titles, source dirs and PDF/no-PDF status all come from
documents.yaml (repo root; the same registry _shared/docrefs.py hands every
conf.py) — run './build.py list' to see the current set. Add a document
there, not here, to register a new sub-project.

Examples
--------
  ./build.py list                       # show registered documents
  ./build.py html                       # build all documents, HTML only
  ./build.py pdf                        # build all documents, LaTeX/PDF only
  ./build.py all                        # build HTML then PDF for everything
  ./build.py html sop-swdp              # build only sop-swdp (HTML)
  ./build.py html sop-toolval sop-soupval
  ./build.py html --base-url https://example.org/qms
                                         # absolute cross-document links/
                                         # intersphinx instead of the local
                                         # file:// fallback (used for deploys)
  ./build.py clean                      # remove _build/
  ./build.py serve                      # serve every built HTML doc on :8000
  ./build.py serve sop-swdp --port 9000 # serve just one, on a custom port
  ./build.py check                      # every conf.py (+ _shared/*.py) parses,
                                         # no Sphinx build needed

Build output lands in _build/<id>/html and _build/<id>/latex.

There is no separate "objects.inv-only" builder: Sphinx's html builder
always writes objects.inv as a side effect, so 'html' is the only way to
produce it. Cross-project navigation and intersphinx (see
_shared/conf_base.py::apply_cross_project_nav) resolve sibling projects
from each other's objects.inv, which only exists once that sibling has
built at least once — so 'html' always runs two passes: the first produces
those artefacts, the second lets every project pick up what its siblings
just produced, so cross-references resolve even for pages added in the
same run.
"""

import argparse
import ast
import functools
import http.server
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SHARED_DIR = REPO_ROOT / "_shared"

sys.path.insert(0, str(SHARED_DIR))
try:
    import docrefs  # noqa: E402
    _DOCREFS_IMPORT_ERROR = None
except SyntaxError as e:
    # A broken _shared/docrefs.py must not crash 'check' with a raw
    # traceback — that's exactly the failure it exists to report cleanly.
    # Every other subcommand needs a working docrefs, so they still fail
    # (via registry()), just not at import time.
    docrefs = None
    _DOCREFS_IMPORT_ERROR = e


def registry():
    """[(doc_id, confdir, path, pdf)] in documents.yaml order; confdir is
    absolute (docrefs.registry_entries() gives it relative to REPO_ROOT).
    """
    if docrefs is None:
        sys.exit(f"_shared/docrefs.py has a syntax error: {_DOCREFS_IMPORT_ERROR}")
    return [
        (doc_id, REPO_ROOT / confdir, path, pdf)
        for doc_id, confdir, path, pdf in docrefs.registry_entries()
    ]


def select(entries, wanted):
    """entries filtered down to `wanted` ids, in registry order (not
    argv order) so e.g. qms-overview always builds before the SOPs that
    intersphinx-reference it — regardless of the order the caller listed
    them in. Empty `wanted` means "everything".
    """
    if not wanted:
        return entries
    known = {e[0] for e in entries}
    unknown = [w for w in wanted if w not in known]
    if unknown:
        valid = ", ".join(e[0] for e in entries)
        sys.exit(f"Unknown document id(s): {', '.join(unknown)}\nValid: {valid}")
    requested = set(wanted)
    return [e for e in entries if e[0] in requested]


def run_sphinx(builder, confdir, outdir, doctrees, extra_args):
    outdir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable, "-m", "sphinx", "-b", builder, *extra_args,
        "-c", str(confdir), "-d", str(doctrees), str(confdir), str(outdir),
    ]
    subprocess.run(cmd, check=True)


def build_html(build_dir, doc_id, confdir, extra_args):
    outdir = build_dir / doc_id / "html"
    doctrees = build_dir / doc_id / ".doctrees"
    print(f"\n{'═' * 48}\n HTML  ▶  {doc_id}  ({confdir})\n{'═' * 48}")
    run_sphinx("html", confdir, outdir, doctrees, extra_args)


def build_pdf(build_dir, doc_id, confdir, extra_args):
    latexdir = build_dir / doc_id / "latex"
    doctrees = build_dir / doc_id / ".doctrees"
    print(f"\n{'═' * 48}\n PDF   ▶  {doc_id}  ({confdir})\n{'═' * 48}")
    run_sphinx("latex", confdir, latexdir, doctrees, extra_args)
    for tex in sorted(latexdir.glob("*.tex")):
        print(f"  → xelatex: {tex.name}")
        for _ in range(2):
            subprocess.run(
                ["xelatex", "-interaction=nonstopmode", tex.name],
                cwd=latexdir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                check=True,
            )
    print(f"  PDF files written to {latexdir}/")


def extra_sphinx_args(args):
    # Cross-project links (nav sidebar, intersphinx) are baked into the
    # cached environment/doctrees at read time. A DOCS_BASE_URL change alone
    # doesn't make Sphinx consider any document outdated, so an incremental
    # rebuild would silently keep serving old links from disk — force a full
    # re-read with -E whenever a base URL is supplied. Without --base-url,
    # incremental caching stays fast as before.
    return ["-E"] if args.base_url else []


def announce(entries, fmt, args):
    names = " ".join(e[0] for e in entries)
    base_url_suffix = f"  [base-url: {args.base_url}]" if args.base_url else ""
    print(f"\nBuilding: {names}  [format: {fmt}]{base_url_suffix}")


def cmd_list(args):
    entries = registry()
    width = max(len(e[0]) for e in entries)
    for doc_id, confdir, path, pdf in entries:
        rel_confdir = confdir.relative_to(REPO_ROOT)
        print(f"{doc_id:<{width}}  pdf={'yes' if pdf else 'no ':<3}  {rel_confdir}  ({path})")


def cmd_html(args):
    build_dir = Path(args.build_dir).resolve()
    entries = select(registry(), args.docs)
    os.environ["DOCS_BASE_URL"] = args.base_url or ""
    extra_args = extra_sphinx_args(args)
    announce(entries, "html", args)
    # Two passes: see the module docstring's objects.inv note.
    for _ in range(2):
        for doc_id, confdir, _path, _pdf in entries:
            build_html(build_dir, doc_id, confdir, extra_args)
    print(f"\nDone. Artefacts in {build_dir}/")


def cmd_pdf(args):
    build_dir = Path(args.build_dir).resolve()
    entries = select(registry(), args.docs)
    os.environ["DOCS_BASE_URL"] = args.base_url or ""
    extra_args = extra_sphinx_args(args)
    announce(entries, "pdf", args)
    for doc_id, confdir, _path, pdf in entries:
        if not pdf:
            print(f"\nSkipping PDF for '{doc_id}' (not a document-controlled record)")
            continue
        build_pdf(build_dir, doc_id, confdir, extra_args)
    print(f"\nDone. Artefacts in {build_dir}/")


def cmd_all(args):
    cmd_html(args)
    cmd_pdf(args)


def cmd_clean(args):
    build_dir = Path(args.build_dir).resolve()
    if build_dir.exists():
        shutil.rmtree(build_dir)
        print(f"Removed {build_dir}")
    else:
        print(f"Nothing to remove ({build_dir} does not exist)")


def cmd_serve(args):
    build_dir = Path(args.build_dir).resolve()
    if args.doc:
        serve_dir = build_dir / args.doc / "html"
        if not serve_dir.is_dir():
            sys.exit(
                f"No HTML build found for '{args.doc}' at {serve_dir}\n"
                f"Run './build.py html {args.doc}' first."
            )
        print(f"Serving {args.doc} at http://localhost:{args.port}/")
    else:
        if not build_dir.is_dir():
            sys.exit(f"No builds found at {build_dir}\nRun './build.py html' first.")
        print(f"Serving all projects at http://localhost:{args.port}/")
        print("Available:")
        for html_dir in sorted(build_dir.glob("*/html")):
            print(f"  http://localhost:{args.port}/{html_dir.parent.name}/html/")
        serve_dir = build_dir

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(serve_dir))
    with http.server.ThreadingHTTPServer(("", args.port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


def _check_files(files):
    """ast.parse each path (never imports it), printing OK/ERR per file.
    Returns whether every file parsed cleanly.
    """
    ok = True
    for f in files:
        rel = f.relative_to(REPO_ROOT)
        try:
            ast.parse(f.read_text(encoding="utf-8"))
            print(f"OK   {rel}")
        except SyntaxError as e:
            print(f"ERR  {rel}: {e}")
            ok = False
    return ok


def cmd_check(args):
    # _shared/*.py aren't in the per-document registry (they're imported by
    # every conf.py, not a sub-project themselves), so check them first —
    # this is plain text parsing, so it works even if docrefs.py itself is
    # what's broken (registry() needs a working docrefs, so it can't help
    # enumerate the per-document conf.py files below in that case).
    ok = _check_files(sorted(SHARED_DIR.glob("*.py")))

    if docrefs is None:
        sys.exit(1)

    doc_files = [confdir / "conf.py" for _doc_id, confdir, _path, _pdf in registry()]
    ok = _check_files(doc_files) and ok
    if not ok:
        sys.exit(1)


def add_build_dir_arg(parser):
    parser.add_argument(
        "--build-dir", metavar="DIR", default=str(REPO_ROOT / "_build"),
        help="build output directory (default: %(default)s)",
    )


def add_common_args(parser):
    parser.add_argument(
        "docs", nargs="*", metavar="doc-id",
        help="one or more document ids to build (default: all; see 'list')",
    )
    parser.add_argument(
        "--base-url", metavar="URL", default=os.environ.get("DOCS_BASE_URL", ""),
        help="absolute base URL for cross-document links/intersphinx, "
        "instead of the local file:// fallback (used for deploys)",
    )
    add_build_dir_arg(parser)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="build.py",
        description=__doc__.split("\n\n")[0],
        epilog=__doc__.split("Examples\n--------\n", 1)[1],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list registered documents")
    p_list.set_defaults(func=cmd_list)

    p_html = sub.add_parser("html", help="build HTML (default: every document)")
    add_common_args(p_html)
    p_html.set_defaults(func=cmd_html)

    p_pdf = sub.add_parser("pdf", help="build PDF (default: every PDF-enabled document)")
    add_common_args(p_pdf)
    p_pdf.set_defaults(func=cmd_pdf)

    p_all = sub.add_parser("all", help="build HTML then PDF (default: every document)")
    add_common_args(p_all)
    p_all.set_defaults(func=cmd_all)

    p_clean = sub.add_parser("clean", help="remove the build output directory")
    add_build_dir_arg(p_clean)
    p_clean.set_defaults(func=cmd_clean)

    p_serve = sub.add_parser("serve", help="serve built HTML docs locally")
    p_serve.add_argument(
        "doc", nargs="?", metavar="doc-id",
        help="serve only this document (default: serve the whole build directory)",
    )
    p_serve.add_argument(
        "--port", type=int, default=8000, help="port to serve on (default: %(default)s)",
    )
    add_build_dir_arg(p_serve)
    p_serve.set_defaults(func=cmd_serve)

    p_check = sub.add_parser(
        "check", help="sanity-check that every conf.py parses (no Sphinx build needed)",
    )
    p_check.set_defaults(func=cmd_check)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
