:orphan:

.. _tpl_soupval:

MyProject — SouP Evaluation Report: [SouP Item Name]
*****************************************************

.. Commentary

   This template guides you in producing a SouP Evaluation Report (SER)
   that is under full QMS control. Complete every section in accordance
   with :ref:`sop-soupval`. Sections marked N/A for the assigned
   safety category must still appear in the document — write "N/A" and
   state the reason.

.. todo::

   1. Replace ``MyProject`` with your project name everywhere in this document
   2. Replace ``[SouP Item Name]`` with the actual name of the SouP component
   3. Replace ``[Version]`` with the exact version string of the SouP item
   4. Fill in the ``.. doc_control::`` fields (owner, effective_date)
   5. Complete each section per :ref:`sop-soupval`
   6. Remove or resolve all ``.. todo::`` blocks before releasing this record

.. todo::

   Verify Inter-Sphinx link configuration so that ``qms:sop-soupval`` and
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

This document is the SouP Evaluation Report for [SouP Item Name] version [Version],
integrated into **MyProject**. It is produced in accordance with :ref:`sop-soupval`.

Purpose
-------

The purpose of this report is to record the evaluation evidence for [SouP Item
Name] and to demonstrate that it is safe and fit for its intended use in the
MyProject software architecture, in compliance with IEC 62304 clauses 5.3.3,
5.3.6, 5.7, 7.1.2, and 7.1.3.

Scope
-----

This report covers [SouP Item Name] as used for [intended purpose] within
MyProject. It documents the safety category rationale, functional and performance
requirements, anomaly evaluation, integration verification results, risk control
measures, and the final acceptance decision.

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history is the result of a query to
the git repository.

.. code::

  .. git_changelog ::
      :filename_filter: docs/qms/MyProjectAbbr-soupval-[soupname].rst

References
----------

Applied SOPs:

- SOP-SOUPVAL :ref:`sop-soupval` — SouP Validation SOP
- SOP-DOCCTL :ref:`sop-docctl:sop-docctl` — Document Control SOP

Definitions
-----------

No project-specific terms defined. See :ref:`sop-soupval` for term
definitions applicable to this record.

SouP Item Identification
========================

.. todo::

   Fill in every row of the table below. The version string must be the
   exact version as reported by the package manager, release tag, or
   commit hash. The architecture location must correspond to the
   component diagram or software architecture description in the SWDS.

.. list-table:: SouP Item Identification
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Value
   * - SouP Item Name
     - [SouP Item Name]
   * - Item Type
     - [Library / Framework / OS component / SDK / Firmware HAL / Other]
   * - Vendor / Upstream Project
     - [Vendor or project name, URL]
   * - Version validated
     - [Exact version string, commit hash, or package hash]
   * - Reference URL's
     - [Where is the source code or/or documentation for this version?]
   * - License type
     - [e.g. MIT, Apache 2.0, BSD-3-Clause, commercial — licence reference]
   * - Architecture location
     - [Module or subsystem in which the SouP item is integrated]
   * - Intended use in this project
     - [Brief description of what function the SouP item provides]
   * - Prerequisites
     - | [OS name and version, CPU architecture, hardware interface
       | container image / native install]

Intended Use
------------

.. todo::

   Brief description of what function the SouP shall be used and the SouP item provides

Safety Category Assignment
===========================

.. todo::

   Evaluate each criterion in the table below and record your assessment.
   Assign the SouP item to Category A or B as defined in
   :ref:`sop-soupval`. Provide a concise rationale paragraph after
   the table. If Category A is assigned, document the architectural
   control (if any) that prevents the item from contributing to a
   hazardous situation.

.. list-table:: Safety Category Criteria
   :header-rows: 1
   :widths: 55 30 15

   * - Criterion
     - Assessment
     - Result
   * - | Could the SouP item process, transform,
       | or display data that affects
       | patient safety or clinical decision-making?
     - [Your assessment]
     - [Yes / No]
   * - | Could a failure or incorrect behavior
       | of the SouP item contribute to
       | a hazardous situation (ISO 14971)?
     - [Your assessment]
     - [Yes / No]
   * - | Is there a downstream architectural control
       | (independent verification layer)
       | that would detect and contain a
       | SouP item failure before it
       | affects a safety-relevant output?
     - | [Your assessment — describe
       | the control if present]
     - [Yes / No]
   * - Assigned Safety Category (A / B)
     - [Rationale for category assignment]
     - [A / B]

