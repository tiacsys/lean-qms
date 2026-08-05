import re
import sys

document_version = "{{ cookiecutter.document_version }}"
email = "{{ cookiecutter.email }}"
first_name = "{{ cookiecutter.first_name }}"
last_name = "{{ cookiecutter.last_name }}"

errors = []

if not re.fullmatch(r"[0-9]{3}", document_version):
    errors.append(
        "document_version must be a three-digit number starting at '001' "
        f"(e.g. '001', '002', ...), got: {document_version!r}"
    )

if "@" not in email:
    errors.append(f"email does not look like a valid email address: {email!r}")

if not first_name.strip():
    errors.append("first_name must not be empty")

if not last_name.strip():
    errors.append("last_name must not be empty")

if errors:
    sys.exit("Invalid input:\n" + "\n".join(f"  - {e}" for e in errors))
