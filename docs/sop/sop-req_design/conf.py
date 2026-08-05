import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.abspath(os.path.join(PROJECT_DIR, "..", "..", "..", "_shared"))
sys.path.insert(0, SHARED_DIR)

from conf_base import apply_base_config, apply_cross_project_nav  # noqa: E402


apply_base_config(
    globals(),
    project_name="SOP — Software Requirement and Design Procedure",
    autosectionlabel_prefix="qms_sop_req_design",
)

apply_cross_project_nav(globals(), "sop-req_design")

# PDF-only sign-off block (Author/Reviewer/Approver) at the top of the
# document, right after the title page/ToC; "bottom"/"none" are also valid
# (see doc_control.py). No effect on the HTML build.
signature_section = "top"

# No chapter formatting: top-level headings become \section, not
# \chapter (no "Chapter N" banner, no forced page break before each).
latex_toplevel_sectioning = "section"
latex_elements["preamble"] += "\n\\renewcommand{\\thesection}{\\arabic{section}}\n"

latex_documents = [
    (
        "index",
        "sop-req_design.tex",
        "SOP — Software Requirement and Design Procedure",
        "TiaC Systems",
        "manual",
    ),
]
