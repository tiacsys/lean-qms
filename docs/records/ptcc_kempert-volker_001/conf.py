import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.abspath(os.path.join(PROJECT_DIR, "..", "..", "..", "_shared"))
sys.path.insert(0, SHARED_DIR)

from conf_base import apply_base_config, apply_cross_project_nav  # noqa: E402


apply_base_config(
    globals(),
    project_name="PTCC - Volker Kempert",
    autosectionlabel_prefix="qms_ptcc_kempert_volker_001",
)

apply_cross_project_nav(globals(), "ptcc_kempert-volker_001")

# Keep the PDF minimal: this is a short signed record, not a manual — no
# title page, no table of contents, and no chapter breaks (top-level
# headings become \section, not \chapter). Suppressing the title page
# leaves an empty implicit level 0, which would otherwise number headings
# "0.1", "0.1.1", ...; secnumdepth=-1 drops heading numbers entirely.
latex_elements["maketitle"] = ""
latex_elements["tableofcontents"] = ""
latex_elements["preamble"] += "\n\\setcounter{secnumdepth}{-1}\n"
latex_toplevel_sectioning = "section"

# PDF-only sign-off block (Author/Reviewer/Approver) at the end of the
# document; "top"/"none" are also valid (see doc_control.py). No effect on
# the HTML build.
signature_section = "bottom"

latex_documents = [
    (
        "index",
        "ptcc_kempert-volker_001.tex",
        "PTCC - Volker Kempert",
        "TiaC Systems",
        "manual",
    ),
]
