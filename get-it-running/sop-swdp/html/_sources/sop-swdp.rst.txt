.. _sop-swdp:

SOP-Software — Software Development Procedure
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

This :term:`SOP` defines procedures for software development of medical products.
The procedure addresses the part of
- Software requirement solicitation
- Software design
- Software implementation

Other mandatory requirements of ISO 62304 like

- Software verification
- Software risk management
- Software tool validation
- :term:`SouP` validation
- Software configuration management

are addressed in other SOP.

The cyclic, iterative process that governs how requirements and design
artefacts are elicited, structured, traced, and refined throughout all
phases is defined in :ref:`sop-req_design:sop-req_design`.


Purpose
-------

This procedure defines general proceduces for firmware and related
software products of medical products in compliance with IEC 62304.

.. note::
  This SOP is **not** a software development plan.

  Thus, every software development plan is specific for project it is written
  for. It is intended that every project enforces the application of this
  :term:`SOP`. and will also tailor the general procedures to the project

  A template of this :doc:`/appendix/tpl-swdp`, is provided.

Scope
-----

This :term:`SOP` should be appled to the software development of

- Embedded firmware
- Safety-related software tools
- Test software
- Internal libraries

that is **intended to be part of a medical product**.


Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. git_changelog ::
  :filename_filter: docs/sop/sop-swdp/sop-swdp.rst


References
----------

- `Twin Peak Model <https://t2informatik.de/en/smartpedia/classification-peaks-model/?noredirect=en-US>`_


Requirements of standards this SOP implements or complies with:

- IEC 62304:2006 + A1:2015 - Medical device software — Software life cycle processes
  - Clause 4.1 - Quality Management System


Applied SOP's

- SOP-DOCCTL :ref:`sop-docctl:sop-docctl` - Each SOP is a controlled document, and so does
  the management of this SOP.
- SOP-REQ-DESIGN :ref:`sop-req_design:sop-req_design` - Defines the artefact model,
  field conventions, traceability links, and the cyclic requirements-and-design
  process (Phases 1–6) applied in the Planning and Develop phases below.

Document Content
================

Roles
-----

.. list-table::
   :header-rows: 1

   * - Role
     - Responsibility
   * - Product Owner
     - Defines needs and priorities
   * - System Engineer
     - Defines system requirements
   * - Software Engineer
     - Design + implementation
   * - Reviewer
     - Independent review
   * - QA/RA
     - Process compliance

Lifecycle Activities
--------------------

Overview
~~~~~~~~

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 1 3 2 1


   * - Phase
     - Activities
     - Delivered Artifacts
     - Gate
   * - Planning
     - | Plan Software activities
       | - Establish development organization
       | - Define development approach
       | - Define verification
       | - Determine risk class
       | - Define config management
       | - Define tooling
       | - Establish drafts
     - | :term:`SwDP`
       | preliminary :term:`SwRS`
       | preliminary :term:`SwDS`
     - DevStart
   * - | Develop
       | and
       | (Software)
       | Verify
     - | - Iterative update req, design
       | - Iterative detailed design,
       |   risk assessment, detailed req
       | - Justify risk class
       | - Iterative testplan, cases
       | - Establishment of development,
       |   including CI, review,
       |   static analysis, coverage
       | - Tool validation
       | - SouP validation
     - | Updated :term:`SwDP`,
       | :term:`SwRS`, :term:`DSwRS`
       | :term:`DSwDS`, :term:`DSwDS`
       | All tool validations
       | All :term:`SouP` validations
       | :term:`SwTP`, :term:`SwTR`, :term:`SwRN`
     - MVP-V&VReady
   * - | Prod & Comfort
       | Software
       | Development
     - | - Iterative Requirements and
       |   design of comfort features
       | - Implementation and test of
       |   comfort features
       | - Iterative testplan, cases updtes
       | - PCB production FCT - test software
       |   development
       | - PCB - factory deployment software
       | - Bugfixing of V&V system test findings
     - | :term:`SwDP`, :term:`DSwDS`
       | :term:`SwRS`, :term:`DSwRS`
       | FCT SW released
       | Factory deployment
       | software released
       | :term:`SwTP`, :term:`SwTR`, :term:`SwRN`
     - ProdReady
   * - Maintenance
     - | - Market Monitoring for incidents
       | - SouP monitoring for :term:`CVE`
       | - :term:`CAPA` process
     - | New releases
       | that fix
       | incidents or CVE
     - ProdReady


