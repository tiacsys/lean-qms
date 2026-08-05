.. _sop-soupval:

SOP-Software of Unknown Provenance Validation Procedure
********************************************************

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

Overview
--------

Software of Unknown Provenance (SouP) is any pre-existing software component —
including open-source libraries, third-party packages, frameworks, and runtime
environments — that is incorporated into a medical device software product
without the manufacturer having full visibility of its development history,
design rationale, or internal quality controls.

Because the development process of SouP cannot be re-enacted, IEC 62304 requires
that the manufacturer instead establish objective evidence that the SouP item
performs as needed for its intended use and that its known limitations and anomalies
are evaluated for impact on patient safety.

This :term:`SOP` establishes a risk-based, structured procedure for the identification,
evaluation, integration verification, and ongoing monitoring of :term:`SouP` items
used in Class B medical device software products.

Purpose
-------

This :term:`SOP` defines:

* How SouP items are identified and recorded in the project SouP Register.
* How each SouP item is classified by risk category (Category A or B) based on
  its potential contribution to hazardous situations.
* What evaluation and verification activities are required per category.
* How known anomalies are assessed and dispositioned.
* The conditions under which re-evaluation is required.
* What records must be retained as objective evidence.

Scope
-----

This procedure applies to all SouP items incorporated into Class B medical device
software products, including but not limited to:

* Open-source libraries (e.g., communication stacks, numeric libraries, UI frameworks)
* Third-party closed-source packages and SDKs
* Operating system components and runtime environments (e.g., RTOS, language runtimes)
* Firmware and hardware abstraction layers supplied by component vendors
* Pre-compiled binaries for which source code is unavailable

This procedure applies to all software safety classes but the required depth of
evaluation scales with the SouP item's safety impact, as defined below.  For
Class B software, all SouP items that could contribute to a hazardous situation
require the full evaluation defined in this SOP.

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. git_changelog ::
  :filename_filter: docs/sop/sop-soupval/sop-soupval.rst

References
----------

Requirements of standards this SOP implements or complies with:

- IEC 62304:2006 + A1:2015 — Medical device software — Software life cycle processes

  - Clause 5.3.3 — Requires identification of SOUP items in the software architectural design.
  - Clause 5.3.6 — Requires specification of functional and performance requirements for
    each SOUP item.
  - Clause 7.1.2 — Requires identification of SOUP items that could contribute
    to a hazardous situation as part of software risk management.
  - Clause 7.1.3 — Requires evaluation of published anomalies in SOUP items for
    their relevance to safety.
  - Clause 5.7 — Requires system testing to verify integration of SOUP items.
  - Clause 8.1.2 — Requires configuration identification of SOUP versions.

- ISO 14971:2019 — Medical devices — Application of risk management to medical devices

  Provides the risk management framework referenced by IEC 62304 clause 7 for
  hazard identification and risk estimation related to SouP items.

- FDA Guidance — *Cybersecurity in Medical Devices* (2023)

  Provides expectations for monitoring and addressing known vulnerabilities
  (CVEs) in third-party and open-source software components.

Applied SOPs

- SOP-DOCCTL :ref:`sop-docctl:sop-docctl` — Each SOP is a controlled document, and so
  does the management of this SOP.

- SOP-SwDP :ref:`sop-swdp:sop-swdp` — The Software Development Procedure governs
  overall software planning, within which SouP identification and evaluation
  planning takes place.

- SOP-TOOLVAL :ref:`sop-toolval:sop-toolval` — Applied in parallel for any SouP item
  that is also used as a development tool.

Document Content
================

Roles
-----

.. list-table::
   :header-rows: 1

   * - Role
     - Responsibility
   * - Software Engineer
     - | Identify SouP items used in the software architecture
       | Execute integration verification test cases
       | Document evaluation evidence in the SouP Evaluation Report
   * - Software Lead / Architect
     - | Classify each SouP item (Category A or B)
       | Define evaluation scope and acceptance criteria
       | Trigger re-evaluation when the SouP item or environment changes
   * - Reviewer
     - | Independently review SouP Evaluation Reports for completeness
       | Verify that acceptance criteria are met and anomalies are dispositioned
   * - QA/RA
     - | Approve completed SouP Evaluation Reports
       | Maintain the SouP Register
       | Trigger periodic re-evaluation reviews

