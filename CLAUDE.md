# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A Sphinx-based lean Quality Management System (QMS) documentation set for
medical device software development, aligned to IEC 62304 / ISO 13485
expectations. There is no application source code here — the repository
content is reStructuredText documentation, Sphinx configuration, and Python
build/governance tooling. "Building" means rendering documentation
(HTML/PDF), not compiling software.

This repository is self-contained: it has no submodules and depends on
nothing outside itself beyond the Python packages in
`_shared/requirements.txt` and a `xelatex` install for PDF output.

## Repository layout (multi sub-project Sphinx build)

Not one Sphinx project — one per document, each with its own `conf.py`,
built independently into `_build/<id>/{html,latex}`. The set of
sub-projects is entirely data-driven from `documents.yaml` (repo root) —
nothing is hardcoded elsewhere:

- `docs/qms-overview/` — portal landing page, methodology overview,
  glossary (HTML-only, no PDF; `pdf: false` in documents.yaml).
- `docs/sop/<id>/` — the 8 Standard Operating Procedures (`sop-docctl`,
  `sop-swdp`, `sop-req_design`, `sop-impl`, `sop-verif`, `sop-cybersec`,
  `sop-toolval`, `sop-soupval`). Some carry an HTML-only `appendix/`
  (document templates, tool usage guides) wrapped in `.. only:: html` —
  never in the PDF.
- `docs/records/<document-id>_<NNN>/` — versioned records (e.g.
  training/compliance confirmations); each folder is one immutable
  edition, `<NNN>` starting at `001`. Generate new ones from
  `templates/cookiecutter-ptcc-record/` (see `templates/README.md`).

`documents.yaml` (repo root) declares:
- `groups:` — nav sidebar sections (`dir:` confdir subfolder under
  `docs/`, `mode:` how a page's own group renders —
  `exclude_if_selected` / `single_doc_title_merge` / `always_keep`,
  `display:` collapsibility — `disabled_collapsing` /
  `collapsed_at_opening` / `not_collapsed_at_opening` / `no-display`).
- `documents:` — one entry per sub-project (`title`, `group`, `pdf`, `path`).

All shared Sphinx behavior lives in `_shared/`, pulled in by every
`conf.py`:
```python
from conf_base import apply_base_config, apply_cross_project_nav
apply_base_config(globals(), project_name="...", autosectionlabel_prefix="...")
apply_cross_project_nav(globals(), "<document-id>")
```
- `_shared/conf_base.py` — project meta, HTML theme (sphinx_rtd_theme),
  LaTeX/xelatex settings (PDF header: `<document-id> | <title> |
  <version>`; footer: `Copyright <year> <company from latex_documents> |
  <page>/<total>`), optional PDF-only signature section
  (`signature_section = "top"|"bottom"|"none"` set per-project in its
  own `conf.py`), and `get_doc_version()` — derives the sidebar/PDF
  version from the nearest `git describe --match <document-id>/*` tag
  (see Versioning below).
- `_shared/docrefs.py` — reads `documents.yaml`, builds the sidebar's
  grouped nav links and `intersphinx_mapping` for every sub-project;
  also exposes `registry_entries()` (used by `build.py`) and its own
  `list` CLI (`docrefs.py list`).
- `_shared/_ext/doc_control.py` — the `.. doc_control::` directive:
  renders the document-control metadata table (version, owner,
  classification, author, reviewed_by, approved_by, approval_date, ...)
  at the top of a document. `classification` is one of: SOP, Work
  Instruction, Record, Policy, Plan, Report, Specification, Register.
  Enforces `version` is `major.minor` for every classification except
  `Record` (which uses its own edition-per-folder scheme).
- `_shared/_templates/layout.html` + `_shared/_static/custom.css` —
  sidebar nav rendering (`reference_groups` block) and its styling
  (collapsible `<details>` groups with a unicode ▶ toggle, distinct
  caption/link colors).

## Common commands

```sh
# Install deps
pip install -r _shared/requirements.txt

# List registered documents (documents.yaml)
./build.py list

# Build all sub-projects, HTML only
./build.py html

# Build all sub-projects, HTML + PDF (requires xelatex)
./build.py all

# Build one sub-project
./build.py html sop-swdp

# Build only PDFs
./build.py pdf

# Serve built HTML locally
./build.py serve                    # all projects, port 8000
./build.py serve sop-swdp --port 9000

# Sanity-check every conf.py parses (no Sphinx build needed)
./build.py check

# Remove all build artefacts
./build.py clean
```