Planning Phase
~~~~~~~~~~~~~~

The planning phase determines essential prerequisites for effective
development of medical software.


Activity - Establish SwDP
^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer, Product Owner

Guidance:
  - Use the :doc:`/appendix/tpl-swdp` Template, that includes guidance
  - Extensions or overwrites is possible, should be discussed with QMS team,
    in order to not violate regulatory needs dictetated by standards

Result, Provided Evidence:
   - Reviewed and approved :term:`SwDP` in QMS


Activity - Establish  Development Team
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer, Product Owner, QA

Guidance
  All persons and their roles have to be named in the :term:`SwDP`

Result, Provided Evidence:
  All persons are aware of applicable :term:`SOP` 's, and understand their
  roles and responsibilities.

  All persons confirmed by filling in :ref:`qms-overview:tpl-qms-comply` template and
  checking in project qms-git


Activity - Preliminary Software Requirement Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer, Product Owner, System Engineer

Guidance
  - Prerequisite are
    - Established User Needs
    - Established top-level system requirements (with traces to user needs)
    - preliminary system design
  - Use the :doc:`/appendix/tpl-swrs` Template
  - Follow :ref:`sop-req_design:sop-req_design` for ``req`` artefact
    conventions: mandatory ``level`` and ``id`` fields, ``concerns`` for
    safety/cybersecurity items, and ``derives`` links to parent needs or
    system requirements.

Result, Provided Evidence:
   - Reviewed and approved :term:`SwRS`
   - in QMS


Activity - Preliminary Software Design Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer, Product Owner, System Engineer

Guidance
  - Prerequisite are
    - Preliminary system design
    - Preliminary :term:`SwRS`
  - Use the :doc:`/appendix/tpl-swds` Template
    - Context diagram is expected
    - Software architecture styles are expected
    - Optionally 1st Level Component Breakdown
  - Follow :ref:`sop-req_design:sop-req_design` for ``spec`` artefact
    conventions: mandatory ``level`` and ``id`` fields, ``implements`` links
    to the requirements being realised, and ``concerns`` for safety-relevant
    design decisions.

Result, Provided Evidence:
   - Reviewed and approved :term:`SwDS`
   - in QMS


Develop and Software Verify Phase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Twin Peak model for software requirements, design and risk assessment.

The following activities are expected to be performed **iteratively**, and in parallel,
according to the twin peak model for software requirements and design
extended by the software risk assessment, as formalised in
:ref:`sop-req_design:sop-req_design` (Phases 2–5).

- Detailed Software Requirement Specification
- Detailed Software Design Specification
- Software Risk Assessment

.. note :: The iteration ends when all the following conditions are met:

  - All software requirements are traced to system requirements,
    or are traced to user needs
    or are traced to risk control measures
  - All detailed software requirements are traced to software requirements
    or are traced to software design elements,
    or are traced to risk control measures
  - All detailedsoftware design elements are traced to software design elements
  - or are traced to (detailed) software requirements
  - All software hazards are identified, and have risk control measures or are accepted
  - The software risk class is justified and accepted

.. note :: This SOP is necessary for **Class B** software development.

  It is not sufficient for **Class C** software development,
  where additional activities are expected, like formal verification, formal methods,
  more detailed design, more tests, more documentation more reviews,
  more stringent :term:`SouP` validation,
  more stringent tool validation, more stringent requirements for software
  configuration management, and software maintenance.


Activity - Detailed Software Requirement Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer, Product Owner, System Engineer

Guidance
  - Prerequisite are
    - Preliminary system design
    - Preliminary :term:`SwRS`
    - Preliminary :term:`SwDS`
  - Extend the preliminary :term:`SwRS` to a detailed :term:`DSwRS`, i.e. establish a new version
  - Follow :ref:`sop-req_design:sop-req_design` for ``req`` artefact
    conventions: mandatory ``level`` and ``id`` fields, ``concerns`` for
    safety/cybersecurity items, ``derives`` links to parent needs or system
    requirements, and ``verifies`` links from test cases.

Result, Provided Evidence:
   - Reviewed and approved updated version :term:`SwRS` and :term:`DSwRS`
   - All detailed software requirements are traced to software design elements or are traced to software requirements
   - All software requirements are traced to system requirements, or are traced to user needs or are traced to risk control measures