**Category statement:** [SouP Item Name] is assigned **Category [A/B]** because
[brief rationale, e.g. "it implements the communication protocol parser whose
output is used directly in a safety-critical data path without independent
re-validation"].

SouP Item Requirements
=======================

.. note::

   This section is required for Category B SouP items.
   For Category A items, mark this section **N/A** and state the reason.

.. todo::

   Specify the functional, performance, interface, and constraint requirements
   that [SouP Item Name] must satisfy within MyProject. These requirements
   form the basis for the integration verification test cases in the next
   section. Add rows as needed.

Functional Requirements
-----------------------

.. todo::

   Add sphinx needs detailed software requirements.

Performance Requirements
------------------------

.. todo::

   Add sphinx needs detailed software requirements.

Interface Requirements
----------------------

.. todo::

   Add sphinx needs detailed software requirements
   Optionally reference design specs/ protocol specs (like http 1.1, json schema, etc)

Constraint Requirements
-----------------------

.. todo::

   Constraint Requirements - in the sense of known limitations or constraints

     - [e.g. The SouP item shall only be used in single-threaded context;
       concurrent calls are prohibited]
     - [Known upstream limitation — reference anomaly or documentation]

Anomaly Evaluation
==================

.. note::

   This section is required for Category B SouP items.
   For Category A items, mark this section **N/A** and state the reason.

.. todo::

   Review the vendor release notes, upstream issue tracker, and public
   vulnerability databases (NIST NVD, CVE) for [SouP Item Name] version
   [Version]. Record every anomaly identified and document your relevance
   decision and disposition. If no anomalies are found, retain the
   statement below and document the sources checked.

Anomaly Search Coverage
-----------------------

.. list-table:: Sources Checked
   :header-rows: 1
   :widths: 40 30 30

   * - Source
     - Coverage (versions / date range)
     - Date Checked
   * - Vendor release notes / changelog
     - [Version range checked]
     - [YYYY-MM-DD]
   * - NIST NVD (CVE database)
     - [Query used, e.g. "cpe:/a:vendor:product"]
     - [YYYY-MM-DD]
   * - Upstream issue tracker
     - [URL, label / milestone filter]
     - [YYYY-MM-DD]

No safety-relevant anomalies identified.

.. Uncomment and complete the table below if anomalies were found:
..
.. .. list-table:: Anomaly Evaluation
..    :header-rows: 1
..    :widths: 12 28 13 12 25 10
..
..    * - Anomaly ID
..      - Description
..      - Severity (Critical / Major / Minor)
..      - Relevant? (Yes / No)
..      - Disposition
..      - Status
..    * - [CVE-XXXX-XXXX / vendor ref]
..      - [Brief description of the defect or vulnerability]
..      - [Critical / Major / Minor]
..      - [Yes / No — rationale]
..      - [Version upgrade / Architectural mitigation / Accepted with rationale]
..      - [Open / Closed]

Integration Verification
========================

.. note::

   This section is required for Category B SouP items.
   For Category A items, mark this section **N/A** and state the reason.

.. todo::

   Define and execute integration verification test cases that demonstrate
   [SouP Item Name] satisfies the requirements in the "SouP Item
   Requirements" section. Reference the requirement ID(s) each test case
   covers. Add rows as needed.


**Integration Verification Conclusion:**



Risk Control Measures
=====================

.. note::

   This section is required for Category B SouP items.
   For Category A items, mark this section **N/A** and state the reason.


.. todo::


   - Do a FMEA
   - Derive mitigation requirements from FMEA

.. todo::

    Identify any residual risks associated with [SouP Item Name] and
    document the risk control measures applied. Confirm that residual risk
    is acceptable per the product's risk management file (ISO 14971).
    If no additional risk control measures are required beyond those already
    captured in the anomaly evaluation and integration verification, state
    this explicitly.

**Residual risk acceptance confirmed by QA/RA:** [Yes / No — see Acceptance
Decision section]

Acceptance Decision
===================

.. todo::

   Record the final acceptance decision. Replace the placeholder text,
   state any conditions or restrictions on use, and obtain signatures
   from the Tester, Reviewer, and QA Approver before releasing this record.

[SouP Item Name] version [Version] is **accepted** / **rejected** for integration
into **MyProject** for the purpose of [intended use].

**Conditions / restrictions** (if any):

- [List any restrictions, e.g. "only to be used within the validated operational
  envelope as defined in CR-01", "must be updated if a new critical CVE is
  published before next release", etc.]
- If no conditions apply, write: None.


Re-evaluation Criteria
=======================

.. todo::

   Review the default re-evaluation triggers listed below. Add or adjust
   project-specific triggers if required by MyProject's risk profile or
   regulatory context.

This SouP evaluation is valid until one of the following re-evaluation triggers
occurs, as defined in :ref:`sop-soupval`:

- The SouP item is updated to a new version.
- The SouP item is used in a new architectural context or for a new purpose not
  covered by this report.
- The target operating environment changes significantly (OS upgrade, hardware
  change, new compiler version, new container base image, etc.).
- A new anomaly or CVE is published that may be relevant to the intended use.
- A change to the product's hazard analysis or intended use changes the safety
  category or residual risk assessment for this SouP item.
- An annual review determines that re-evaluation is warranted.

Upon any trigger, a new or amended SouP Evaluation Report shall be produced and
approved before the SouP item is returned to use.