SouP Safety Category Scheme
----------------------------

Each SouP item shall be classified as Category A or Category B based on whether
it could contribute to a hazardous situation in the context of the medical device's
intended use.  The determination shall be made by the Software Lead in consultation
with the risk management team.

.. list-table:: SouP Safety Category Decision Criteria
   :header-rows: 1

   * - | Does the SouP item process, transform,
       | or display data that could affect
       | patient safety or clinical decision-making?
     - | Could a failure or incorrect
       | behavior the of the SouP item
       | contribute to a hazardous situation
       | (as defined by ISO 14971)?
     - | Resulting
       | Safety Category
   * - No
     - No
     - | **A** —
       | Reduced
       | evaluation
   * - | Yes, but a downstream software layer
       | independently verifies correctness
       | before it affects a safety-relevant output
     - | Marginal — risk is adequately
       | controlled by the
       | architectural control
     - | **A** —
       | Document the
       | architectural
       | control
   * - Yes
     - Yes
     - | **B** —
       | Full evaluation
       | required

**Category A — No or negligible safety contribution.**
The SouP item does not process safety-relevant data and cannot contribute to a
hazardous situation.  A failure would be detected and corrected before it could
affect a clinical or safety outcome.
Evaluation requirement: identification and version recording in the SouP Register;
brief justification for Category A assignment.

**Category B — Safety-relevant.**
The SouP item processes, transforms, or displays data that could contribute to a
hazardous situation if the item malfunctions.  Class B software requires full
evaluation per Steps 1–7 below.
Evaluation requirement: full SouP Evaluation Report using template
:ref:`tpl_soupval`.

.. note::

   When the safety category is uncertain, Category B shall be assigned.
   Reclassification from B to A requires documented rationale approved by QA/RA.

Procedure
---------

Step 1 — SouP Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the start of each project (or project phase), all SouP items incorporated into
the software architecture shall be identified.  Each SouP item shall be recorded
in the project **SouP Register** with the following information:

* SouP item name and type (library, framework, OS component, SDK, etc.)
* Vendor or upstream project name and URL
* Exact version in use (version string, commit hash, or package hash as applicable)
* Intended purpose and location within the software architecture
* License type and any relevant license obligations
* Responsible engineer

The SouP Register shall be kept under version control and updated whenever a SouP
item is added, removed, or updated.  For projects using a package manager, the
lock file (e.g., ``requirements.txt``, ``Cargo.lock``, ``package-lock.json``) may
serve as the version-pinning record and shall be referenced from the SouP Register.

Objective evidence:

* SouP Register entry with name, vendor, version, architecture location, license,
  and responsible engineer

IEC 62304 compliance:

* Clause 5.3.3, Clause 8.1.2

Step 2 — Safety Category Assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each SouP item in the SouP Register, the Software Lead shall assign a safety
category (A or B) using the scheme defined above.

The category assignment and its rationale shall be documented in the SouP Register
or in the SouP Evaluation Report.  The assessment shall be based on the SouP item's
role in the software architecture and the product's hazard analysis (ISO 14971).

When in doubt, Category B shall be assigned.

Objective evidence:

* Safety category assignment and rationale recorded in the SouP Register

IEC 62304 compliance:

* Clause 7.1.2

Step 3 — Requirements Specification for SouP Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each Category B SouP item, the following shall be documented in the SouP
Evaluation Report:

* **Functional requirements:** what the SouP item must do within the software
  architecture (e.g., parse protocol messages, compute numerical results, manage
  memory).
* **Performance requirements:** timing, throughput, or resource constraints the
  SouP item must satisfy.
* **Interface requirements:** the API surface, data formats, and communication
  protocols through which the SouP item is accessed.
* **Constraint requirements:** known limitations, prohibited configurations, or
  conditions of use that must be respected to maintain safety.

