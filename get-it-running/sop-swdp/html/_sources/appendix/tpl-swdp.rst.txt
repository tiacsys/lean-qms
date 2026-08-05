:orphan:

.. _tpl-swdp:

MyProject — Software Development Plan
************************************************************

.. Commentary

   Commentary is to guide you turning the document into a project specific plan.
   Commentary is marked as such, and should be removed once the document is
   finalized.

   .. todo::  Must be resolved by project specific content, and this must be removed.

.. todo::

  1. Replace MyProject by your project name everywhere in this document
  2. Replace MyProduct by your product name everywhere in this document

.. todo::

   Setup Inter-Sphinx appropriate linking in conf.py.
   Resolve the *qms* qualifier to the rendered location of QMS publishing


.. doc_control::
   :version: 1.0
   :based_on_template: 001
   :owner: MyProject
   :classification: Plan
   :effective_date: 2026-06-06


.. Note decide about versioning of this document.

   Proposal - allign to milestones
   Use simple enumeration, or alignment to whole doc artifact repository (i.e. sha1 or tag)


.. contents:: Table of Content
   :local:
   :depth: 3

Document Control
================

Overview
--------

.. todo ::

  Change according to your project


  MyProduct is medical product that addresses the following needs

  - need A
  - need B

  MyProduct shall be sold to the followwing markets.

  MyProduct contains Software, that is developed in **MyProject**
  hereafter refered as this project.

  This document is the Software Development Plan (:term:`SwDP`)
  of this project.

Purpose
-------

This plan structures the development activities

- shall lead to a market approved, certified prodoct,
  meets the needs and does not harm users.
- is enforced (produced artifacts are to be reviewed and approved)
  to be followed up
- shall organize the development efficiently

Scope
-----

This document plans all **MyProduct** relevant
software development of **MyProject**.

Relevant means, the software is developed for the perpose of
- ether being part of the product,
- or being part of verification of the product during V&V.



Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. code::

  # does not work straight on github, final solution on azure - resolve it over there
  .. git_changelog ::
	  :filename_filter: docs/qms/MyProjectAbbr-swdp.rst


References
----------

.. add this here if you overwrite a certain procedure of SOP

  Requirements of standards this SOP implements or complies with:

  - IEC 62304:2006 + A1:2015 - Medical device software — Software life cycle processes
    - Clause xyz


Applied SOP's

- SOP-DOCCTL :ref:`sop-docctl:sop-docctl` - This is a controlled document.
- SOP-SWDP :ref:`sop-swdp` - SOP for medical software development
- SOP-TOOLVAL :ref:`sop-toolval:sop-toolval` - SOP for tool validation
- SOP-SOUPVAL :ref:`sop-soupval:sop-soupval` - SOP for software of unknown provenance validation

Definitions
-----------

..

  Add project specific terms here, that are not part of any SOP yet.
  Do as you go.


Add project specific terms here when needed.


Document Content
================

Roles and Role Assignment
--------------------------

.. Define additional roles if needed

  Additional Roles
  ~~~~~~~~~~~~~~~~

  .. list-table::
    :header-rows: 1

    * - Role
      - Responsibility
    * - New Role
      - - Responsibility One
        - Responsibility Two


  Role Assignment
  ~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Role
     - Assigned Person
   * - Product Owner
     - | - Person A
       | - Person B
   * - System Engineer
     - | - Person C
       | - Person D
   * - Software Engineer
     - | - Person E
       | - Person F
   * - Reviewer
     - Any of the above persons, but different to maintain four-eye-principle
   * - QA/RA
     - Person G

.. note system engineer does not show up, since he/she has no stake in software development

Lifecycle Activities
--------------------

Planning Phase
~~~~~~~~~~~~~~

The project executes :ref:`sop-swdp` for software development,
specifically, the planning phase activities.


.. Describe any activities that are specific to your project,
   that are not covered by the SOP, or that need to be highlighted
   for your project.


The expected results and evidences are listed (including the location
where) herafter, ordered by the respective activity.

Development Team - Enablement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The developer QMS training confirmation are recorded in
this repository at the folder ``docs/project-control/records/process-training.``
Each QMS training confirming document is individually submitted by the
individual developer.

Establish SwDP
^^^^^^^^^^^^^^^

The result is this plan document. It shall be located at
``docs/project-control/MyProjectAbbr-swdp.rst``.

Establish SwRS
^^^^^^^^^^^^^^^

The result is a preliminary software requirement specification document.
It shall be located at ``docs/software/swrs/MyProjectAbbr-swrs.rst``.

Establish SwDS
^^^^^^^^^^^^^^^

The result is a preliminary software design specification document.
It shall be located at ``docs/software/swds/MyProjectAbbr-swds.rst``.


Develop and Software Verify Phase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The project executes :ref:`sop-swdp` for software development,
specifically, the develop and software verify phase activities.


.. Describe any activities that are specific to your project,
   that are not covered by the SOP, or that need to be highlighted
   for your project.

The expected results and evidences are listed (including the location
where) herafter, ordered by the respective activity.


Software Requirements
^^^^^^^^^^^^^^^^^^^^^^

- Primary source of software requirements - is sphinx-needs
- Location ``docs/software/swrs/`` folder
- Software requirements are traceable to their origin e.g.
  user needs, system requirements, risk control measures.
- A Traceability matrix is maintained, and is available at
  ``docs/software/swrs/traceability.rst``

Software Requirements
^^^^^^^^^^^^^^^^^^^^^^

- Primary source of software design - is sphinx-needs
- Location ``docs/software/swds/`` folder
- Software design elements are traceable to their origin e.g.
  user needs, system requirements, software requirements.
