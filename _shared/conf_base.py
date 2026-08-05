# _shared/conf_base.py
#
# Copyright (c) 2026 TiaC Systems
# SPDX-License-Identifier: Apache-2.0
#
# Shared Sphinx configuration for all sub-projects.
# Each project's conf.py calls:
#
#   import sys, os
#   PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
#   SHARED_DIR = os.path.abspath(os.path.join(PROJECT_DIR, "..", "..", "_shared"))
#   sys.path.insert(0, SHARED_DIR)
#   from conf_base import apply_base_config, apply_cross_project_nav
#   apply_base_config(globals(), project_name="...", autosectionlabel_prefix="...")
#   apply_cross_project_nav(globals(), "<project-key>")
#
# After the call, the project conf.py can override any value (e.g.
# latex_documents, latex_appendices).

import datetime
import os
import re
import subprocess
import sys

SHARED_DIR = os.path.dirname(os.path.abspath(__file__))
if SHARED_DIR not in sys.path:
    sys.path.insert(0, SHARED_DIR)

import docrefs  # noqa: E402


def _document_id_from_dir(project_dir):
    """Same derivation as doc_control.py's ``_extract_document_id``: the
    confdir's basename, minus a trailing ``_<version>`` (see
    templates/cookiecutter-ptcc-record and documents.yaml's per-group
    ``dir:``). Used here to build the ``<document-id>/*`` tag-match glob.
    """
    basename = os.path.basename(os.path.normpath(project_dir))
    return re.sub(r"_\d+$", "", basename)


