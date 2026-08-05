.. _sop-cybersec:

SOP-Software — Cybersecurity Procedures
***************************************

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

This :term:`SOP` defines cybersecurity activities applicable to software elements
that are part of a medical product. It complements the Software Implementation SOP
(by excluding static code analysis, which is covered there) and focuses on activities
such as threat model creation, protectable asset evaluation, cybersecurity risk
assessment, SBOM generation, CVE tracking and mitigations, and evidence traceability.

Scope
-----

Applies to software elements and associated artifacts used within medical products,
including embedded firmware, software components, production/test tools, and
relevant third-party dependencies. Intended for use across Software Safety Classes
A/B and extended for Class C as needed.

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. git_changelog ::
    :filename_filter: docs/sop/sop-cybersec/sop-cybersec.rst

References
----------

- IEC 62304:2006 + A1:2015 - Medical device software — Software life cycle processes
- Relevant cybersecurity guidance (FDA/EMA/MDCG) and IEC 62443 / ISO 27001 where applicable
- SOP-Software — Software Development Procedure :ref:`sop-swdp:sop-swdp`
- SOP-Software — Implementation Procedure :ref:`sop-impl:sop-impl`

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
   * - Cybersecurity Engineer
     - Lead threat modelling, vulnerability analysis, SBOM generation and mitigation planning
   * - Software Engineer
     - Provide component details, support integration tests and remediation
   * - Test Engineer
     - Execute cyber-related verification (HIL fuzzing, penetration tests) and collect evidence
   * - QA/RA
     - Approve cyber risk assessments, ensure regulatory alignment
   * - Configuration Manager
     - Maintain SBOM artifacts and component versions

Procedure
=========

Overview
--------

Cybersecurity activities ensure identification, assessment, mitigation, and traceable
recording of software-related security risks. Activities integrate with the verification
and release gates defined in the SwDP and SwTP.

Protectable Asset Evaluation
----------------------------

- Identify assets (code modules, secrets, keys, data stores, interfaces, hardware endpoints).
- Classify assets by confidentiality, integrity, availability (CIA) impact and safety relevance.
- Record asset owners and responsible teams.

Threat Modeling
---------------

- Create and maintain a threat model for each major software component and the system architecture.
- Use attacker profiles, STRIDE or similar frameworks; document attack vectors and likelihood/impact.
- Map threats to protectable assets and proposed mitigations.
- Review threat models at architectural changes and major releases.

Cybersecurity Risk Assessment
-----------------------------

- For each identified threat, perform risk assessment (likelihood × impact) and recommend mitigations.
- Prioritize mitigations according to risk, safety relevance, and available resources.
- Document residual risk and accepted risk with approvals.

SBOM Generation and Management
-------------------------------

- Generate an SBOM for each release including direct and transitive dependencies (use SPDX/CycloneDX formats).
- Automate SBOM generation in CI and attach SBOMs to release artifacts.
- Record component versions, licenses, and origin.

Vulnerability and CVE Tracking
------------------------------

- Subscribe to relevant CVE sources and security advisories for third-party components used.
- Maintain a tracked list of vulnerabilities affecting the product — include severity, affected versions, and status.
- Define SLAs for triage and remediation per vulnerability severity (e.g., critical, high, medium, low).
- For each CVE, record mitigation: patch, upgrade, compensating control, or accepted risk.

Secure Integration and Testing
------------------------------

- Plan and execute security-focused tests during HW–SW and SW–SW integration phases (e.g., fuzzing, protocol fuzz, boundary tests).
- Include HIL and simulated attacker scenarios where feasible.
- Record test cases, environment, results, and remediation traces.

Patch and Release Management
----------------------------

- Integrate cybersecurity fixes into normal release branches respecting SwDP gates.
- Provide security release notes and associated SBOM updates.
- Ensure vulnerability fixes are traceable to CI runs, test evidence, and the SBOM.

Operational Monitoring and Post-Release
---------------------------------------

- Maintain processes for incident detection, reporting, and CVE response.
- Feed field incidents back into risk assessments and threat models.
- Apply CAPA workflow for systematic weaknesses.

Traceability and Records
------------------------

- Maintain traceability from threats and vulnerabilities to mitigations, test cases, and release artifacts using project traceability tooling (sphinx-needs links, reqSuite, or equivalent).
- Retain SBOMs, threat models, risk assessments, test results, and remediation records.

CI and Automation
-----------------

- Automate SBOM generation, vulnerability scanning, and baseline checks in CI pipelines.
- Fail pipelines on blocking security gates as defined in SwDP/SwTP.

Acceptance Criteria and Gates
------------------------------

- Define acceptance criteria for cyber gates in the SwTP (examples: no unresolved critical CVEs, threat model reviewed, SBOM attached to release).
- Gates must be signed off by QA/RA and Cybersecurity Engineer.

Deviations
----------

Any deviation from this procedure shall be documented and approved according to
SOP-DOCCTL.


.. note::
   This SOP is a bootstrap template. Tailor threat modeling approaches, SBOM tooling
   and response SLAs to project specifics in the SwDP and SwTP.

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

   Threat model
     A structured representation of potential threats, attack vectors, and mitigations for the system.

   Protectable asset
     Software, data, interfaces, or hardware elements whose compromise would adversely affect safety, privacy, or availability.

   SBOM
     Software Bill of Materials — a machine-readable inventory of software components and dependencies.
