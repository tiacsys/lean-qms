# Copyright (c) 2026 TiaC Systems
# SPDX-License-Identifier: Apache-2.0
"""Central cross-document reference registry for qms-base's Sphinx sub-projects.

All inter-document links are derived from a single registry file,
``documents.yaml`` (qms-base repo root), so each sub-project's ``conf.py`` only declares
its own identity (its registry key) and picks up the derived structures::

    import docrefs
    refs = docrefs.load("sop-swdp")

    html_context = {"reference_groups": refs.reference_groups}
    intersphinx_mapping = refs.intersphinx_mapping

To add a cross-reference target, add an entry to documents.yaml — nothing in
any conf.py needs to change. ``build.py`` also reads the registry (via the
``list`` CLI subcommand below) so its project registry and the PDF/no-PDF
split never drift out of sync with what conf.py sees.
"""

import argparse
import os
import sys
from pathlib import Path

import yaml

SHARED_DIR = Path(__file__).resolve().parent
REPO_ROOT = SHARED_DIR.parent
BUILD_ROOT = REPO_ROOT / "_build"
DEFAULT_REGISTRY = REPO_ROOT / "documents.yaml"


def _registry(registry=None):
    """Load, parse and validate the registry YAML."""
    registry = Path(registry) if registry else DEFAULT_REGISTRY
    with open(registry) as f:
        data = yaml.safe_load(f)
    _validate(data)
    return data


def _validate(data):
    """Raise ``ValueError`` on any registry validation problem."""
    groups = data.get("groups")
    if not groups:
        raise ValueError(
            "docrefs: registry 'groups:' is missing or empty — declare at "
            "least one group with an 'id' and 'title'"
        )
    group_ids = {g["id"] for g in groups}

    for group in groups:
        mode = group.get("mode", "exclude_if_selected")
        if mode not in _GROUP_MODES:
            raise ValueError(
                f"docrefs: group '{group['id']}' has mode '{mode}', which is "
                f"not one of {_GROUP_MODES}"
            )

        display = group.get("display", "disabled_collapsing")
        if display not in _GROUP_DISPLAYS:
            raise ValueError(
                f"docrefs: group '{group['id']}' has display '{display}', which is "
                f"not one of {_GROUP_DISPLAYS}"
            )

    for doc_id, meta in data.get("documents", {}).items():
        group = meta.get("group")
        if group is None:
            raise ValueError(f"docrefs: document '{doc_id}' is missing a 'group:' field")
        if group not in group_ids:
            raise ValueError(
                f"docrefs: document '{doc_id}' has group '{group}', which is "
                f"not a declared group id (known groups: {sorted(group_ids)})"
            )


#: Group ``mode:`` values (see documents.yaml's per-group field docs):
#:   "exclude_if_selected"    this_doc is excluded from its own group's nav
#:                            links (a page doesn't link to itself). Default
#:                            when a group has no ``mode:``.
#:   "single_doc_title_merge" same exclusion as "exclude_if_selected", for a
#:                            group whose membership always resolves to
#:                            exactly one document (e.g. "Overview") — that
#:                            single link then renders merged into the
#:                            caption instead of a caption + one-item list
#:                            (see the {% if group.links|length == 1 %}
#:                            check in _shared/_templates/layout.html).
#:   "always_keep"            every document in the group is always listed,
#:                            including this_doc — e.g. "Records", so a
#:                            person's own confirmation still shows up in
#:                            the roster while they're reading it.
_GROUP_MODES = ("exclude_if_selected", "single_doc_title_merge", "always_keep")

#: Group ``display:`` values (see documents.yaml's per-group field docs):
#:   "disabled_collapsing"      no expand/collapse control; the group is
#:                              always fully shown. Default when a group
#:                              has no ``display:``.
#:   "collapsed_at_opening"     the group is collapsible and starts
#:                              collapsed when the page loads.
#:   "not_collapsed_at_opening" the group is collapsible and starts
#:                              expanded when the page loads.
#:   "no-display"               the group is not shown at all, regardless
#:                              of how many links it would otherwise have.
_GROUP_DISPLAYS = (
    "disabled_collapsing",
    "collapsed_at_opening",
    "not_collapsed_at_opening",
    "no-display",
)


def _groups(data):
    """Ordered ``[{id, title, mode, display}]`` from the registry ``groups:`` list."""
    return [
        {
            "id": g["id"],
            "title": g["title"],
            "mode": g.get("mode", "exclude_if_selected"),
            "display": g.get("display", "disabled_collapsing"),
        }
        for g in data["groups"]
    ]


def grouped_links(this_doc, data, href_fn):
    """Ordered grouped cross-document links for ``this_doc``.

    Returns ``[{"id", "title", "mode", "display", "links": [{"label", "href"}]}]``:
      * groups in registry ``groups:`` order; documents in registry order;
      * groups with ``display: "no-display"`` are dropped entirely, as are
        groups left empty after filtering (no dangling heading);
      * ``label`` is the document ``title``; ``href`` is ``href_fn(doc_id, meta)``;
      * ``this_doc`` is excluded from its own group's links, unless that
        group's ``mode`` is ``"always_keep"`` (see ``_GROUP_MODES``).
    """
    documents = data["documents"]
    result = []
    for group in _groups(data):
        if group["display"] == "no-display":
            continue
        keep_current = group["mode"] == "always_keep"
        links = []
        for doc_id, meta in documents.items():
            if meta.get("group") != group["id"]:
                continue
            if doc_id == this_doc and not keep_current:
                continue
            links.append({"label": meta.get("title", doc_id), "href": href_fn(doc_id, meta)})
        if links:
            result.append(
                {
                    "id": group["id"],
                    "title": group["title"],
                    "mode": group["mode"],
                    "display": group["display"],
                    "links": links,
                }
            )
    return result