`build.py` (repo root) is the single build tool — there is no Makefile,
`build.sh`, `serve_html.sh`, or `check_syntax.py`; everything is this one
Python CLI. `qms-overview` always builds first (registry order), so
intersphinx cross-references from the SOPs resolve even in a
from-scratch build; HTML builds run two passes for the same reason
(each sub-project's `objects.inv` must exist before its siblings can
reference it).

There is no test suite; correctness is checked by whether the Sphinx
build succeeds (broken `:ref:`/intersphinx links fail or warn at build
time) and by `build.py check` for conf.py syntax.

## Document governance: docctl.py

`docctl.py` (repo root) is a CLI that edits a document's
`.. doc_control::` directive fields and commits the change with the
caller's own git identity (from `git config user.name`/`user.email`),
signed-off (`-s`) and GPG-signed (`-S`) — an unconfigured signing key is
a hard failure, not a skip.

```sh
./docctl.py list                                    # document-ids it can operate on
./docctl.py author <document-id> [--version VERSION]
./docctl.py review <document-id> [--force]
./docctl.py approve <document-id> [--effective-date YYYY-MM-DD] [--force]
./docctl.py bump-version <document-id> [--major | --minor]
```

- Commit subject: `docs(<document-id>): <Action> version <version>`.
- `author` → plain `Signed-off-by:`. `review`/`approve` add
  `Reviewed-by:`/`Approved-by:` trailers.
- `review` refuses unless `author` is already set, and refuses
  self-review (same committer email as the `author` commit, via `git
  blame`) unless `--force`. `approve` refuses unless `reviewed_by` is
  set *and* backed by an actual commit, unless `--force`. This enforces
  author -> review -> approve ordering.
- `approve` also creates a signed tag (`git tag -s`) named
  `<document-id>/<version>` — the release marker `conf_base.py`'s
  `get_doc_version()` reads back to render the sidebar/PDF version.
- `bump-version` starts a new version cycle for an already-released
  controlled document (refused for `classification: Record`): bumps
  `:version:` (`--minor` default: x.Y -> x.Y+1; `--major`: X.y -> X+1.0),
  removes `:author:`/`:reviewed_by:`/`:approved_by:`/`:approval_date:`
  entirely (so doc_control.py's own "not-authored-yet"/etc. placeholders
  take over), and rebases the document's `.. git_changelog::`
  `:rev-list:` to `<document-id>/<old-version>..HEAD` if that release
  tag exists.

This mirrors `sop-docctl`'s "Review and Approval Workflow"/"Starting an
Updated Version" sections, which describe the same steps as **manual**
git operations — `docctl` is documented there as an optional convenience
tool, not a requirement; its actual usage is written up in
`docs/sop/sop-docctl/appendix/docctl-usage.rst` (an HTML-only appendix).

## Versioning

Controlled documents (everything except `Record`) use `major.minor`:
minor for typo/formatting fixes (no retraining), major for content
changes (may require retraining/redistribution) — see `sop-docctl`'s
"Version Numbering". Released versions are tagged
`<document-id>/<version>` (e.g. `sop-docctl/1.0`), which
`get_doc_version()` resolves via `git describe` to render in the
sidebar/PDF: just the version if HEAD is exactly at the tag or on
`main`; `"<version> <sha>"` otherwise; the bare sha if no matching tag
is reachable.

Records are versioned differently: each edition is an immutable,
separately filed folder (`<document-id>_<NNN>`), not a revision of the
same document.

## CI / deployment

`.github/workflows/deploy-docs.yml` runs on push to `main`/`feature/**`,
builds every sub-project's HTML via `./build.py html` (with
`--base-url` if the `QMS_BASE_URL` repository variable is configured),
then deploys over SFTP via `lftp` to a Strato-hosted server. `main`
deploys to the site root; `feature/<branch>` deploys under its own
subfolder so multiple in-progress branches can coexist.

## Known gotcha

Each SOP's `.. git_changelog::` directive is filtered by
`filename_filter`, but `sphinx_git` only ever considers the **last 10
commits repo-wide** (not "the last 10 commits touching this file")
before that filter is applied. If none of those 10 happen to touch a
given SOP, the rendered change-history list is empty — which breaks the
LaTeX/PDF build (an empty `itemize` is a hard xelatex error:
"Something's wrong--perhaps a missing \item"). `docctl bump-version`
mitigates this going forward by pointing `:rev-list:` at `<tag>..HEAD`,
but an older/untouched SOP can still hit it.
