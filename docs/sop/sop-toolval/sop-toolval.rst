.. _sop-toolval:

SOP-Software — Tool Validation Procedure
*****************************************

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

Software tools used in the development, verification, and maintenance of medical
device software can introduce undetected errors into the product if they malfunction
or are misconfigured.  Tool validation is the process of establishing objective
evidence that each such tool consistently produces correct output for its intended
use within the development environment.

This :term:`SOP` establishes a risk-based framework for tool validation aligned
with IEC 62304 clause 5.1.2 and the :term:`GAMP` 5 computerised system validation
approach.  The depth of validation required is proportional to the risk the tool
poses to the quality and safety of the medical device software.

Purpose
-------

This :term:`SOP` defines:

* How software tools are identified and recorded.
* How tools are classified by risk (Category 1, 2, or 3).
* What qualification activities (IQ, OQ, PQ) are required per category.
* The conditions under which revalidation is required.
* What records must be retained as objective evidence.

Scope
-----

This procedure applies to all software tools used in the software lifecycle of
medical device software products, including but not limited to:

* Compilers and linkers
* Static analysis tools and linters
* Integrated Development Environments (IDEs)
* Automated test frameworks and test execution tools
* Build systems and continuous integration / continuous delivery (CI/CD) components
* Version control systems
* Documentation generators (e.g., Sphinx, Doxygen)
* Requirement and risk management tools
* Code coverage measurement tools
* Hardware debuggers and firmware programming tools

The procedure applies regardless of Software Safety Class (A, B, or C) as required
by IEC 62304 clause 5.1.2.

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. git_changelog::
  :filename_filter: docs/sop/sop-toolval/sop-toolval.rst

References
----------

Requirements of standards this SOP implements or complies with:

- IEC 62304:2006 + A1:2015 — Medical device software — Software life cycle processes

  Clause 5.1.2 requires that the software development plan identify the software
  tools to be used and, where such tools can have an impact on the safety of the
  medical device, that they be validated before use.

- FDA Guidance — *General Principles of Software Validation* (2002)

  Provides principles for risk-based validation of software tools and computerised
  systems used in the development and manufacture of medical devices.

- IEC TR 80002-2:2017 — *Guidance on the application of ISO 14971 to medical
  device software*

  Provides context for applying risk management principles to tool selection and
  validation decisions.

Applied SOPs

- SOP-DOCCTL :ref:`sop-docctl:sop-docctl` — Each SOP is a controlled document, and so
  does the management of this SOP.

- SOP-SwDP :ref:`sop-swdp:sop-swdp` — The Software Development Procedure governs
  overall software planning, within which tool identification and validation planning
  takes place.

Document Content
================

Roles
-----

.. list-table::
   :header-rows: 1

   * - Role
     - Responsibility
   * - Software Engineer
     - | Identify tools used in the software lifecycle
       | Execute IQ, OQ, and PQ test cases
       | Document test results in the Tool Validation Report
   * - Software Lead / Architect
     - | Classify each tool (Category 1, 2, or 3)
       | Define validation scope and acceptance criteria
       | Trigger revalidation when the tool or environment changes
   * - Reviewer
     - | Independently review validation test specifications and results
       | Verify that acceptance criteria are met and anomalies are dispositioned
   * - QA/RA
     - | Approve completed Tool Validation Reports
       | Maintain the Tool Register
       | Trigger periodic revalidation reviews

Tool Classification Scheme
--------------------------

Tools are classified into three risk categories based on the potential impact of
a tool malfunction on the safety and quality of the medical device software.  The
determining factors are:

* Whether the tool's output is independently verifiable by a downstream process.
* Whether the tool directly produces or modifies a deliverable software artefact.

.. list-table:: Tool Classification Decision Criteria
   :header-rows: 1

   * - Tool role
     - Output independently verifiable?
     - Directly affects deliverable?
     - Category
   * - Text editor, terminal emulator, project management software
     - Yes — human review catches errors
     - No
     - 1
   * - Compiler, static analyser, IDE, linter, build system, documentation generator
     - Yes — output is reviewed or tested by another step
     - Indirectly
     - 2
   * - Automated code generator (sole output, no post-generation review)
     - No
     - Yes
     - 3
   * - Automated test execution framework used as sole verification evidence
     - No — test results are accepted without independent re-execution
     - Yes
     - 3
   * - Automated deployment / firmware programming tool
     - No
     - Yes
     - 3

**Category 1 — No or negligible impact.**
The tool's output is independently verified by a downstream process or human
review such that a tool malfunction would be detected before it could affect the
deliverable.  Examples: text editors, terminal emulators, issue trackers, project
management software.
Validation requirement: identification and version recording only.

**Category 2 — Moderate impact.**
The tool supports development or verification but its output can be verified by
other means (e.g., the compiled binary is subsequently tested; the generated
documentation is reviewed).  Examples: compilers, static analysis tools, IDEs,
linters, build systems, Sphinx documentation generators.
Validation requirement: Operational Qualification (OQ) — functional tests using
known-good inputs and expected outputs.

