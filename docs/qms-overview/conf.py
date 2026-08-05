import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED_DIR = os.path.abspath(os.path.join(PROJECT_DIR, "..", "..", "_shared"))
sys.path.insert(0, SHARED_DIR)

from conf_base import apply_base_config, apply_cross_project_nav  # noqa: E402


# HTML-only: the portal landing page, methodology overview, glossary and
# cross-cutting records/templates are not a document-controlled record with
# its own PDF (see documents.yaml's pdf: false) - no latex_documents here.
apply_base_config(
    globals(),
    project_name="Lean QMS for Medical Software",
    autosectionlabel_prefix="qms_overview",
)

apply_cross_project_nav(globals(), "qms-overview")
