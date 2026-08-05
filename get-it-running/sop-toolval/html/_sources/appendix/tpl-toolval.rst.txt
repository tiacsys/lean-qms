

:orphan:

.. _tpl-toolval:

MyProject — Tool Validation Report: [Tool Name]
*************************************************

.. Commentary

   This template guides you in producing a Tool Validation Report (TVR)
   that is under full QMS control. Complete every section in accordance
   with :ref:`sop-toolval`. Sections marked N/A for the assigned
   tool category must still appear in the document — write "N/A" and
   state the reason.

.. todo::

   1. Replace ``MyProject`` with your project name everywhere in this document
   2. Replace ``[Tool Name]`` with the actual name of the tool being validated
   3. Replace ``[Version]`` with the exact version string of the tool
   4. Fill in the ``.. doc_control::`` fields (owner, effective_date)
   5. Complete each section per :ref:`sop-toolval`
   6. Remove or resolve all ``.. todo::`` blocks before releasing this record

.. todo::

   Verify Inter-Sphinx link configuration so that ``qms:sop-toolval`` and
   ``qms:sop-docctl`` resolve correctly in your project's Sphinx build.

.. _control:

.. doc_control::
   :version: 001
   :based_on_template: 001
   :owner: MyProject
   :classification: Record
   :effective_date: 2026-06-06


.. contents:: Table of Content
   :local:
   :depth: 3

Document Control
================

Overview
--------

This document is the Tool Validation Report for [Tool Name] version [Version],
used in **MyProject**. It is produced in accordance with :ref:`sop-toolval`.

Purpose
-------

The purpose of this report is to record the validation evidence for [Tool Name]
and to demonstrate that it is fit for its intended use in the MyProject software
development lifecycle, in compliance with IEC 62304 clause 5.1.2.

Scope
-----

This report covers [Tool Name] as used for [intended purpose] within MyProject.
It documents the classification rationale, validation approach, test results,
anomalies encountered, and the final acceptance decision.

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history is the result of a query to
the git repository.

.. code::

  .. git_changelog ::
      :filename_filter: docs/qms/MyProjectAbbr-toolval-[toolname].rst

References
----------

Applied SOPs:

- SOP-TOOLVAL :ref:`sop-toolval` — Tool Validation SOP
- SOP-DOCCTL :ref:`sop-docctl:sop-docctl` — Document Control SOP

Definitions
-----------

No project-specific terms defined. See :ref:`sop-toolval` for term
definitions applicable to this record.

Tool Identification
===================

.. todo::

   Fill in every row of the table below. The version string must be the
   exact version as reported by the tool itself (e.g. output of
   ``tool --version``). The operating environment must match the
   environment in which the tool is actually used (CI, local workstation,
   container image, etc.).

.. list-table:: Tool Identification
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Value
   * - Tool Name
     - [Tool Name]
   * - Vendor / Author
     - [Vendor or author name, URL]
   * - Version validated
     - [Exact version string, e.g. 1.2.3]
   * - License type
     - [e.g. MIT, Apache 2.0, commercial — licence reference]
   * - Intended use in this project
     - [Brief description of how and where the tool is used]
   * - Operating environment
     - [OS name and version, CPU architecture, container image / native install]
   * - Responsible engineer
     - [Full name and role]
   * - Validation date
     - [YYYY-MM-DD]

Tool Classification
===================

.. todo::

   Evaluate each criterion in the table below and record your assessment.
   Assign the tool to Category 1, 2, or 3 as defined in
   :ref:`sop-toolval`. Provide a concise rationale sentence after the
   table.

.. list-table:: Classification Criteria
   :header-rows: 1
   :widths: 50 35 15

   * - Criterion
     - Assessment
     - Result
   * - Output is independently verifiable by a downstream process or review
       step (i.e. errors would be caught before affecting a deliverable)
     - [Your assessment]
     - [Yes / No]
   * - Tool directly generates or modifies deliverable software or safety-
       relevant documentation without independent verification
     - [Your assessment]
     - [Yes / No]
   * - Assigned Category (1 / 2 / 3)
     - [Rationale for category assignment]
     - [1 / 2 / 3]

