# templates

Scaffolding tools for qms-base. Not part of the Sphinx build itself.

## cookiecutter-ptcc-record

Generates a new PTCC (Process Training and Compliance Confirmation) record —
the same kind of standalone sub-project as
`docs/records/ptcc_kempert-volker_001/` — from
`docs/qms-overview/doc-templates/tpl-qms-comply.rst`, asking for the
**User Information** section's data interactively.

### Install

```sh
python -m pip install -r templates/requirements.txt
```

### Generate a record

Run from the qms-base repo root so the record lands directly under
`docs/records/`:

```sh
cookiecutter templates/cookiecutter-ptcc-record --output-dir docs/records
```

You'll be prompted for: first name, last name, email, role, department, the
record edition (`document_version`, three digits — `001` for a first-time
confirmation, `002`/`003`/... for a later re-confirmation), and the GPG
signature public fingerprint block.

The fingerprint block is multi-line and terminal prompts can't accept
embedded newlines, so join its lines with `|` when entering it, e.g.:

```
pub   ed25519/94D23A6534BE3697 2025-09-06 [SC]|      5012128B8FE98CF84B3CD0A394D23A6534BE3697|uid   [ultimate] Jane Doe (general purpose) <jane.doe@example.com>|sub   cv25519/580AC9FC2C3B9A0D 2025-09-06 [E]
```

The `|`-joined lines are expanded back into the record's GPG fingerprint
table cell at render time.

For a non-interactive/scripted run, pass values directly:

```sh
cookiecutter templates/cookiecutter-ptcc-record --output-dir docs/records --no-input \
  first_name=Jane last_name=Doe email=jane.doe@example.com \
  role="Software Engineer" department=RnD document_version=001 \
  gpg_fingerprint="pub   ed25519/... [SC]|      .../uid   [ultimate] Jane Doe ... |sub   cv25519/... [E]"
```

### Folder naming

The generated sub-project folder is named
`<document-id>_<document-version>`, where `document-id` is always
`ptcc_<last-name>-<first-name>` (lowercased). E.g. Jane Doe's first
confirmation lands at
`docs/records/ptcc_doe-jane_001/ptcc_doe-jane_001.rst`.

The doc_control block inside the record only ever shows the plain
`document_id` (`ptcc_doe-jane`, without the version) — the trailing
`_<version>` on the folder/file name is stripped by
`doc_control.py::_extract_document_id`, since it identifies the *edition*,
not the document's identity. `:version:` is filled from the same
`document_version` you were prompted for.

### After generating

The generator prints the exact `documents.yaml` entry to add (under the
`records` group) — see its printed "Next steps". Nothing is registered
automatically: adding a controlled record to the registry is a deliberate,
reviewed step, not something the generator should do silently.