These requirements form the basis for the integration verification test cases
defined in Step 5.

Objective evidence:

* SouP item requirements section in the SouP Evaluation Report

IEC 62304 compliance:

* Clause 5.3.6

Step 4 — Anomaly Evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each Category B SouP item, all published and known anomalies shall be evaluated
for their relevance to the item's intended use in this product.  The evaluation
shall cover:

* Vendor release notes, errata, and known-issues lists for the version in use and
  all versions between the previous evaluation and the current version.
* Public vulnerability databases (e.g., NIST NVD, CVE listings) for security
  vulnerabilities in the SouP item.
* Upstream issue trackers for relevant open defects.

For each anomaly identified, the following shall be documented:

* Anomaly identifier (e.g., CVE number, upstream issue reference, vendor errata ID)
* Brief description
* Severity assessment:

  * **Critical** — the anomaly could directly contribute to a hazardous situation
    in this product's intended use.
  * **Major** — the anomaly could indirectly contribute to a hazardous situation
    or significantly degrade system reliability.
  * **Minor** — the anomaly has no plausible path to a hazardous situation in
    this product's intended use.

* Relevance decision: relevant or not relevant, with rationale
* Disposition for relevant anomalies:

  * Corrected by updating to a version where the anomaly is fixed (triggers
    re-evaluation per the Re-evaluation Triggers section)
  * Mitigated by an architectural control (document the control measure)
  * Accepted with formal written risk justification reviewed by QA/RA

Critical anomalies shall block approval of the SouP item until they are resolved
or formally accepted with documented rationale approved by QA/RA.

Objective evidence:

* Anomaly Evaluation section in the SouP Evaluation Report

IEC 62304 compliance:

* Clause 7.1.2, Clause 7.1.3

Step 5 — Integration Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each Category B SouP item, integration verification test cases shall be
defined and executed to confirm that the SouP item:

* Satisfies the functional, performance, interface, and constraint requirements
  specified in Step 3.
* Behaves correctly within the target hardware and software environment.
* Does not introduce unacceptable interactions with other software components.

Test cases shall follow the same structure as the project's software integration
test specifications (see :ref:`sop-swdp:sop-swdp`).  At minimum, the following
shall be verified:

* The SouP item initialises correctly in the target environment.
* Each functional requirement is exercised with known inputs and the output is
  compared against the defined expected result.
* Boundary conditions and error-handling paths relevant to safety are tested.
* Resource consumption (memory, CPU, timing) is within the specified constraints.

All test cases must pass for the integration verification to be accepted.  Any
deviation shall be logged as a SouP Anomaly and handled per Step 4 before the
integration may be approved.

Objective evidence:

* Integration Verification section (test specifications and execution records)
  in the SouP Evaluation Report

IEC 62304 compliance:

* Clause 5.7

Step 6 — Risk Control Measures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each Category B SouP item, the residual risks associated with the item shall
be evaluated against the product's risk acceptability criteria (ISO 14971).

Where risks are not already acceptable or are controlled by architectural controls
identified in Step 4:

* Additional risk control measures shall be defined (e.g., input validation,
  watchdog monitoring, output plausibility checks, use of the SouP item only
  within a tested operational envelope).
* The effectiveness of each risk control measure shall be verified as part of the
  integration verification (Step 5) or the system-level risk management activities.

Residual risk acceptance shall be documented in the SouP Evaluation Report and
confirmed by QA/RA.

Objective evidence:

* Risk Control Measures section in the SouP Evaluation Report
* Reference to the product's risk management file (ISO 14971)

IEC 62304 compliance:

* Clause 7.1.2, Clause 7.1.3

Step 7 — Approval and Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upon completion of all required evaluation activities (Steps 3–6) and disposition
of all anomalies, the SouP Evaluation Report shall be:

1. Independently reviewed by the Reviewer for completeness and correctness.
2. Approved by QA/RA.

Upon approval:

* The SouP item is registered as evaluated and accepted at the specified version
  in the SouP Register.
* The approved SouP Evaluation Report is stored as a controlled document under
  version control.