**Category 3 — High impact.**
The tool directly produces or modifies deliverable software artefacts without an
independent verification opportunity.  Examples: automated code generators (where
generated code is not independently reviewed), automated test execution frameworks
used as the sole evidence of verification, automated deployment or firmware
programming tools.
Validation requirement: full Installation Qualification (IQ) + Operational
Qualification (OQ) + Performance Qualification (PQ).

.. note::

   When the risk category is uncertain, the higher category shall be assigned.
   Reclassification to a lower category requires documented rationale approved
   by QA/RA.

Procedure
---------

Step 1 — Tool Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the start of each project (or project phase), all tools used in the software
lifecycle shall be identified.  Each tool shall be recorded in the project
**Tool Register** with the following information:

* Tool name and vendor
* Version or build number in use
* Intended purpose within the lifecycle (e.g., compilation, static analysis,
  unit test execution)
* Responsible engineer

Tools to be considered include, but are not limited to: compilers, linkers, IDEs,
static analysers, unit test frameworks, CI/CD pipeline components, version control
systems, documentation generators, requirement management tools, code coverage
tools, and hardware debuggers / firmware programmers.

The Tool Register shall be kept under version control and updated whenever a tool
is added, removed, or updated.

Objective evidence:

* Tool Register entry with name, vendor, version, purpose, and responsible engineer

IEC 62304 compliance:

* Clause 5.1.2

Step 2 — Tool Risk Assessment and Classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each tool in the Tool Register, the Software Lead assigns a Category (1, 2,
or 3) using the classification scheme defined above.

The classification rationale shall be documented in the Tool Register or in the
Tool Validation Report.  Where a tool's category is not immediately obvious, the
Software Lead shall consult with QA/RA before assigning the category.

When in doubt, the higher category shall be assigned.

Objective evidence:

* Category assignment and rationale recorded in the Tool Register

IEC 62304 compliance:

* Clause 5.1.2

Step 3 — Validation Planning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each tool, the required validation activities shall be planned according to
its category:

* **Category 1:** No further validation steps required beyond registration.
* **Category 2:** Author OQ test cases that exercise the tool's relevant functions
  with known-good inputs and defined expected outputs.  Define acceptance criteria
  (e.g., "actual output matches expected output for all test cases").
* **Category 3:** Author IQ, OQ, and PQ test specifications.

  * IQ: verifies correct installation (version, dependencies, licence, and
    CI/CD accessibility).
  * OQ: verifies functional correctness with known-good inputs.
  * PQ: verifies correct behaviour under production-representative conditions.

The validation plan, test specifications, and acceptance criteria shall be
documented in the **Tool Validation Report** (template ``tpl-toolval``).

Objective evidence:

* Tool Validation Report containing the validation plan and test specifications

IEC 62304 compliance:

* Clause 5.1.2