.. note:: Requirements in General

    Requirements shall be:

    - uniquely identified
    - testable
    - version controlled
    - traceable


.. note:: Traceability of requirements

    The traceability of requirements is a key aspect of the software development
    process, as it ensures that all requirements are properly implemented and
    verified. It also helps to identify any gaps or inconsistencies in the
    requirements, and to ensure that all requirements are properly tested.

    Traceability is assured by a sphinx-needs tool that allows to link requirements
    to needs, risk mitigation measures,
    design elements, test cases, and other.

.. note:: Storage of requirements

    Requirements are stored in sphinx-needs and reqSuite requirement management tools.
    sphinx-needs integrates smoothly into to software development processes, whereby
    reqSuite is more suitable for complex complete projects that cross more engineering domains.

    The leading system is reqSuite. sphinx-needs imports items from reqSuite at certain baselines.
    (milestones) ReqSuite does not import items from sphinx-needs. Thus,
    detailed software requirements, software design, software test cases and software test
    result are stored in sphinx-needs, whereas software requirements are stored in reqSuite.

    Traceability is assured by linking items in sphinx-needs to items in reqSuite,
    and by linking items in sphinx-needs to each other.


Activity - Detailed Software Design Specification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer, Software Architect

Guidance
  - Prerequisite are
    - Preliminary system design
    - Preliminary :term:`SwRS` and :term:`DSwRS`
    - Preliminary :term:`SwDS`
  - Extend the preliminary :term:`SwDS` to a detailed :term:`DSwDS`, i.e. establish a new version
  - Follow :ref:`sop-req_design:sop-req_design` for ``spec`` artefact
    conventions: mandatory ``level`` and ``id`` fields, ``implements`` links
    to the requirements being realised, and ``concerns`` for safety-relevant
    design decisions.

Result, Provided Evidence:
   - Reviewed and approved updated version:term:`SwDS` and :term:`DSwDS`
   - All detailed software design elements are traced to software design elements or are traced to (detailed)software requirements
   - All architectural views are available (structural, behavioral, deployment)
   - All Interfaces and protocols are defined
   - All software modules are defined
   - All SouP are identified


Activity - Software Risk Assessment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer, Product Owner, System Engineer

Guidance
  - Prerequisite are
    - Preliminary system design
    - Preliminary :term:`SwRS`
    - Preliminary :term:`SwDS`
  - For how hazard, risk, and risk-control measure requirements are authored
    as ``hazard``, ``risk``, and ``req`` artefacts with ``concerns: safety``,
    ``mitigates``, and ``causes`` links, follow
    :ref:`sop-req_design:sop-req_design` Phase 3b.

Result, Provided Evidence:
   Reviewed and approved :term:`SwRAR` in QMS, that includes:
   - A :term:`Software Risk Class` justification
   - List of identified :term:`software hazard` s and their :term:`risk control measure` s
   - Optional :term:`FTA` analysis for critical hazardous situations
   - Optional :term:`FMEA`

.. note:: Software Risk Class

     The software risk class is determined by the severity of the harm that
     can be caused by a software failure, and the probability of occurrence
     of such a failure. The software risk class is determined according to
     the rules defined in IEC 62304, and is documented in the risk assessment
     report.


Activity - Tool Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer

Guidance
  Apply :ref:`sop-toolval:sop-toolval` for all software tools that are used in the software development process,
  and that can have an impact on the safety of the medical product.

Result, Provided Evidence:
   Reviewed and approved tool validation reports in QMS for all tools.


Activity - SouP Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer

Guidance
  Apply :ref:`sop-soupval:sop-soupval` for all software tools that are used in the software development process,
  and that can have an impact on the safety of the medical product.

Result, Provided Evidence:
   Reviewed and approved tool validation reports in QMS for all tools.


Activity - Cybersecurity Assessment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer

Guidance
  Apply :ref:`sop-cybersec:sop-cybersec` for all software elements that are used in the software development process,

Result, Provided Evidence:
   Reviewed and approved cybersecurity assessment reports in QMS for all software elements.

   - It shall include a list of all software elements, and their associated CVE,
     if applicable, and the mitigation measures for each CVE.
   - It shall include a thread model for the software, and the associated mitigation measures for each threat.

Activity - Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Responsible:
  Software Engineer

Guidance
  - Apply :ref:`sop-impl:sop-impl` for all software elements