* The SouP item may be used in the software product as described in the evaluated
  scope.

Objective evidence:

* Approved SouP Evaluation Report
* SouP Register updated with evaluated status and approved version

IEC 62304 compliance:

* Clause 5.3.3, Clause 7.1.2

Re-evaluation Triggers
-----------------------

A previously evaluated SouP item shall be re-evaluated when any of the following
conditions occur:

* **Version update:** The SouP item is updated to a new version.  For minor patch
  updates, an impact assessment may suffice if the vendor's release notes confirm
  that no relevant functional changes or new safety-relevant anomalies are
  introduced.
* **Extended use:** The SouP item is used in a new architectural context or for a
  new purpose not covered by the scope of the original evaluation.
* **Environment change:** The target hardware, operating system, compiler, or other
  environmental dependency changes in a way that may affect SouP item behaviour.
* **New anomaly discovered:** A SouP anomaly is discovered (e.g., new CVE published,
  upstream defect reported) that was not evaluated in the original report.
* **Risk profile change:** A change to the product's hazard analysis or intended
  use changes the safety category or residual risk assessment for the SouP item.
* **Periodic review:** An annual review determines that the original evaluation is
  no longer adequate.

The re-evaluation shall follow the same procedure (Steps 1–7) for the affected
activities.  Unchanged activities may be referenced from the previous SouP
Evaluation Report rather than repeated, provided the Software Lead and QA/RA
confirm that those activities remain valid.

Evidence Requirements
---------------------

The following records shall be retained for each evaluated SouP item:

* SouP Register (current and historical versions)
* Safety category assignment and rationale
* SouP item requirements specification (for Category B items)
* Anomaly evaluation records (anomaly list, relevance decisions, dispositions)
* Integration verification test specifications and execution records
* Risk control measures and residual risk acceptance
* Approved SouP Evaluation Report

All records shall be stored in the project repository under version control.

IEC 62304 Clause Mapping
------------------------

.. list-table::
   :header-rows: 1

   * - Activity
     - IEC 62304 Clause
   * - SouP identification and SouP Register
     - 5.3.3, 8.1.2
   * - Safety category assignment
     - 7.1.2
   * - Requirements specification for SouP items
     - 5.3.6
   * - Anomaly evaluation (known defects and CVEs)
     - 7.1.2, 7.1.3
   * - Integration verification testing
     - 5.7
   * - Risk control measures and residual risk
     - 7.1.2, 7.1.3
   * - Approval and registration
     - 5.3.3
   * - Re-evaluation
     - 5.3.3, 7.1.2

Deviations
----------

Any deviation from this procedure shall be documented and approved according to
SOP-DOCCTL :ref:`sop-docctl:sop-docctl`.

.. only:: html

   Appendix
   ========

   Document templates referenced by this SOP:

   .. toctree::
      :maxdepth: 1

      appendix/tpl-soupval

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

   SouP Register
     A controlled document (or section of the Software Bill of Materials) that
     records all SouP items used in a project, together with their version,
     source, intended use, safety category, evaluation status, and known anomalies.

   SouP Safety Category
     The risk-based classification of a SouP item that determines the depth of
     evaluation required:

     * **Category A** — the SouP item cannot contribute to a hazardous situation.
       Reduced evaluation applies.
     * **Category B** — the SouP item could contribute to a hazardous situation.
       Full evaluation per this SOP is required.

   SouP Anomaly
     A defect, erroneous behaviour, or known vulnerability (including CVEs)
     in a SouP item that has been published by the vendor, reported in issue
     trackers, or discovered during integration.

   SouP Evaluation Report
     The controlled record produced for each Category B SouP item that documents
     the evaluation evidence, integration verification results, anomaly
     assessment, and acceptance decision.  Produced using template
     :ref:`tpl_soupval`.

   Integration Verification
     The process of confirming that a SouP item, once integrated into the
     software system, performs its intended function correctly and does not
     introduce unacceptable hazards.

   Re-evaluation
     The repetition of SouP evaluation activities, triggered by a change to
     the SouP item version, its configuration, or the operating environment.
