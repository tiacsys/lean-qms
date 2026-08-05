.. _sop-impl:

SOP-Software — Implementation Procedure
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

This :term:`SOP` defines the process for software implementation and
software unit verification activities during medical device software
development.

The procedure ensures compliance with IEC 62304 software lifecycle
requirements and establishes controls for:

* Software implementation
* Code review
* Static code analysis
* Developer unit testing
* Software coverage assessment
* Software unit acceptance
* Traceability and evidence generation

Scope
-----

This procedure applies to all software developed as part of medical
device software products classified according to IEC 62304.

The procedure applies to Software Safety Classes A, B and C where
required by IEC 62304.

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. git_changelog ::
  :filename_filter: docs/sop/sop-impl/sop-impl.rst


References
----------

Requirements of standards this SOP implements or complies with:

- IEC 62304:2006 + A1:2015 - Medical device software — Software life cycle processes

  Cause 5.1.2  requires the planning of software tools to be used for software development
  and the validation of such tools if they can have an impact on the safety of the medical product.

- SOP-SwDP :ref:`sop-swdp:sop-swdp` - SOP-Software — Software Development Procedure.

Applied SOP's

- SOP-DOCCTL :ref:`sop-docctl:sop-docctl` - Each SOP is a controlled document, and so does
  the management of this SOP.


1. IEC 62304 Mapping
====================

+-------------------------------+--------------------+------------------------------+
| Activity                      | IEC 62304 Clause   | Compliance Method            |
+===============================+====================+==============================+
| Software implementation       | 5.5.1              | Source code implementation   |
+-------------------------------+--------------------+------------------------------+
| Unit verification strategy    | 5.5.2              | Verification procedure       |
+-------------------------------+--------------------+------------------------------+
| Unit acceptance criteria      | 5.5.3              | Acceptance checklist         |
+-------------------------------+--------------------+------------------------------+
| Additional unit acceptance    | 5.5.4              | Static analysis and review   |
| criteria (Class C)            |                    | activities                   |
+-------------------------------+--------------------+------------------------------+
| Unit verification execution   | 5.5.5              | Reviews and tests            |
+-------------------------------+--------------------+------------------------------+


Roles
=====

.. list-table::
   :header-rows: 1

   * - Role
     - Responsibility
   * - Software Engineer
     - | Implement software units
       | Perform unit testing
       | Resolve static analysis findings
       | Participate in peer reviews
       | Maintain traceability of implementation to requirements and design specs
   * - Reviewer
     - | Perform independent code review
       | Verify coding standard compliance
       | Verify implementation against design specifications
       | Document findings
   * - Software Lead Engineer/QA
     - | Oversee software implementation
       | Ensure compliance with development processes
       | Approve unit acceptance criteria

Procedure
=============

Software Unit Implementation
--------------------------------

Each software unit shall be implemented according to:

* Software requirements
* Software architecture
* Detailed design documentation
* Coding standards
* Risk control implementation requirements

Implementation activities shall maintain traceability between:

* Requirement → Design → Source Code → Verification Evidence

Objective Evidence:

* Source code repository history
* Traceability records

IEC 62304 Compliance:

* Clause 5.5.1

Code Review
---------------

Purpose
~~~~~~~

Code review provides verification that software units meet design,
coding, and safety expectations.

IEC 62304 permits software unit verification through review activities
provided verification methods and procedures are defined. Code review
supports software unit verification and acceptance criteria.
IEC 62304 does not prescribe a specific review tool or workflow.


Review Criteria
~~~~~~~~~~~~~~~~

The reviewer shall verify:

* Requirements implemented correctly
* Compliance with coding standard
* Design conformity
* Absence of obvious defects
* Traceability completeness

Reviewer Independence
~~~~~~~~~~~~~~~~~~~~~

The reviewer shall not be the original code author.

Evidence
~~~~~~~~

Review evidence shall include:

* Reviewer identity
* Review date
* Reviewed changeset
* Findings
* Resolution status
* Approval status

IEC 62304 Compliance:

* Clause 5.5.2
* Clause 5.5.3
* Clause 5.5.5

Static Code Analysis
------------------------

Purpose
~~~~~~~

Static analysis supports software unit verification by identifying
potential defects before integration.

Examples:

* Coding standard violations
* Dead code
* Memory issues
* Resource handling issues
* Complexity concerns
* Potential overflow conditions
* Initialization defects

.. note:: Class B software is addressed.

  Class C software may require additional static analysis activities
  and criteria as part of software unit acceptance.


Findings Handling
~~~~~~~~~~~~~~~~~

Static analysis findings shall be:

* Corrected
* Justified
* Formally dispositioned

Evidence
~~~~~~~~

* Analysis report
* Tool output
* Finding resolution records

IEC 62304 Compliance:

* Clause 5.5.2
* Clause 5.5.3

Developer Unit Testing
--------------------------

Purpose
~~~~~~~

Developer unit testing verifies that software units perform according
to allocated requirements and detailed design.

Unit tests shall:

* Execute defined test procedures
* Verify expected outputs
* Include pass/fail criteria
* Document test evidence

Test Considerations
~~~~~~~~~~~~~~~~~~~

Tests should address:

* Normal conditions
* Boundary conditions
* Error handling
* Fault conditions
* Risk control functionality

Where testing is used as verification, test procedures shall be
evaluated for adequacy.

Evidence
~~~~~~~~

* Unit test specification
* Test execution results
* Automated test logs
* Failure investigation records

IEC 62304 Compliance:

* Clause 5.5.2
* Clause 5.5.5

Coverage Assessment
-----------------------

Purpose
~~~~~~~

Coverage measurement provides objective evidence regarding verification
completeness.

IEC 62304 does not mandate specific coverage metrics or thresholds.
Coverage objectives shall therefore be defined within the Software
Development Plan.
Examples:

* Statement coverage
* Branch coverage
* Decision coverage
* MC/DC coverage (where justified)

Coverage gaps shall be:

* Justified
* Risk assessed if applicable
* Approved

Evidence
~~~~~~~~

* Coverage reports
* Coverage justification records

IEC 62304 Compliance:

* Clause 5.5.2
* Clause 5.5.5

Software Unit Acceptance
----------------------------

Prior to integration, software units shall satisfy acceptance criteria.

Acceptance criteria include:

* Static analysis findings resolved
* Code review completed
* Unit tests passed
* Coverage objective achieved

IEC 62304 Compliance:

* Clause 5.5.3

Records
==========

The following records shall be retained:

* Code review reports
* Static analysis reports
* Unit test reports
* Coverage reports
* Traceability evidence


Deviations
=============

Any deviation from this procedure shall be documented and approved
according to the Quality Management System.

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

    Coding Standard
        A set of guidelines and best practices for writing source code, which may include rules for naming conventions, code structure, formatting, and other aspects of code quality.

    Software Unit
        The smallest testable part of a software system that can be independently implemented and verified.

    Software Unit Verification
        The process of evaluating a software unit to determine whether it meets its specified requirements and design specifications.

    Software Unit Acceptance Criteria
        The specific conditions that a software unit must satisfy in order to be considered acceptable for integration into the larger software system.