**Classification statement:** [Tool Name] is assigned **Category [1/2/3]**
because [brief rationale, e.g. "its output is directly included in the
released firmware without an independent verification step"].

Validation Approach
===================

.. todo::

   State which qualification stages are required for the assigned category
   and describe how they will be carried out. Delete the rows that are not
   applicable.

Based on the assigned category, the following qualification stages are
required:

.. note::

   - **Category 1** — Tool identification only (Sections `Tool Identification`_
     and `Tool Classification`_ are sufficient). IQ, OQ, and PQ sections must
     be present but may be marked N/A.
   - **Category 2** — IQ and OQ are required. PQ is not required.
   - **Category 3** — IQ, OQ, and PQ are all required.

.. list-table:: Validation Approach Summary
   :header-rows: 1
   :widths: 25 15 60

   * - Qualification Stage
     - Required?
     - Approach
   * - Installation Qualification (IQ)
     - [Yes / No / N/A]
     - [Describe how installation will be verified]
   * - Operational Qualification (OQ)
     - [Yes / No / N/A]
     - [Describe functional test strategy]
   * - Performance Qualification (PQ)
     - [Yes / No / N/A]
     - [Describe end-to-end / realistic-use test strategy]

Installation Qualification (IQ)
================================

.. note::

   This section is required for Category 2 and Category 3 tools.
   For Category 1 tools, mark this section **N/A** and state the reason.

.. todo::

   Execute each IQ test case, record the actual result, and mark Pass or
   Fail. Add rows as needed. At minimum, verify the correct version is
   installed, all declared dependencies are present, and the tool is
   accessible in the CI/CD environment.

.. list-table:: IQ Test Cases
   :header-rows: 1
   :widths: 10 30 25 25 10

   * - Test ID
     - Description
     - Expected Result
     - Actual Result
     - Pass / Fail
   * - IQ-01
     - Correct tool version is installed and reported
     - Version string matches ``[Version]``
     - [Actual output]
     - [Pass / Fail]
   * - IQ-02
     - All declared runtime dependencies are present
     - No missing-dependency errors on launch
     - [Actual output]
     - [Pass / Fail]
   * - IQ-03
     - Tool is accessible in the CI/CD environment
     - Command exits with code 0; version banner visible in pipeline log
     - [Actual output]
     - [Pass / Fail]

**IQ Conclusion:**

.. list-table:: IQ Sign-Off
   :header-rows: 1
   :widths: 20 20 20 40

   * - Outcome
     - Tester
     - Date
     - Notes
   * - [Pass / Fail]
     - [Name]
     - [YYYY-MM-DD]
     - [Any remarks or deviations]

Operational Qualification (OQ)
================================

.. note::

   This section is required for Category 2 and Category 3 tools.
   For Category 1 tools, mark this section **N/A** and state the reason.

.. todo::

   Define OQ test cases that verify the tool behaves correctly for each
   function it performs within MyProject. Provide specific inputs and
   compare actual outputs against expected outputs. Add rows as needed.

.. list-table:: OQ Test Cases
   :header-rows: 1
   :widths: 10 25 15 20 20 10

   * - Test ID
     - Description
     - Input
     - Expected Output
     - Actual Output
     - Pass / Fail
   * - OQ-01
     - [Describe the functional behaviour being tested]
     - [Specific input value or file]
     - [Expected result or artefact]
     - [Observed result]
     - [Pass / Fail]
   * - OQ-02
     - [Describe the functional behaviour being tested]
     - [Specific input value or file]
     - [Expected result or artefact]
     - [Observed result]
     - [Pass / Fail]
   * - OQ-03
     - [Describe error-handling or boundary behaviour]
     - [Specific edge-case input]
     - [Expected result or error message]
     - [Observed result]
     - [Pass / Fail]

**OQ Conclusion:**

.. list-table:: OQ Sign-Off
   :header-rows: 1
   :widths: 20 20 20 40

   * - Outcome
     - Tester
     - Date
     - Notes
   * - [Pass / Fail]
     - [Name]
     - [YYYY-MM-DD]
     - [Any remarks or deviations]

Performance Qualification (PQ)
================================

.. note::

   This section is required for Category 3 tools only.
   For Category 1 and Category 2 tools, mark this section **N/A** and
   state the reason.

.. todo::

   Define PQ test cases that verify the tool performs correctly under
   realistic project conditions (real data, full pipeline, representative
   workload). Add rows as needed.

.. list-table:: PQ Test Cases
   :header-rows: 1
   :widths: 10 30 30 20 10

   * - Test ID
     - Scenario
     - Acceptance Criterion
     - Result
     - Pass / Fail
   * - PQ-01
     - [Realistic end-to-end scenario reflecting actual project use]
     - [Measurable acceptance criterion]
     - [Observed result]
     - [Pass / Fail]
   * - PQ-02
     - [Realistic end-to-end scenario reflecting actual project use]
     - [Measurable acceptance criterion]
     - [Observed result]
     - [Pass / Fail]

**PQ Conclusion:**

.. list-table:: PQ Sign-Off
   :header-rows: 1
   :widths: 20 20 20 40

   * - Outcome
     - Tester
     - Date
     - Notes
   * - [Pass / Fail]
     - [Name]
     - [YYYY-MM-DD]
     - [Any remarks or deviations]

Anomaly Log
===========

.. todo::

   Record every anomaly observed during validation. If no anomalies were
   found, replace the table with the statement below and retain it. For
   each anomaly, assign a unique ID (e.g. ANO-01), assess severity, record
   the root cause and disposition (accepted with rationale / rejected /
   workaround defined), and track the status to closure.

No anomalies detected during validation.

.. Uncomment and complete the table below if anomalies were found:
..
.. .. list-table:: Anomaly Log
..    :header-rows: 1
..    :widths: 10 30 15 20 20 5
..
..    * - Anomaly ID
..      - Description
..      - Severity (Critical / Major / Minor)
..      - Root Cause
..      - Disposition
..      - Status
..    * - ANO-01
..      - [Description of anomaly]
..      - [Critical / Major / Minor]
..      - [Root cause analysis]
..      - [Accepted with rationale / Rejected / Workaround defined]
..      - [Open / Closed]

Acceptance Decision
===================

.. todo::

   Record the final acceptance decision. Replace the placeholder text,
   state any conditions or restrictions on use, and obtain signatures from
   the Tester, Reviewer, and QA Approver before releasing this record.

[Tool Name] version [Version] is **accepted** / **rejected** for use in
**MyProject** for the purpose of [intended use].

**Conditions / restrictions** (if any):

- [List any restrictions on use, e.g. "only to be used with input files
  conforming to schema version X", "not to be used for safety-critical
  output without secondary review", etc.]
- If no conditions apply, write: None.

.. list-table:: Acceptance Sign-Off
   :header-rows: 1
   :widths: 20 25 20 35

   * - Role
     - Name
     - Date
     - Signature
   * - Tester
     - [Full name]
     - [YYYY-MM-DD]
     - [Wet ink / electronic ref.]
   * - Reviewer
     - [Full name]
     - [YYYY-MM-DD]
     - [Wet ink / electronic ref.]
   * - QA Approver
     - [Full name]
     - [YYYY-MM-DD]
     - [Wet ink / electronic ref.]

Revalidation Criteria
=====================

.. todo::

   Review the default revalidation triggers listed below. Add or adjust
   project-specific triggers if required by MyProject's risk profile or
   regulatory context.

This tool validation is valid until one of the following revalidation
triggers occurs, as defined in :ref:`sop-toolval`:

- The tool is updated to a new version.
- The tool is used for a new purpose not covered by this report.
- The operating environment changes significantly (OS upgrade, new CI
  platform, new container base image, etc.).
- An anomaly is discovered during routine use that calls the validation
  conclusions into question.
- An annual review determines that revalidation is warranted.

Upon any trigger, a new or amended Tool Validation Report shall be
produced and approved before the tool is returned to use.
