.. _sop-docctl:

Software Lifecycle Documentation Control Procedure
************************************************************

.. only:: html

    .. contents:: Table of Content
        :local:
        :depth: 3

Document Control
================

.. doc_control::
   :version: 1.0
   :owner: QA
   :classification: SOP

The lean quality management system for **medical software development** is
**aligned to IEC 62304-supporting QMS expectations**.

Overview
--------

This :term:`SOP` defines the characteristics/formatting of the managed documents

- Identification
- Referencing
- Validity

It defines the roles and responsibilities of persons who are involved with
:term:`Controlled Document`

- author
- reviewer
- approver

and enforces that author is a different person than the reviewer.

It provides policy like activities that the persons fulfilling a certain role
have to do and have to follow.


Purpose
-------

This procedure defines how software lifecycle documents are created, reviewed, approved, versioned,
changed, archived, and released within a Git-controlled documentation system using Sphinx-rendered
source files.

The objective is to ensure controlled documentation that supports compliance with IEC 62304 and related QMS expectations.


Scope
-----

This :term:`SOP` applies to all controlled documents used within the software lifecycle, including but not limited to:

- Software Development Plans
- Requirements Specifications
- Architecture / Design Documents
- Risk Management Records
- Verification Protocols / Reports
- Traceability Records
- Maintenance Records
- Problem Resolution Records
- Release Notes
- :term:`SOP`'s / Work Instructions

Documents are authored as text-based source files (Markdown / reStructuredText) rendered using Sphinx and maintained under Git version control.


Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.


.. git_changelog ::
  :filename_filter: docs/sop/sop-docctl/sop-docctl.rst


.. _sop/sop-docctl/references:

References
----------

Requirements of standards this SOP implements or complies with:

- IEC 62304:2006 + A1:2015 - Medical device software — Software life cycle processes
  - Clause 4.1 - Quality Management System
- ISO 13485:2016 - Medical devices — Quality management systems — Requirements for regulatory purpose
  - Clause 4.2.4 - Documentation requirements, control of documents
  - Clause 4.2.5 - Documentation requirements, control of records
  - Clause 5 - Management responsibility, responsibilities, approvals

Document Content
================

Roles and Responsibilities
--------------------------

Author
~~~~~~

Responsible for:

- Drafting and updating content
- Technical correctness of proposal
- Referencing impacted records
- Opening merge/pull request
- Update the document content based on reviewers request

Reviewer (Independent)
~~~~~~~~~~~~~~~~~~~~~~

Responsible for:

- Independent review of content
- Checking completeness, clarity, consistency
- Submit document change request to authors if any
- Confirm the reviewed document content

.. attention::

   Reviewer shall not be sole author of the change.

Approver
~~~~~~~~

Responsible for:

- Final release decision
- Ensuring review completed
- Ensuring training / communication if needed

Configuration Manager / Repo Maintainer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Responsible for:

- Repository permissions
- Branch protections
- Release tags
- Backup and retention

System Description
------------------

Documentation system consists of:
- ``The documents`` as source files (human and machine readable) in Git repository
- ``git repository`` as source of truth

  - Branch protection rules
  - Version history
  - Release branch (main) for **approved** versions
  - Development branches for documents that are not yet approved.

- ``Cryptographically signed commits`` for review and document approval
- Cryptographically signed commits for review users understanding and
  consideration.
- ``Pull/Merge request`` for review and approval workflow

  - Review comments as evidence of review
  - Approval via merge approval or signed approval record

- ``Sphinx Build`` pipeline

  - Rendered HTML/PDF artifacts of actually effective versions.
  - Performs **checks for consistency, integrity, versioning, traceability**, and formatting.

- ``Web server``

  - Online inspection of documents (effective versions) as official records.

.. note::

   No uncontrolled local copies shall be considered official records.
   This is prevented by only publishing the last released and effective version on the web server.
   No pdf publishing, no local copies, no printing is allowed.

   The official record is the online version on the web server.

.. note::

   PDF versions are only required if gpg signatures are not available and allow for
   printing, manual signing, and archiving. The effective electtronic equivalents
   of the printed versions are distributed via webserver.

Documents
~~~~~~~~~~

Documents are a RestructuredText documents.
Each document is organized in one file named *<document identifier>.rst*.
This file contains a *docctl* sphinx directive.
This file might include content from other files, named *<document identifier>_<sub-topic>.rst*

Modifications are checked into git repository, whereby a commit shall only address one document.

Each :term:`controlled document` is structured

- Title
- *doc-ctl*
- table of content
- Overview
- Purpose
- Scope
- References
- Definitions

Document Identification
~~~~~~~~~~~~~~~~~~~~~~~~

Each :term:`controlled document` has a :term:`document identifier`.
That allows to reference the document in a unique way across the DMS.