def _current_branch(project_dir):
    """Best-effort branch name: CI checkouts are commonly detached HEAD,
    where 'git symbolic-ref' finds nothing, so GITHUB_REF_NAME (set by
    GitHub Actions to the branch/tag being built — see deploy-docs.yml's
    own github.ref_name check) is tried first.
    """
    ref_name = os.environ.get("GITHUB_REF_NAME")
    if ref_name:
        return ref_name
    try:
        return subprocess.check_output(
            ["git", "symbolic-ref", "--short", "-q", "HEAD"],
            cwd=project_dir,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return None


def get_doc_version(project_dir):
    """The version shown in the sidebar's "Version ..." element (and,
    since they share this value, html_title / the PDF footer's \\release).

    Per SOP-DOCCTL's "Released Versions": a controlled document is tagged
    ``<document-id>/<version>`` on release (e.g. ``sop-docctl/1.0``). This
    finds the nearest such tag reachable from HEAD via
    ``git describe --match <document-id>/*`` and renders:
      - just the version, if HEAD is exactly at that tag, or on the "main"
        branch (main is policy-only ever the latest released state per
        SOP-DOCCTL and README's CI section, so a nonzero commit count past
        the tag there is just other documents' unrelated commits, not this
        one having drifted from its release);
      - "<version> <sha>" otherwise (a work-in-progress build past the
        last release, worth distinguishing by commit);
      - just the sha, if no tag matching this document exists at all.
    """
    version = os.environ.get("VERSION")
    if version:
        return version.strip()

    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=project_dir,
            text=True,
        ).strip()
    except Exception:
        return "unknown"

    document_id = _document_id_from_dir(project_dir)
    try:
        described = subprocess.check_output(
            ["git", "describe", "--tags", "--match", f"{document_id}/*"],
            cwd=project_dir,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        # No tag matching this document is reachable from HEAD.
        return sha

    tag_prefix = f"{document_id}/"
    distance_match = re.search(r"^(.*)-(\d+)-g[0-9a-fA-F]+$", described)
    exact = distance_match is None
    tag = described if exact else distance_match.group(1)
    if not tag.startswith(tag_prefix):
        return sha
    doc_version = tag[len(tag_prefix):]

    if exact or _current_branch(project_dir) == "main":
        return doc_version
    return f"{doc_version} {sha}"


def _latex_escape(text):
    """Escape LaTeX special characters for safe use outside math mode
    (e.g. a document-id like ``ptcc_kempert-volker`` contains ``_``, which
    LaTeX otherwise treats as a math-mode subscript and errors on).
    """
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


_SIGNATURE_LINE_MACRO = r"""
% \signatureline{Role}{Name} - a bold role label, the signer's name (if
% known), and a blank ruled line underneath for them to sign on. Shared by
% the (currently unused) \signaturemaketitle title-page mechanism below and
% by doc_control's per-project "signature_section" (top/bottom, PDF only —
% see doc_control.py's doctree-resolved handler).
\newcommand{\signatureline}[2]{%
    \noindent\textbf{#1}\par
    \vspace{0.35cm}
    \noindent#2\par
    \vspace{0.20cm}
    \noindent\makebox[\linewidth]{\rule{0pt}{0.5pt}\hrulefill}\par
    \vspace{0.85cm}
}
"""


def _signature_preamble(signature_data, project):
    return rf"""
\newcommand{{\signaturemaketitle}}{{%
    \sphinxmaketitle
    \clearpage
    \thispagestyle{{empty}}
    \vspace*{{1.5cm}}
    \begin{{center}}
        {{\Huge\bfseries Signatures}}
    \end{{center}}
    \vspace{{2.0cm}}
    \signatureline{{Author}}{{{signature_data["author"]}}}
    \signatureline{{Reviewer}}{{{signature_data["reviewer"]}}}
    \signatureline{{Approver}}{{{signature_data["approver"]}}}
    \vfill
    \noindent\textbf{{Project:}} \textit{{{project}}}\par
    \clearpage
}}
"""

def setup(app):
    app.add_config_value('releaselevel', 'mvp', 'env')

def apply_base_config(
    g,
    *,
    project_name,
    autosectionlabel_prefix,
    include_sphinx_needs=False,
    include_signature_page=False,
    signature_data=None,
):
    """
    Populate the calling conf.py's globals() with shared Sphinx settings.

    Parameters
    ----------
    g : dict
        globals() of the calling conf.py
    project_name : str
        Human-readable project name (sets ``project`` and ``html_title``).
    autosectionlabel_prefix : str
        Prefix used by prefix_autosectionlabel (e.g. 'qms_sop_swdp').
    include_sphinx_needs : bool
        Add sphinx_needs and myst_parser to the extension list.
    include_signature_page : bool
        Generate a LaTeX signature page.
    signature_data : dict or None
        Keys: author, reviewer, approver. Defaults to placeholder strings.
    """
    project_dir = g.get("PROJECT_DIR", os.getcwd())

    if signature_data is None:
        signature_data = {
            "author": "Author Name",
            "reviewer": "Reviewer Name",
            "approver": "Approver Name",
        }

    # ------------------------------------------------------------------ paths
    # Ensure shared extensions are on sys.path
    import sys

    shared_ext = os.path.join(SHARED_DIR, "_ext")
    if shared_ext not in sys.path:
        sys.path.insert(0, shared_ext)

    # Sphinx only calls a conf.py's own module-level setup(app) — it never
    # looks inside imported helper modules. Inject ours into the caller's
    # globals() (the same dict Sphinx reads back as the conf.py namespace)
    # so every sub-project picks it up without redeclaring it.
    g["setup"] = setup

    # ------------------------------------------------------------------ meta
    g["project"] = project_name
    g["html_title"] = f"{project_name} {get_doc_version(project_dir)}"
    g["copyright"] = f"{datetime.datetime.now().year}, TiaC Systems"
    g["author"] = "Volker Kempert"
    g["language"] = "en"
    g["version"] = get_doc_version(project_dir)
    g["release"] = g["version"]

    # ------------------------------------------------------------------ source
    g["master_doc"] = "index"
    g["source_suffix"] = {".rst": "restructuredtext"}
    g["exclude_patterns"] = ["_build", "Thumbs.db", ".DS_Store", "_glossary_terms.rst"]

    # ------------------------------------------------------------------ extensions
    base_extensions = [
        "sphinx.ext.todo",
        "sphinx.ext.ifconfig",
        "sphinx.ext.githubpages",
        "sphinx.ext.intersphinx",
        "sphinxcontrib.plantuml",
        "sphinxcontrib.mermaid",
        "sphinx_git",
        "sphinx_rtd_theme",
        "sphinx.ext.inheritance_diagram",
        # shared custom extensions
        "doc_control",
        "prefix_autosectionlabel",
    ]
    if include_sphinx_needs:
        base_extensions = ["myst_parser", "sphinx_needs"] + base_extensions
    g["extensions"] = base_extensions

    # ------------------------------------------------------------------ autosectionlabel
    g["autosectionlabel_prefix_document"] = True
    g["autosectionlabel_prefix"] = autosectionlabel_prefix

    # ------------------------------------------------------------------ misc
    g["pygments_style"] = "sphinx"
    g["todo_include_todos"] = True

    # ------------------------------------------------------------------ HTML
    g["html_theme"] = "sphinx_rtd_theme"
    g["html_logo"] = os.path.join(SHARED_DIR, "_static", "bridle-logo.svg")
    g["html_favicon"] = os.path.join(SHARED_DIR, "_static", "bridle-favicon.ico")
    g["html_theme_options"] = {
        "logo_only": False,
        "prev_next_buttons_location": "bottom",
        "style_external_links": False,
        "vcs_pageview_mode": "",
        "style_nav_header_background": "white",
        "flyout_display": "hidden",
        "version_selector": True,
        "language_selector": False,
        "collapse_navigation": True,
        "sticky_navigation": True,
        "navigation_depth": 3,
        "includehidden": True,
        "titles_only": False,
    }
    g["html_static_path"] = [os.path.join(SHARED_DIR, "_static")]
    g["html_css_files"] = ["custom.css"]
    if os.environ.get("DRAFT_DEPLOY"):
        g["html_css_files"].append("draft.css")
    g["templates_path"] = [os.path.join(SHARED_DIR, "_templates")]

    # ------------------------------------------------------------------ LaTeX
    sig_preamble = (
        _signature_preamble(signature_data, project_name)
        if include_signature_page
        else ""
    )
    sig_maketitle = (
        r"\signaturemaketitle" if include_signature_page else r"\sphinxmaketitle"
    )

    document_id = _document_id_from_dir(project_dir)
    copyright_year = datetime.datetime.now().year
    # The company name comes from latex_documents' author field (its 4th
    # tuple element), but latex_documents is only assigned by the calling
    # conf.py *after* this apply_base_config() call returns, so it isn't
    # available here yet. Sphinx itself always turns that field into the
    # standard \author{...} LaTeX command, though, so \qmscopyrightauthor
    # just captures a reference to \@author (not its expansion — this is a
    # plain \def, not \edef) to resolve lazily once \author{...} has run,
    # right before \begin{document}.
    company_macro = r"""
\makeatletter
\newcommand{\qmscopyrightauthor}{\@author}
\makeatother
"""
    # sphinxlatexstylepage.sty (pulled in by \usepackage{sphinx}) defines the
    # "normal" and "plain" pagestyles via \fancypagestyle — the body and ToC
    # pages select those with \pagestyle{normal}/{plain} (see the generated
    # .tex), not a bare "fancy", so a plain \pagestyle{fancy} here is inert
    # and gets clobbered. Redefining the same two named styles (after
    # \usepackage{sphinx} has run) is what actually sticks.
    _page_style = rf"""
    \fancyhf{{}}
    \fancyhead[L]{{{_latex_escape(document_id)}}}
    \fancyhead[C]{{{_latex_escape(project_name)}}}
    \fancyhead[R]{{{_latex_escape(g["release"])}}}
    \fancyfoot[L]{{Copyright {copyright_year} \qmscopyrightauthor. All rights reserved}}
    \fancyfoot[R]{{\thepage/\pageref{{LastPage}}}}
    \renewcommand{{\headrulewidth}}{{0.4pt}}
    \renewcommand{{\footrulewidth}}{{0.4pt}}
    """
    header_footer = rf"""
{company_macro}
\fancypagestyle{{normal}}{{{_page_style}}}
\fancypagestyle{{plain}}{{{_page_style}}}
"""

    g["latex_engine"] = "xelatex"
    g["latex_use_xindy"] = False
    g["latex_domain_indices"] = False
    g["latex_elements"] = {
        "papersize": "a4paper",
        "pointsize": "11pt",
        "figure_align": "htbp",
        "inputenc": "",
        "utf8extra": "",
        "classoptions": "oneside,openany",
        "preamble": r"""
\usepackage{longtable}
\usepackage{array}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage{lastpage}
\usepackage{xcolor}
\usepackage{tabularx}
\usepackage{graphicx}
"""
        + _SIGNATURE_LINE_MACRO
        + sig_preamble
        + header_footer
        + r"""
% Do not add any index or glossary
\let\printindex\relax
\let\printglossary\relax
\let\printglossaries\relax
""",
        "maketitle": sig_maketitle,
        "printindex": "",
    }

    # ------------------------------------------------------------------ PlantUML
    g["plantuml_theme"] = "azusa-color"
    g["plantuml_output_format"] = "svg"
    g["plantuml_latex_output_format"] = "eps"


# ---------------------------------------------------------------------------
# Cross-project navigation (nav sidebar, intersphinx)
# ---------------------------------------------------------------------------
#
# Derived from the central registry documents.yaml (repo root) — see docrefs.py.
# documents.yaml is the single source of truth for the set of qms-base
# sub-projects; build.py reads the same file (via `docrefs.py list`) so its
# project registry and PDF/no-PDF split never drift out of sync with what
# conf.py sees.


def apply_cross_project_nav(g, current_key):
    """Wire nav sidebar links and intersphinx for every other document in
    the central registry (documents.yaml, repo root).

    Call after apply_base_config(). Populates:
      - g["html_context"]["reference_groups"]: grouped nav links rendered by
        the {% block menu %} override in _shared/_templates/layout.html.
      - g["intersphinx_mapping"]: one entry per sibling that has already
        produced an objects.inv on disk (skipped otherwise, e.g. on a fresh
        first pass before any project has built) so a missing sibling
        artifact degrades quietly instead of failing the build.
    """
    refs = docrefs.load(current_key)
    html_context = g.setdefault("html_context", {})
    html_context["reference_groups"] = refs.reference_groups
    intersphinx_mapping = g.setdefault("intersphinx_mapping", {})
    intersphinx_mapping.update(refs.intersphinx_mapping)