- A Traceability matrix is maintained, and is available at
  ``docs/software/swds/traceability.rst``

Software Risk Assessment
^^^^^^^^^^^^^^^^^^^^^^^^

- Primary source of software risk assessment - is sphinx-needs
- Location ``docs/software/risks/`` folder
- Mitigation measures are identified and stored
  at ``docs/software/risks/requirements.rst``
- Risidual risks are identified and stored at ``docs/software/risks/residual-risks.rst``
- The risk class is justified and stored at ``docs/software/risks/risk-class.rst``

Tool Validation
^^^^^^^^^^^^^^^

- Tools are identified and listed at ``docs/project-control/records/tool-validation``
- Each tool is validated according to :ref:`sop-toolval:sop-toolval` and the results
  are stored in the same folder.

SouP Validation
^^^^^^^^^^^^^^^

- Software of unknown Provenance are identified and listed
  at ``docs/project-control/records/soup-validation``
- Each :term:`SouP` is validated according to :ref:`sop-soupval:sop-soupval` and the results
  are stored in the same folder.

Cybersecurity Assessment
^^^^^^^^^^^^^^^^^^^^^^^^

- A threat model is created and maintained at
  ``docs/software/cybersecurity/threat-model.rst``
- Each :term:`CVE` is tracked.
  Where and how the CVE tracking is done depends on the software design,
  SouP's and SouP's tooling and project CI/CD strategy

  It needs to be described in the curse of this phase, and the results need
  to be stored in the project repository/ this plan.

- SBOM are created and as part of the release process through CI

.. todo ::

  Detail down the CVE management process

Implementation
^^^^^^^^^^^^^^

- Repository branch protection rules require:
  - signed commits,
  - authenticated users,
  - verified commits
- At pull request review,
  - CI: conventional commits check
  - CI: static code analysis
  - CI: unit test execution and coverage reporting
  - Peer review of code changes

    - including traceability to requirements
    - and risk control measures,
    - and verification of the implementation against
    - the design and requirements.
    - including check of code style and coding standard.
    - including check of documentation correctness and completeness.

Provided Evidences
"""""""""""""""""""

Code review reports are stored within Azure DevOps, and are accessible through
the respective pull request links.

Additionally, not acceptable deviations are fixed by the author prior to merging.

Unit test reports and coverage reports are provided by CI.

Traceability evidence is given by a mapping of the software unit as described
detailed design to a set of folders in the source code.



.. todo:: Organization of the implementation phase

  - Write down coding standards and code style rules, and how they are enforced in the project.
  - Write down the code review process, and how it is enforced in the project.
  - Detail down code review criteria.
  - Write down commit message requirements, and how they are enforced in the project.

.. todo:: Tooling

  - Detail down toolchain, build container, CI/CD strategy
  - Access to Target ISE for ci testing and verification


Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~

Source Code and Version Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: Review and update the configuration management strategy.

- Version control system is git, and the repository is hosted on Azure DevOps.
- Branching strategy is
  `GitFlow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_.
  - The feature branch and release branches are protected by branch protection rules,
  - Feature branches require pull requests review.
- Versioning strategy is
  `semantic versioning <https://semver.org/>`_,
  and version numbers are assigned
  at release time.
- Prior to release, the version major version is 0, and the initial minor version
  is 1, and incremented according to the rules of semantic versioning.
  Dev versions are marked with -dev suffix and the respective build number.
- Release tags are created at release time, and follow the format v<MAJOR>.<MINOR>.<PATCH>
- Versions are stamped into the software during build time,
  and are available in the software at runtime.
- Version numbers are also stored in the documentation, and are updated at release time.
- Individual software items with individual lifecycle are maintained in individual
  git repositories and versioned individually.
  (They potentially following other versioning rules, as dictated by their
  lifecycle and release strategy, e.g. SouP software)


Build and Integration
^^^^^^^^^^^^^^^^^^^^^^

- The build process is automated through CI/CD pipelines.
- Build environments are defined as code, and are maintained in a project repository.
- Build environments are versioned and stored/archived as container images.
- The build process includes the following steps:
  - Code checkout
  - Dependency installation
  - Version stamping
  - Build execution
  - Unit test execution and coverage reporting
  - Static code analysis
  - Build artifact generation and storage
  - Documentation generation and storage
- Build artifacts are stored in the CI/CD system and are accessible through the
  respective build links, and are archived according to the CI/CD strategy.
- Dependencies (software items in individual git repositories) are included in the product
  software through submodules, and the version of the submodule is updated at release time.

.. todo:: include software items with individual lifecycle and versioning

   Is git submodules the best solution?

Verification
^^^^^^^^^^^^^

Verification activities are performed according to :ref:`sop-verif:sop-verif` ,
and the test reports of manually executed testsare stored in the project repository
at ``docs/software/releases/<version>`` folder.

(Automated test reports are stored in the CI/CD system, and are accessible through
 the respective build links, and are archived according to the CI/CD strategy.)

The test plans and test cases are maintained in the project repository at
``docs/software/testing/`` folder, and are traceable to their
origin e.g. requirements.

.. todo:: Formalize the verification strategy, and how it is enforced in the project.


Release
^^^^^^^

Release activities are performed according to :ref:`sop-swdp` Activity - Release,
and the release notes are stored in the project repository .. attention:: text

``docs/software/releases/<version>/sw-release-notes_<version>.rst``

Additionally, all release artifacts are published and archived in a git-lfs
release repository in azure devops.
(This is the "handover point" to production and service.)