- E.g. sop-docctl

- The document identifier is composed of document identifier sniplets.
  The sniplets are separated by dashes "-".

  There are a few conventions:

  - 1st sniplet is the document classification like :term:`SOP`, or project abbreviation
  - 2nd sniplet is a project specific classification or a sequential number
  - 3rd sniplet (if available is a sequential number)

- Document identifiers must be unique.
- The document identifier represents all
  versions of a document. However, at one point in time only one version is
  valid (aka effective). It is the latest approved version.

  .. note::

    The document identifier is the base name of the document file where
	  the *doc_ctl* directive is located.

	  The *doc_ctl* directive might contain the the document_id as option.
	  If so, the name must be identical to the base name of the document file.


.. _sop/sop-docctl/document-control-fields:

Document Control
~~~~~~~~~~~~~~~~


The document implicitly contains the following information:

- **Title**
  The title of the document. It is but more verbose and
  readable than the document identifier.

- **Document Identifier**
  The document identifier is a short identifier of a document without whitespaces.
  It is unique accross a DMS. It is the base name of the document file where
  the *doc_ctl* directive is located.


Information about a document that are derived from the git revision management system:

- **Status** (Draft / In Review / Released / Obsolete)

  The status is not explicitly modelled. It is implicitly derivable from git

  - *Draft* - the document is developed in a dev branch
  - *In Review* - the document  is part of a pull request in a dev branch
  - *Released* - the document is on main branch
  - *Obsolete* - the document is removed from main branch

  The status is not stored within the document, it is always derived from the git revision management system.
  This is to avoid that the status is not updated by the author, which would lead to confusion and noncompliance.

Each :term:`controlled document` is guided by the *doc_ctl* restructured text directive.

The *doc_ctl* contains:

- **Version**
  For controlled documents, the version is ``major.minor`` (see
  :ref:`sop/sop-docctl/version-numbering`). The first version of a
  controlled document is ``1.0``. Records use their own versioning instead
  (see :ref:`sop/sop-docctl/version-numbering`).


- **Effective date**

  - Mandatory: if the document is a process document; i.e a :term:`SOP`.
    The effective date is after all team has been trained.
  - Optional: if the document is not a process document, will be set to the approval date.
  - Shall be provided in ISO 8601 format: YYYY-MM-DD.

- **Owner**

  A organizational unit, or a role. E.g. QA for quality assurance unit, or
  project team abbreviation.


Sample *doc_ctl* directive for a :term:`SOP`:

.. code-block:: yaml

   version: v002
   owner: Quality
   effective_date: 2026-06-06

Extracted from git revision management system: see
:ref:`sop/sop-docctl/review-and-approval-workflow` for exactly how each of
these is recorded.

- **Author**
  The person who created the document or made the change. Recorded via a
  ``Signed-off-by:`` trailer on the commit that sets ``:author:``.
- **Reviewer**
  The person who independently reviewed the document or the change.
  Recorded via a ``Reviewed-by:`` trailer on the commit that sets
  ``:reviewed_by:`` — made by a different git identity than whoever's
  commit set ``:author:``.
- **Approver**
  The person who approved the document or the change for release.
  Recorded via an ``Approved-by:`` trailer on the commit that sets
  ``:approved_by:``, valid only once a genuine reviewer commit exists.
- **Approval date**
  The date the change was approved, in ISO 8601 format (YYYY-MM-DD).


Authoring Rules
---------------

Documents shall be written in repository source format:

- Markdown files `*.md`
- Restructured text files `*.rst`

Authors shall:

- Use templates where available (for new documents)
- Use clear headings
- Reference related records by ID
- Avoid ambiguous language
- Keep traceability links current

.. note ::

  Sphinx processes all *DMS directives* and pulls relevant information from git repository.
  It complains if:

  - the document identifier is not unique
  - the document identifier is not identical to the base name of the document file
  - the effective date is missing for a SOP
  - the effective date is not in ISO 8601 format
  - the version is not in the correct format
  - the version is not incremented for a new release
  - the document is not on main branch but has a version higher than the latest released version

.. note::

  A git commit hook wil only accept commit message that reference the document identifier of the changed document.


.. _sop/sop-docctl/review-and-approval-workflow:

Review and Approval Workflow
----------------------------

This procedure is enforced by the structure of the Git commit history
itself — specific commit subjects, trailers, and a release tag — not by
any particular hosting platform's pull-request features. What this
:term:`SOP` requires is that the commits described below exist; whether
they are produced by hand with plain ``git`` commands or with the help of
a tool is a matter of choice (see the Appendix).

Drafting
~~~~~~~~

Author creates feature branch:

The branch name should follow the convention:


.. code::

   docs/<document identifier>_<optional short description of the change>


The first commit should be either the new document-template with updated document control sections.
The commit message should look like:

.. code::

   docs(document identifier): Create from template

   Template: <template name>

or the updated document by only incremented version.
The commit message should look like:

.. code::

   docs(document identifier): Bump version to <incremented version>


Subsequent commits should be incremental changes to the document,
with commit messages referencing the document identifier and describing the change.
The scope and type should always be :code:`docs(document identifier):`.

.. note ::

   We follow conventional commit style for commit messages, with the document identifier in parentheses at the start of the message.
   see https://www.conventionalcommits.org/en/v1.0.0/ for more details.

   Scope is the document identifier.
   Type of change is not needed for document changes.

   Type is needed if the changes address publishing workflow (*ci*) or checking and output processing (*build*)
   or update to directives (*feat, fix*) or fix formatting (*style*).

Once the document is ready to be reviewed, the author sets ``:author:``
and ``:version:``
on the ``.. doc_control::`` directive to their own identity (name and
e-mail, as configured in ``git config user.name``/``user.email``) and
commits that change with a ``Signed-off-by:`` trailer:

.. code::

   docs(<document identifier>): Author version <version>

   Signed-off-by: <Author Name> <author@example.org>

Review Request
~~~~~~~~~~~~~~

The author submits the change for review — via a merge/pull request, or
however the team routes review requests — stating:

- Purpose of change
- Impacted documents
- Reason for change
- Evidence references if applicable

Independent Review
~~~~~~~~~~~~~~~~~~~

Review includes:

- Content adequacy
- Grammar/readability
- Consistency with other records
- Regulatory impact
- Traceability completeness

Once the review is complete and no further changes are requested, the
reviewer records this by setting ``:reviewed_by:`` on the document's
``.. doc_control::`` directive to their own identity and committing that
change:

.. code::

   docs(<document identifier>): Review version <version>

   Signed-off-by: <Reviewer Name> <reviewer@example.org>
   Reviewed-by: <Reviewer Name> <reviewer@example.org>

.. attention::

   At least one reviewer independent of authorship shall review.

   The commit that set ``:author:`` and the commit that sets
   ``:reviewed_by:`` shall have been made by two different git identities
   (compared by committer e-mail) — a reviewer reviewing their own
   authorship is not a valid review.

.. note::

   Commits should be GPG-signed (``git commit -S``) in addition to
   ``--signoff``, so the identity named in the trailer is
   cryptographically verifiable rather than just self-asserted free text.

Approval
~~~~~~~~

Approval occurs by an authorized approver, once a genuine reviewer commit
(see `Independent Review`_ above) exists — not merely a ``:reviewed_by:``
value typed into the file without a backing commit. The approver sets
``:approved_by:`` and ``:approval_date:`` (ISO 8601, YYYY-MM-DD) and
commits:

.. code::

   docs(<document identifier>): Approve version <version>

   Signed-off-by: <Approver Name> <approver@example.org>
   Approved-by: <Approver Name> <approver@example.org>