Step 4 — Installation Qualification (IQ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applies to Category 3 tools.  May optionally be applied to Category 2 tools where
installation errors are identified as a concern during planning.

The IQ shall verify:

* The tool is installed at the correct, registered version.
* All dependencies are present at the correct versions.
* The software licence is valid and covers the intended use.
* The tool is accessible within the CI/CD environment used for development and
  verification.

The IQ result (pass / fail) shall be recorded in the Tool Validation Report,
including the tester identity, execution date, and environment details.

.. attention::

   An IQ failure shall block further qualification stages until the installation
   issue is resolved and the IQ is re-executed and passes.

Objective evidence:

* IQ execution records in the Tool Validation Report

IEC 62304 compliance:

* Clause 5.1.2

Step 5 — Operational Qualification (OQ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applies to Category 2 and Category 3 tools.

Each OQ test case shall be executed by following the test procedure; the actual
output shall be compared against the defined expected output; and a pass or fail
result shall be recorded per test case.

All OQ test cases must pass for the OQ stage to be considered accepted.  Any
deviation between actual and expected output shall be logged as a Tool Anomaly
and handled per Step 7 before the OQ stage may be closed.

Objective evidence:

* OQ test execution records (per-test-case actual output, pass/fail, tester,
  date) in the Tool Validation Report

IEC 62304 compliance:

* Clause 5.1.2

Step 6 — Performance Qualification (PQ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applies to Category 3 tools only.

PQ test cases shall simulate realistic production workloads or scenarios
representative of the tool's actual use.  Examples:

* Running the automated test framework on the full production test suite and
  verifying that pass/fail results are reproducible and match manual expectations.
* Executing the code generator on representative input models and verifying the
  generated artefacts against reference outputs.
* Running the deployment tool against a representative target configuration and
  verifying the deployed artefact matches expectations.

Tool performance (e.g., execution time) and output quality shall be acceptable
under production-representative conditions.  Acceptance criteria for PQ shall be
defined during planning (Step 3).

The PQ result shall be recorded in the Tool Validation Report.

Objective evidence:

* PQ test execution records in the Tool Validation Report

IEC 62304 compliance:

* Clause 5.1.2

Step 7 — Anomaly Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any unexpected or incorrect tool behaviour observed during validation or production
use shall be logged as a **Tool Anomaly**.  For each anomaly the following shall
be documented:

* Description of the observed behaviour
* Severity assessment:

  * **Critical** — the tool cannot be used safely; there is a risk of undetected
    errors in deliverables.
  * **Major** — significant deviation; a workaround is possible but must be
    documented.
  * **Minor** — low-risk deviation with negligible impact on deliverable quality.

* Root-cause investigation result
* Disposition:

  * Corrected by vendor update (triggers revalidation per the Revalidation
    Triggers section below)
  * Worked around with a documented procedure
  * Accepted with formal written justification

Critical anomalies shall block approval of the tool until they are resolved or
formally accepted with documented rationale approved by QA/RA.

Anomalies and their dispositions shall be recorded in the Tool Validation Report.

.. note::

   Tool anomalies discovered during production use (after validation is complete)
   shall be recorded in the Tool Anomaly log and assessed for impact on previously
   accepted deliverables.  If an impact is identified, affected work products shall
   be reviewed and re-verified as necessary.

Objective evidence:

* Tool Anomaly log and disposition records in the Tool Validation Report

IEC 62304 compliance:

* Clause 9.x (problem resolution process)

Step 8 — Approval and Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upon completion of all required qualification stages (IQ / OQ / PQ as applicable)
and disposition of all anomalies, the Tool Validation Report shall be:

1. Independently reviewed by the Reviewer for completeness and correctness.
2. Approved by QA/RA.

Upon approval:

* The tool is registered as validated at the specified version in the Tool Register.
* The approved Tool Validation Report is stored as a controlled document under
  version control.
* The tool may be used in the software lifecycle as specified in the validated scope.

Objective evidence:

* Approved Tool Validation Report
* Tool Register updated with validated status and approved version

IEC 62304 compliance:

* Clause 5.1.2

Revalidation Triggers
---------------------

A previously validated tool shall be revalidated when any of the following
conditions occur:

* **Version update:** The tool is updated to a new major or minor version.
  For minor patch or bugfix updates, an impact assessment may suffice if the
  vendor's release notes confirm no relevant functional changes affecting the
  validated use.
* **Extended use:** The tool is used for a new purpose or in a new context not
  covered by the scope of the original validation.
* **Environment change:** The operating system, CI/CD platform, hardware, or
  other environmental dependency changes in a way that may affect tool behaviour.
* **Production anomaly:** A Tool Anomaly is discovered in production use that was
  not detected during the original validation.
* **Periodic review:** An annual review determines that the original validation is
  no longer adequate (e.g., due to changes in regulatory expectations or project
  risk profile).

The revalidation shall be planned and executed following the same procedure
(Steps 1–8) for the affected qualification stages.  Unchanged qualification
stages may be referenced from the previous Tool Validation Report rather than
repeated, provided the Software Lead and QA/RA confirm that the unchanged stages
remain valid.

Evidence Requirements
---------------------

The following records shall be retained for each validated tool:

* Tool Register (current and historical versions)
* Tool classification rationale
* Validation plans — IQ, OQ, and PQ test specifications as applicable
* Test execution records — actual results, tester identity, and execution date
* Tool Anomaly log and disposition records
* Approved Tool Validation Report

All records shall be stored in the project repository under version control.

IEC 62304 Clause Mapping
------------------------

.. list-table::
   :header-rows: 1

   * - Activity
     - IEC 62304 Clause
   * - Tool identification and planning
     - 5.1.2
   * - Tool classification and risk assessment
     - 5.1.2 / ISO 14971 risk management principles
   * - IQ/OQ/PQ execution and documentation
     - 5.1.2 (validation obligation)
   * - Anomaly management and problem resolution
     - 9.x (problem resolution process)
   * - Revalidation
     - 5.1.2

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

      appendix/tpl-toolval

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

   Software Tool
     Any software used to support the development, maintenance, or verification of
     medical device software, including compilers, analysers, test frameworks,
     build systems, and documentation generators.

   Tool Validation
     The process of establishing objective evidence that a software tool consistently
     produces correct output when used for its intended purpose in the target
     development environment.

   Tool Classification
     The risk-based categorisation of a software tool into Category 1, 2, or 3,
     which determines the depth of validation required.

   Installation Qualification (IQ)
     Verification that a software tool is installed correctly in the target
     environment at the expected version, with all required dependencies and
     licences present.

   Operational Qualification (OQ)
     Verification that a software tool operates as specified across its intended
     operating range, using known-good inputs and expected outputs.

   Performance Qualification (PQ)
     Verification that a software tool consistently performs as intended under
     conditions representative of actual production use.

   Revalidation
     Repeated validation of a software tool, triggered by a change to the tool
     version, its configuration, or the operating environment.

   Tool Anomaly
     Any unexpected or incorrect behaviour observed during tool validation or
     operational use that deviates from the expected or documented behaviour of
     the tool.

   GAMP
     Good Automated Manufacturing Practice — an industry framework for
     computerised system validation, originally developed for the pharmaceutical
     industry and widely applied to the qualification of software tools used in
     medical device development.
