

{{ '=' * (7 + (cookiecutter.__full_name | length)) }}
PTCC - {{ cookiecutter.__full_name }}
{{ '=' * (7 + (cookiecutter.__full_name | length)) }}

.. doc_control::
   :version: {{ cookiecutter.document_version }}
   :based_on_template: tpl-qms-comply_001
   :owner: Quality Management
   :classification: Record


PTCC - Process Training and Compliance Confirmation
===================================================

Purpose
-------

This record confirms that the undersigned person:

* has read and understood the listed Standard Operating Procedures (SOPs),
* has received the required process training,
* agrees to follow the applicable procedures and processes,
* understands that compliance with the QMS is mandatory,
* acknowledges responsibility to work according to the current released versions
  of the referenced documents.

Scope
-----

This confirmation applies to all personnel contributing to regulated activities,
including but not limited to:

* software development,
* electronics development,
* system engineering,
* testing and verification,
* risk management,
* document management,
* maintenance activities.

Git Commit Requirements
-----------------------

This record shall be committed to the project repository by the respective user.

The commit shall:

* contain this completed training record,
* use a signed-off commit,
* use a verified cryptographic signature,
* be traceable to the responsible person.

Example workflow:

.. code-block:: bash

   git add docs/records/{{ cookiecutter.__folder_name }}/index.rst

   git commit -s -S -m "docs(qms): Confirm SOP training for {{ cookiecutter.__full_name }}"



Verification Requirements
-------------------------

The following conditions apply:

* The Git identity used for the commit shall uniquely identify the contributor.
* The commit signature shall be verified by the repository hosting platform.
* Repository branch protection rules should require:

  * signed commits,
  * authenticated users,
  * pull request review,
  * traceable history retention.

Review and Retention
--------------------

This record is considered a quality record and shall be retained according to
the applicable document retention procedure.

Changes to this document require:

* version control,
* review,
* approval according to the document control process.

Approval
-----------------------

By committing this document with a signed-off and verified commit, the user
electronically confirms the statements in this record. (if and only if the
cryptographic key/signature of the user has been verified upfront.

or

By signing the pdf version of this document (as the author), the user confirms the statements
of this records.

By signing the pdf version of this document (as reviewer and approver) that person confirms
that she/he has verified the signature of the author (the identity of the author
with an official Photo-ID and the electrnic signautre key if provided).

.. note::

   If the cryptographic electronic signature is not given in this document the cryptographic
   electronic signature is treated as **not verifed**.

   Any cryptographically signed commits by the author are subseqently treated as not-trusted.


Applicable SOPs
=================

The following SOPs are covered by this confirmation record.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - SOP ID
     - Version
     - Title
   * - sop-docctl
     - 1.x
     - SOP Document Control
   * - sop-swdp
     - 1.x
     - SOP Software Development Procedure
   * - sop-cybersec
     - 1.x
     - SOP Cybersecurity
   * - sop-req_design
     - 1.x
     - SOP Requirement and Design
   * - sop-impl
     - 1.x
     - SOP Implementation
   * - sop-verif
     - 1.x
     - SOP Verification
   * - sop-toolval
     - 1.x
     - SOP Tool Validation
   * - sop-soupval
     - 1.x
     - SOP SouP Validation


Training Confirmation
======================

I confirm that:

* I have read and understood all SOPs listed above.
* I know where to access the controlled versions of these documents.
* I will follow the defined procedures during my work.
* I will consult the responsible process owner or quality representative if
  uncertainties arise.
* I understand that deviations from the defined processes must be documented
  and approved according to the applicable procedures.

User Information
=================

.. list-table::
   :widths: 30 70

   * - Full Name
     - {{ cookiecutter.__full_name }}
   * - email address
     - {{ cookiecutter.email }}
   * - Responsibility/Role
     - {{ cookiecutter.role }}
   * - Department/Team/Company
     - {{ cookiecutter.department }}
   * - GPG signature public fingerprint
     - | {{ cookiecutter.gpg_fingerprint.replace('|', '\n       | ') }}


.. code-block:: bash
   :caption: Get the GPG signature (for verification)

   gpg --list-keys --keyid-format=long