``:effective_date:`` shall also be set at this point for process
documents (:term:`SOP`'s — see :ref:`sop/sop-docctl/document-control-fields`).

Release
~~~~~~~

The approver additionally creates a signed Git tag (``git tag -s``) on
the approval commit, named ``<document identifier>/<version>`` (see
`Released Versions`_) — the authoritative marker of a released version.

.. note::

   The steps above — checking segregation of duties, committing with the
   right subject/trailers, tagging on approval — are easy to get wrong by
   hand. The optional ``docctl`` command-line tool automates them and
   refuses to proceed if a prerequisite is missing (e.g. approving
   without a genuine review commit). Using it is a matter of choice, not
   a requirement of this :term:`SOP` — see the Appendix for its usage.

Furthermore, after the approval:

- the PR is merged by a rebase commit to the controlled branch.
- the development branch is removed

This is a formal process and can be done be either role author, reviewer,
approver.

Upon merge to controlled branch:

- CI builds Sphinx html outputs from controlled branch, where effective
  documents are maintained and publishes them to web server.

.. note:: If printed and signed documents are needed

   Upon merge to controlled branch, CI builds pdf output or the document

   The pdf output gets printed and auther, reviewer and approver
   sign the pdf manually and archive the printed document.


Segregation of Duties
---------------------

The following controls apply:

.. list-table::
   :header-rows: 1

   * - Activity
     - Minimum Requirement
   * - Authoring
     - Author
   * - Review
     - Independent reviewer
   * - Approval
     - Authorized approver

Single-person author-review-approve cycle is not permitted unless
formally justified for low-risk internal records.

Version Control
---------------

Source Versioning
~~~~~~~~~~~~~~~~~

All changes shall occur through Git commits.

Commits shall follow `conventional commits <https://conventionalcommits.org>`_.

Commits that modify content of a document shall be scoped with
document identifier and typed as doc


.. _sop/sop-docctl/released-versions:

Released Versions
~~~~~~~~~~~~~~~~~

Approved documents shall be tagged by ``<document identifier>/<version>``,
created on the approval commit (see
:ref:`sop/sop-docctl/review-and-approval-workflow`).

e.g.

.. code::

   sop-docctl/1.0


.. _sop/sop-docctl/version-numbering:

Version Numbering
~~~~~~~~~~~~~~~~~

Controlled documents — SOPs, templates, plans, specifications, and any
other document-controlled artifact not classified as ``Record`` — are
versioned as ``major.minor``. The initial version of a controlled document
is ``1.0``.

- **Minor** version increases (e.g. ``1.0`` -> ``1.1``) are typo fixes,
  formatting/layout changes, and other edits that do not change the
  document's content or meaning. No re-training or re-distribution is
  required.
- **Major** version increases (e.g. ``1.0`` -> ``2.0``) change content:
  anything that changes what the document requires, permits, or describes.
  A major version increase potentially requires new training and active
  distribution of the updated document to affected users.

A higher version number indicates a more recent version of the document.

Records (e.g. training/compliance confirmations) are versioned
differently: each edition of a record is an immutable, separately-filed
document rather than a revision of the same one — see the record's own
template/registry conventions instead of this section.

.. _sop/sop-docctl/starting-an-updated-version:

Starting an Updated Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting a new version of an already-released controlled document
requires, as a single commit:

- ``:version:`` incremented per `Version Numbering`_ (minor for
  cosmetic changes, major for content changes);
- ``:author:``, ``:reviewed_by:``, ``:approved_by:`` and
  ``:approval_date:`` removed from the ``.. doc_control::`` directive —
  the new version has not yet been authored, reviewed, or approved, and
  leaving the previous version's values in place would misrepresent the
  new draft as already signed off;
- the ``.. git_changelog::`` directive's change history rebased to start
  from the previous release, e.g. ``:rev-list: <document
  identifier>/<previous version>..HEAD``, so it reflects only the
  changes made for this new version rather than an arbitrary window of
  recent commits.

.. code::

   docs(<document identifier>): Bump version to <new version>

Once bumped, the document re-enters `Review and Approval Workflow`_ from
`Drafting`_ for the new version.

.. note::

   The optional ``docctl`` command-line tool's ``bump-version``
   subcommand (``--major``/``--minor``, default ``--minor``) performs the
   steps above in a single commit — see the Appendix.

Change Control
--------------

Changes to released documents require:

- Change rationale
- Review
- Approval
- New version
- Audit trail in Git history


Obsolete Documents
------------------

Superseded documents shall:

- **Are not published anymore**, and therefore are not accessible anymore
  (neither for reading nor referencing). There superseeded by the new versions or
  by "non-existence in the active branch (named main) in git"

- Remain retrievable, by simply browsing and checking out the git history at the
  respective  tag of that document.

- Not be used for current operations, by not providing the rendered content.


Traceability
------------

Traceability on document level is done by the :ref:`sop/sop-docctl/references` section.
Sphinx link check kicks in if a reference is to a :term:`SOP` document or similar.

Traceability on Sub-document level like

- Requirements IDs
- Risk IDs
- Test IDs
- Release IDs
- Problem reports

is not addressed by this SOP.

Electronic Records / Audit Trail
--------------------------------

Git history serves as audit evidence for:

- Author identity
- Date/time of commits
- Change diffs
- Review comments
- Approval evidence
- Release tags

User accounts shall be individual, not shared.

Access Control
--------------

Repository permissions shall enforce:

- Read access as defined
- Write access (ability to commit) for authors, reviewers and approver
- Protected main/release branches
- Mandatory review before merge

Backup and Retention
--------------------

Repositories and released artifacts shall be backed up regularly.

Retention period shall follow company retention policy.

Periodic Review
---------------

This :term:`SOP` and documentation process shall be periodically reviewed for
continued suitability.

Recommended interval: annually.

Nonconformities
---------------

Detected issues such as:

- Missing review
- Unauthorized changes
- Wrong version usage
- Broken traceability

shall be handled per :term:`CAPA` / nonconformance process.

.. only:: html

   Appendix
   ========

   Optional tooling referenced by this SOP:

   .. toctree::
      :maxdepth: 1

      appendix/docctl-usage

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

   Controlled Document
     Document subject to this :term:`SOP`.

   SOP
     Standard Operating Procedure.

   Reviewer
     Independent person evaluating adequacy.

   Approver
     Authorized role releasing document.

   Effective Version
     Approved released version.

   Git Tag
     Immutable identifier for released state.

   Sphinx Build
     Rendered output from controlled source.

   Document Identifier
     Short identifier of a document without whitespaces.
	 Is unique accross a DMS.

   DMS
     Document Management System