class Refs:
    """Derived cross-document link structures for the current document."""

    def __init__(self, reference_groups, intersphinx_mapping, pdf):
        self.reference_groups = reference_groups
        self.intersphinx_mapping = intersphinx_mapping
        self.pdf = pdf


def load(this_doc, registry=None):
    """Build the cross-document link structures for ``this_doc``.

    ``this_doc`` is the document's registry key (matches its directory name
    under docs/ and its _build/<key>/html output dir).
    """
    data = _registry(registry)
    documents = data["documents"]

    base_url = os.environ.get("DOCS_BASE_URL") or data.get("base_url", "")
    base_url = base_url.rstrip("/")
    if base_url and "://" not in base_url:
        # A bare host/path (e.g. "a.b.c" or "a.b.c/qms") has no scheme, so a
        # browser resolves "a.b.c/sop-swdp/html/index.html" as a *relative*
        # link against the current page instead of an absolute URL — it
        # silently navigates nowhere real instead of erroring, which is far
        # more confusing than requiring a scheme up front.
        print(
            f"docrefs: --base-url/DOCS_BASE_URL '{base_url}' has no scheme "
            f"(http:// or https://) — defaulting to https://{base_url}",
            file=sys.stderr,
        )
        base_url = f"https://{base_url}"

    def _base_href(doc_id, meta):
        """Directory-style URL for ``doc_id``, no trailing slash."""
        path = meta.get("path", f"{doc_id}/html")
        if base_url:
            return f"{base_url}/{path}"
        return "file://" + str((BUILD_ROOT / path).resolve())

    def _page_href(doc_id, meta):
        """Clickable link to ``doc_id``'s landing page.

        Must point at index.html itself, not just the bare directory: a
        file:// URL with no trailing slash and no filename is what a
        directory *without* a slash looks like to a browser, and Firefox
        (and others) won't auto-append one — the link silently fails to
        navigate instead of resolving to the index page.
        """
        return _base_href(doc_id, meta) + "/index.html"

    reference_groups = grouped_links(this_doc, data, _page_href)

    intersphinx_mapping = {}
    for doc_id, meta in documents.items():
        if doc_id == this_doc:
            continue
        path = meta.get("path", f"{doc_id}/html")
        inv_path = BUILD_ROOT / path / "objects.inv"
        # Local inventory only (no URL fallback): a missing inventory just
        # warns instead of Sphinx trying to fetch "<url>/objects.inv" over
        # the network, which fails loudly for a file:// url. A sibling that
        # hasn't built yet just doesn't get an intersphinx entry on this pass
        # (see build.py's two-pass HTML build).
        if inv_path.exists():
            intersphinx_mapping[doc_id] = (_base_href(doc_id, meta) + "/", str(inv_path))

    this_meta = documents.get(this_doc, {})
    return Refs(reference_groups, intersphinx_mapping, pdf=this_meta.get("pdf", True))


def _group_confdir(data, group_id):
    """Docs subdirectory a group's sub-projects live under (e.g. ``sop``,
    ``records``), or ``""`` if the group's documents sit directly under
    ``docs/`` (see each group's optional ``dir:`` field in documents.yaml).
    """
    for g in data["groups"]:
        if g["id"] == group_id:
            return g.get("dir", "")
    return ""


def registry_entries(registry=None):
    """``[(doc_id, confdir, path, pdf)]`` in registry order, for build.py.

    ``confdir`` is the project's source directory relative to the repo root
    (e.g. ``docs/sop/sop-swdp``, ``docs/records/rd-confirm-..._00``,
    ``docs/qms-overview``), derived from the document's group ``dir:``.
    """
    data = _registry(registry)
    entries = []
    for doc_id, meta in data["documents"].items():
        group_dir = _group_confdir(data, meta["group"])
        confdir = f"docs/{group_dir}/{doc_id}" if group_dir else f"docs/{doc_id}"
        path = meta.get("path", f"{doc_id}/html")
        entries.append((doc_id, confdir, path, meta.get("pdf", True)))
    return entries


def _cli(argv=None):
    parser = argparse.ArgumentParser(
        prog="docrefs", description="Query the qms-base document registry (documents.yaml)."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser(
        "list",
        help="print '<id> <confdir> <path> <pdf:0|1>' lines for build.py",
        description="Print one line per registered document: its id, source "
        "confdir (relative to the repo root), deploy path, and whether it "
        "wants a PDF build.",
    )
    p_list.add_argument("--registry", metavar="documents.yaml", default=None)

    args = parser.parse_args(argv)
    if args.command == "list":
        for doc_id, confdir, path, pdf in registry_entries(args.registry):
            sys.stdout.write(f"{doc_id} {confdir} {path} {'1' if pdf else '0'}\n")


if __name__ == "__main__":
    _cli()
