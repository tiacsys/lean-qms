.. _sop-verif:

SOP-Software — Verification Procedure
****************************************

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

Purpose
-------

This :term:`SOP` defines the software verification activities required by IEC 62304
and related QMS expectations. It complements the Software Implementation SOP and
focuses on verification beyond code review and static analysis, aligning activities
with black-box component testing, HW–SW integration testing, SW–SW integration testing,
and traceability of verification evidence to requirements.

Scope
-----

Applies to verification of software elements that form part of a medical product,
including embedded firmware, test software, and software components integrated
with hardware or other software elements. It is intended for Software Safety Classes
A/B (and extended for Class C where additional evidence is required).

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. git_changelog ::
    :filename_filter: docs/sop/sop-verif/sop-verif.rst

References
----------

- IEC 62304:2006 + A1:2015 - Medical device software — Software life cycle processes
  - Clause 5.5 (Unit verification)
  - Clause 5.6 (Integration and system verification)
- SOP-Software — Software Development Procedure :ref:`sop-swdp:sop-swdp`
- SOP-Software — Implementation Procedure :ref:`sop-impl:sop-impl`
- SOP-Software — Software Tool Validation :ref:`sop-toolval:sop-toolval`

Applied SOPs
------------

- SOP-DOCCTL :ref:`sop-docctl:sop-docctl`
- SOP-SwDP  :ref:`sop-swdp:sop-swdp`
- SOP-Implementation :ref:`sop-impl:sop-impl`

Roles
-----

.. list-table::
   :header-rows: 1

   * - Role
     - Responsibility
   * - Test Engineer
     - Author and execute verification tests, maintain test environments, collect evidence
   * - Software Engineer
     - Provide unit-level verification artifacts, support integration testing
   * - QA/RA
     - Approve test strategies, review evidence, ensure traceability and compliance
   * - Reviewer
     - Independent review of verification plans and results

Procedure
=========

Overview
--------

Verification activities must ensure that requirements are implemented correctly and
that the integrated software/hardware system behaves as intended. Verification shall
provide objective evidence that requirements are satisfied, and that traceability from
requirements to verification artifacts is maintained.

Test Strategy
-------------

- Define verification levels: unit, component (black-box), integration (SW–SW, HW–SW), system
- For each software element, specify the verification method: review, static analysis, unit test,
  black-box test, integration test, system test
- Identify test environments, test data, and pass/fail criteria in the Software Test Plan (SwTP)
- Ensure independence of verification activities where required by IEC 62304 (e.g., independent
  reviewers, separate test execution team)

Unit and Developer Verification
-------------------------------

- Follow SOP-Implementation for unit verification: code review, static analysis, developer unit tests
- Maintain unit test evidence: test specifications, automated test logs, coverage reports
- Unit verification must demonstrate requirement-level verification where units implement
  specific requirements

Black-box Component Testing
---------------------------

- Derive component-level test cases from detailed software requirements (DSwRS) and acceptance criteria
- Execute tests in a component test environment that isolates the component under test and
  exercises its externally visible interfaces
- Capture inputs, outputs, and pass/fail criteria; log results and any anomalies
- For each test case, record links to the requirement IDs it verifies

SW–SW Integration Testing
-------------------------

- Identify integration interfaces and interaction scenarios between software modules
- Define integration test cases that cover normal and fault/error scenarios for inter-module communication
- Execute integration tests in an environment representing the target integration topology
- Track failures, resolutions, and regression tests

HW–SW Integration Testing
-------------------------

- Establish representative hardware testbeds or use hardware-in-the-loop (HIL) setups where applicable
- Verify hardware/software interaction points, timing constraints, and error handling
- Include stress and boundary tests relevant to hardware dependencies

System Verification
-------------------

- Perform system-level tests in an environment representative of the final product configuration
- Validate end-to-end behavior against system and user requirements
- Verify traceability of system test cases to system and software requirements

Traceability
------------

- Maintain requirement ⇄ test case links for all verification activities using the project
  traceability toolchain (sphinx-needs links, reqSuite integration where applicable)
- Ensure each requirement has at least one associated verification artifact and executed test result
- Use automated reports where possible to show coverage and gaps

Test Automation and CI
----------------------

- Automate regressions and unit/component tests in the CI pipeline
- Ensure reproducible test environments (containers, emulators, hardware fixtures)
- Fail CI builds on breaking verification gates as defined in SwDP

Acceptance Criteria and Gates
-----------------------------

- Define acceptance criteria per level in SwTP and SwDP (e.g., pass rates, coverage thresholds)
- Gates (examples):
  - MVP-V&VReady: component tests passed, traceability established
  - ProdReady: system verification passed, no open critical defects

Records
-------

Retain:

- Test plans and procedures
- Executed test cases and results
- Test logs and artifacts (captures, logs, hardware traces)
- Traceability records linking requirements to verification artifacts
- Deviation records and disposition

IEC 62304 Mapping
-----------------

+-----------------------------------------------+--------------------+
| Activity                                      | IEC 62304 Clause   |
+===============================================+====================+
| Unit verification (reviews, unit tests)       | 5.5                |
+-----------------------------------------------+--------------------+
| Integration verification (SW–SW, HW–SW)       | 5.6                |
+-----------------------------------------------+--------------------+
| System verification                           | 6.x (system level) |
+-----------------------------------------------+--------------------+

Deviations
----------

Any deviation from this procedure shall be documented and approved according to
SOP-DOCCTL.


.. note::
   This SOP is a bootstrap template. Tailor test environments, automation and
   traceability practices to project specifics in the SwDP and SwTP.

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

   Verification
     Confirmation by examination and provision of objective evidence that specified requirements
     have been fulfilled.

   Black-box component test
     Verification of a software component against its specified requirements without reference
     to internal implementation.

   HW-SW integration test
     Verification of interactions between hardware and software components in a representative
     environment.

   SW-SW integration test
     Verification of interactions between software components/modules when integrated together.
