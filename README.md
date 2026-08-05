# README

This is a sphinx, git, pr based lean QMS system for software development
portion of medical products.

It addresses the Quality Management System (QMS) related requirements as
stated in the ISO 62304 standard.

Sphinx is used to structure and reference text based

- SOPs, templates, and arbitrary explanations to obtain web broseable output as well as
  PDF document output
- With proper linking and referencing in both html output and pdf output
- With proper version, revision injection derived from git

Git is used to organize

  - Revisioning/baselining, diffing
  - Reviewing and approval by PR/by signoff
  - Ensure related SOPs and templates are consistent over time

Detailed guidance is in [SOP-DOCCTL](/docs/sop/sop-docctl/sop-docctl.rst)

## Repository layout (multi sub-project Sphinx build)

This is not one Sphinx project — it's ten, each with its own `conf.py`,
built independently into `_build/<name>/{html,latex}`:

| Sub-project | Confdir | Content |
|---|---|---|
| `qms-overview` | `docs/qms-overview/` | Portal page, methodology overview, glossary, cross-cutting templates (HTML only, no PDF) |
| `sop-docctl` | `docs/sop/sop-docctl/` | SOP Document Control |
| `sop-swdp` | `docs/sop/sop-swdp/` | SOP Software Development Procedure + appendix (`tpl-swdp`, `tpl-swrs`, `tpl-swds`) |
| `sop-req_design` | `docs/sop/sop-req_design/` | SOP Requirement and Design Procedure |
| `sop-impl` | `docs/sop/sop-impl/` | SOP Implementation Procedure |
| `sop-verif` | `docs/sop/sop-verif/` | SOP Verification Procedure |
| `sop-cybersec` | `docs/sop/sop-cybersec/` | SOP Cybersecurity Procedures |
| `sop-toolval` | `docs/sop/sop-toolval/` | SOP Tool Validation Procedure + appendix (`tpl-toolval`) |
| `sop-soupval` | `docs/sop/sop-soupval/` | SOP SouP Validation Procedure + appendix (`tpl-soupval`) |
| `ptcc_kempert-volker_001` | `docs/records/ptcc_kempert-volker_001/` | PTCC training/compliance confirmation record (group `records`) |

Every SOP is its own controlled document — one PDF per SOP — and lives
under `docs/sop/`. A SOP's document templates are published as a LaTeX
appendix of that SOP's own PDF/HTML document rather than as standalone
documents. Templates that are not owned by a single SOP (e.g.
`tpl-qms-comply`) live in `qms-overview`. Each signed training/compliance
confirmation record (per contributor) is its own standalone sub-project
under `docs/records/`, registered under the `records` document group in
`documents.yaml`. A record's folder is named `<document-id>_<version>`,
where `document-id` is `ptcc_<last-name>-<first-name>` and `version` is a
three-digit edition starting at `001` — a re-confirmation gets its own
`002`, `003`, ... folder rather than editing the previous (already-signed)
one. The record's `doc_control` block only shows the plain `document_id`
(the `_<version>` suffix is stripped, since it's the edition, not the
document's identity) and its own `:version:` matching the folder. Generate
a new one with the `templates/cookiecutter-ptcc-record` cookiecutter
template — see [templates/README.md](templates/README.md).

All shared Sphinx behavior (theme, LaTeX settings, custom extensions,
sibling-project navigation) lives in `_shared/` and is pulled in by every
sub-project's `conf.py` via `_shared/conf_base.py`.

## Building

### Prerequisites

1. Install python
2. Install sphinx and extensions
```
python -m pip install -r _shared/requirements.txt
```

### Building

```sh
# List registered documents (documents.yaml)
./build.py list

# Build all sub-projects, HTML only
./build.py html

# Build all sub-projects, HTML + PDF (requires xelatex)
./build.py all

# Build one sub-project (name is one of: qms-overview sop-docctl sop-swdp
# sop-req_design sop-impl sop-verif sop-cybersec sop-toolval sop-soupval
# ptcc_kempert-volker_001)
./build.py html sop-swdp

# Build only PDFs (every SOP except qms-overview)
./build.py pdf

# Sanity-check that every conf.py parses (no Sphinx build needed)
./build.py check
```

Run live
```sh
./build.py serve                    # all projects at http://localhost:8000/<name>/html/
./build.py serve sop-swdp           # just one project
./build.py serve --port 9000        # custom port
```

point your browser to [localhost:8000](http://localhost:8000) and reload the
page after each rebuild

Clean all build artefacts: `./build.py clean`

## CI

A deployment job deploys to a static CDN, that may or may not be public.
This job is sensitive about branches and tags.
- main branch (represents latest released) - deploys each sub-project to
  `base-dir/qms/<name>/html`
- dev/xyz branch (represents updates) - deploys each sub-project to
  `base-dir/qms/xyz/<name>/html`

## License

Code and tooling (`build.py`, `docctl.py`, `_shared/`, CI workflows) are
licensed under [Apache-2.0](LICENSE). Documentation content (everything
under `docs/`, `templates/`) is licensed under
[CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt). Full license texts are under
[`LICENSES/`](LICENSES/); source files carry an `SPDX-License-Identifier`
comment identifying which license applies.