Result, Provided Evidence:
  Reviewed and approved policy for software implementation in QMS, that includes:
  - coding guidelines applied
  - code review process defined
  - code review criteria are defined and applied
  - static analysis tools and rules are defined
  - (developer unit) test coverage criteria are defined
  - static analysis required
  - no direct merge to protected branch

.. note ::

  Developer unit tests are intended to support
  the development process and to ensure a high level of code quality.

  Developer unit tests are tested on target ISA
  (microcontroller or on a representative environment.

  Coverage is expected to be 100% branch coverage for unit tests,

  but documented and accepted coverage exclude annotations are admissible.


Activity - Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only a software element that has been implemented according to the defined
procedures, and has passed the defined verification activities, can be released.

Minimum levels:

- integration tests
- system tests where applicable
- traceability to requirements
- test coverage analysis

Responsible:
  Test Engineer, Software Engineer, Product Owner

Guidance
  - follow the test strategy defined in the :term:`SwDP`
  - apply :ref:`sop-verif:sop-verif` for all software elements

Result, Provided Evidence:
  Reviewed and approved policy for software verification in QMS, that includes:
  - test strategy defined
  - test plan for each software element (including test environments)
  - test cases for each software requirement and detailed software requirement
  - test results for each test case
  - traceability of test cases to requirements


Activity - Release
^^^^^^^^^^^^^^^^^^

A software release is a version of the software that has been implemented
according to the defined procedures, and has passed the defined verification activities.
A software release is intended to **be used outside the development environment**.

Responsible:
  Software Engineer

Guidance
- Prerequisites

  - All software elements have been implemented according to the defined procedures
  - All software elements have passed the defined verification activities
  - All software elements have been reviewed and approved
  - All software elements have been documented in the project repository
  - All software elements have been linked to their respective requirements,
    design elements, and test cases

- Release process

  - Create a release branch from the main branch
  - Update the version number in the software and documentation
  - Generate release notes that include:

    - List of implemented features and changes
    - List of fixed bugs and known issues
    - List of all software elements included in the release,
      with their respective version numbers and links to their documentation

  - Tag the release in the version control system
  - Merge the release branch back to the main branch
  - Create a release notes controlled document from `tpl-sw-rn` template,
  - Publish the release notes and the software release to the appropriate channels



Metrics for Passing of MVP-V&VReady Gate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Documents released:
- SwRS,
- SwDS,
- SwTP,
- SwTR,
- SwRN
- Tool validation reports
- SouP validation reports
- Risk assessment report

Traces:

- All software requirements have associated test cases
- All software requirements have associated design elements
- All software requirements are traced to system requirements,
  or are traced to user needs
  or are traced to risk control measures
- All detailed software requirements are traced to software requirements
  or are traced to software design elements

The automated traceability checks enforced by the Sphinx build (schema
validation and constraint rules) are documented in
:ref:`sop-req_design:sop-req_design` under *Traceability Completeness
Checks*. A passing build is a prerequisite for gate sign-off.

Open defects:

- No open critical or high defects

Software verification:

- all software requirements have associated test cases
- all test cases have been executed with passing results
- test coverage at 100% branch coverage for unit tests
  (documented  and accepted coverage exclude annotations are admissible)
- unit tests performed on target ISA (microcontroller or on a representative environment)


Production Software and Comfort Feature Phase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Production Software is the software that is used to perform FCT testing of the PCB,
and is also used for factory deployment of the software on the PCB.

It is not part of the medical product, but is essential for the production of
the medical product.


Comfort features are software features that are not essential for the safe and
effective use of the medical product.

They are not part of the MVP, but are intended to be added in later releases of
the medical product, after the MVP is released. They do not require any
electronics or hardware changes, but are purely software features.

They improve the user experience, simplify the support and maintenance.


.. todo :: This phase is added later but before V&VReady of the first project

Maintenance Phase
~~~~~~~~~~~~~~~~~

.. todo :: This phase is added later but before ProdReady of the first project

    Address

    - Incindent monitoring,
    - CAPA process,
    - CVE monitoring,
    - and related software updates.

.. only:: html

   Appendix
   ========

   Document templates referenced by this SOP:

   .. toctree::
      :maxdepth: 1

      appendix/tpl-swdp
      appendix/tpl-swrs
      appendix/tpl-swds

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

  SwDP
    Software Development Plan

  SwRN
    Software Release Notes

  SwTP
    Software Test Plan

  SwTR
    Software Test Report
