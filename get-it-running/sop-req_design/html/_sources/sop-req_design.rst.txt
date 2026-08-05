.. _sop-req_design:

SOP — Software Requirement and Design Procedure
****************************************************

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

This :term:`SOP` defines the iterative process by which the project derives,
structures, and refines its software requirements and design artefacts —
from high-level stakeholder needs through system-level requirements and
architecture, down to detailed software requirements and software design
specifications, with an embedded preliminary risk analysis cycle that feeds
safety and cybersecurity risk-control requirements back into the
requirements baseline.

The procedure establishes the roles, artefact types, traceability links,
and review gates that govern this cyclic improvement process throughout the
software development lifecycle.

Scope
-----

This :term:`SOP` applies to all software development activities that produce
or consume the following controlled artefact types:

- Stakeholder and user needs
- System requirements and system design specifications
- Risk and hazard records, including risk-control measure requirements
- Software requirements (top-level and detailed)
- Software design specifications (top-level and detailed)
- Software test cases that verify requirements

It is applicable for Software Safety Classes A, B, and C as defined by
IEC 62304, and it is designed to support compliance with IEC 62304 clauses
5.1–5.4 (software requirements and architecture) as well as ISO 14971
clause 10 (software contribution to risk management).

Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history is derived from a query to
the git repository.

.. git_changelog::
   :filename_filter: docs/sop/sop-req_design/sop-req_design.rst

References
----------

Standards implemented or complied with by this :term:`SOP`:

- **IEC 62304:2006 + A1:2015** — Medical device software — Software life cycle processes

  - Clause 5.1 — Software development planning
  - Clause 5.2 — Software requirements analysis
  - Clause 5.3 — Software architectural design
  - Clause 5.4 — Software detailed design

- **ISO 14971:2019** — Medical devices — Application of risk management to medical devices

  - Clause 5 — Risk analysis
  - Clause 6 — Risk evaluation
  - Clause 7 — Risk control
  - Clause 10 — Software as a component of a medical device

- **IEC 62443-4-1:2018** — Security for industrial automation and control systems — Part 4-1:
  Secure product development lifecycle requirements (for cybersecurity concerns)

Applied :term:`SOP`\s:

- :ref:`sop-docctl:sop-docctl` — Documentation control for all artefacts produced
- :ref:`sop-swdp:sop-swdp` — Software Development Plan; defines milestones and release gates
- :ref:`sop-verif:sop-verif` — Verification procedure applied to requirements and design
- :ref:`sop-cybersec:sop-cybersec` — Cybersecurity procedure for threats and risk controls

Roles and Responsibilities
==========================

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Role
     - Responsibility
   * - Systems Engineer / Requirement Author
     - Elicit and document stakeholder needs; derive and maintain system
       requirements; co-author system specifications; trace requirements to
       needs and design artefacts.
   * - Software Architect / Design Author
     - Derive system and software design specifications; ensure specifications
       implement the corresponding requirements; maintain ``implements`` links.
   * - Risk Manager
     - Perform preliminary risk analysis; document hazards and risks; identify
       required risk-control measures; ensure risk-control requirements carry
       ``concerns: safety`` and valid ``mitigates`` links.
   * - Cybersecurity Engineer
     - Identify cybersecurity threats alongside risk analysis; author or review
       requirements carrying ``concerns: cybersecurity``; liaise with Risk Manager
       where concerns overlap.
   * - Software Engineer
     - Derive and document detailed software requirements; author software design
       specifications; maintain ``derives`` and ``implements`` links.
   * - Test Engineer
     - Author test cases that verify requirements; maintain ``verifies`` links.
   * - Reviewer / QA
     - Verify completeness, consistency, and traceability at each review gate;
       approve artefacts before promotion to the next phase.


Process Overview
================

The following diagram illustrates the cyclic improvement process defined
by this procedure. The process is intentionally iterative: each design phase
may reveal gaps in the requirements above it, and each risk analysis pass may
introduce new requirements that feed back into the design.

.. mermaid::

   flowchart TD
       A[Stakeholder Needs\n  need N_ ] --> B[System Requirements\n  req level:system ]
       B --> C[System Design\n  spec level:system ]
       C --> D{Preliminary\nRisk Analysis}
       D -->|new risk-control\nrequirements| B
       D --> E[Risk and Hazard\nRecords  risk  hazard ]
       E --> F[Risk-Control Requirements\n  req  concerns:safety/cybersecurity\n mitigates  RSK_ / HAZ_ ]
       F --> G[Software Requirements\n  req level:software ]
       B --> G
       G --> H[Software Design Specifications\n  spec level:software ]
       H --> I[Test Cases\n  test ]
       I -->|verification gap\nor anomaly| G
       G -->|scope change or\nnew hazard| D
       H -->|further risk identified| D

   style A fill:#9856a5,color:#fff
   style B fill:#BFD8D2
   style C fill:#FEDCD2
   style E fill:#DF744A,color:#fff
   style F fill:#BFD8D2
   style G fill:#BFD8D2
   style H fill:#FEDCD2
   style I fill:#DCB239


Artefact Types and Fields
=========================

All requirements, specifications, risks, and test cases are managed as
sphinx-needs *needs* within the source repository.  The table below
summarises the types used by this procedure.

.. list-table::
   :header-rows: 1
   :widths: 12 12 12 64

   * - Type
     - Directive
     - Prefix
     - Purpose
   * - Need
     - ``need``
     - ``N_``
     - Stakeholder, user, market, business, or regulatory need.
       Must carry a ``category`` field.
   * - Requirement
     - ``req``
     - ``REQ_``
     - Any requirement at any level. Must carry a ``level`` field.
       May carry ``concerns``, ``constraint``, ``release``, and link fields.
   * - Specification
     - ``spec``
     - ``SPEC_``
     - Any design specification at any level. Must carry a ``level`` field.
       Links to requirements via ``implements``.
   * - Risk
     - ``risk``
     - ``RSK_``
     - Identified risk combining a hazard situation with likelihood and
       severity. Linked from mitigating requirements via ``mitigates``.
   * - Hazard
     - ``hazard``
     - ``HAZ_``
     - Source of potential harm. Linked to risks via ``causes``.
   * - Test Case
     - ``test``
     - ``TC_``
     - Verification artefact. Links to requirements via ``verifies``.

Mandatory Fields per Artefact
------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 22 60

   * - Field
     - Applies to
     - Description
   * - ``:id:``
     - all
     - Unique, stable identifier. Must never be changed after first release.
   * - ``:level:``
     - ``req``, ``spec``
     - ``system``, ``hardware``, ``software``, or ``detailed_software``.
   * - ``:category:``
     - ``need``
     - ``user``, ``business``, ``market``, ``organizational``, or ``regulatory``.
   * - ``:concerns:``
     - ``req``, ``spec``
     - ``safety``, ``cybersecurity``, or both (comma-separated).
       Required when the artefact is a risk-control measure or addresses a
       security threat.
   * - ``:constraint:``
     - ``req``
     - Boolean ``true`` when the requirement is also a design constraint
       that restricts the solution space.
   * - ``:release:``
     - ``req``, ``spec``
     - Target milestone (e.g., ``mvp``).  Recommended for all software-level
       artefacts.

.. _sop-req_design/links:

Traceability Links
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Link field
     - Semantic meaning
   * - ``:derives:``
     - This artefact is *derived from* the referenced need or higher-level
       requirement.  Direction: child → parent.
   * - ``:implements:``
     - This specification *implements* the referenced requirement.
       Direction: spec → req.
   * - ``:verifies:``
     - This test case *verifies* the referenced requirement.
       Direction: test → req.
   * - ``:mitigates:``
     - This requirement or specification *mitigates* the referenced risk
       or hazard.  Direction: control → risk/hazard.
   * - ``:causes:``
     - This hazard *causes* the referenced risk.
       Direction: hazard → risk.
   * - ``:constrains:``
     - This requirement or risk *constrains* the referenced artefact.


Procedure
=========

Phase 1 — Elicit and Document Stakeholder Needs
------------------------------------------------

The process begins with structured elicitation of all stakeholder goals,
expectations, and constraints. Each distinct need is documented as a
``need`` artefact and assigned a stable identifier.

**Activities**

1. Conduct stakeholder interviews, user research, and regulatory review.
2. Group needs by category: ``user``, ``business``, ``market``,
   ``organizational``, or ``regulatory``.
3. Record each need as a ``need`` directive with a mandatory ``category``
   and a unique ``id``.
4. Have needs reviewed by a representative of the stakeholder group where
   possible.

**Example** — user need:

.. code-block:: rst

   .. need:: OP User must set the system's segment positions
      :id: N_U_001
      :category: user

      The OP User must be able to adjust the table segments
      to fit the surgeon's requirements for the specific procedure.

**Traceability gate**: Every system requirement in Phase 2 shall trace
back to at least one ``need`` via ``:derives:``.


Phase 2 — Derive System Requirements
--------------------------------------

System requirements translate stakeholder needs into solution-neutral,
verifiable statements about the system as a whole. They are assigned
``level: system``.

**Activities**

1. Review each stakeholder need and derive one or more system requirements.
2. Each requirement shall be:

   - **Atomic** — addresses a single concern.
   - **Verifiable** — can be confirmed by inspection, test, or analysis.
   - **Traceable** — linked to its parent need via ``:derives:``.

3. Flag requirements that restrict the solution space with
   ``constraint: true``.
4. Flag requirements arising from safety or cybersecurity considerations
   with the ``concerns`` field.
5. Obtain independent review and approval before baseline.

**Example** — system requirement derived from a user need:

.. code-block:: rst

   .. req:: Control panel HMI element
      :level: system
      :id: REQ_SY_001
      :derives: N_U_001

      The system shall provide a control panel on the column.
      The control panel is an HMI element that allows the user to set
      the system's segment positions.

**Example** — system-level safety requirement (risk-control measure):

.. code-block:: rst

   .. req:: Redundant button press detection
      :level: system
      :id: REQ_SY_M_001
      :concerns: safety
      :mitigates: RSK_001, HAZ_001
      :derives: N_U_001

      The system shall provide safe button press detection, such that
      the system can be certain the user truly intends the commanded
      table movement.

**Traceability gate**: All system requirements shall have a ``derives``
link to at least one ``need`` or to a risk-control decision documented
in Phase 3.


Phase 3 — System Architecture and Preliminary Risk Analysis
------------------------------------------------------------

System design decisions are documented as ``spec`` artefacts at
``level: system``. In parallel, a **preliminary risk analysis** (PRA)
is performed over the emerging architecture.

Phase 3a — System Design Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Activities**

1. Decompose the system into subsystems and functional blocks (e.g. via
   block diagrams and class diagrams authored in the design document).
2. For each design decision that allocates or realises a system requirement,
   create a ``spec`` artefact linked to the requirement via ``:implements:``.
3. Have the architecture reviewed by the Systems Engineer and Risk Manager
   before the PRA.

**Example** — system-level specification:

.. code-block:: rst

   .. spec:: Power Guard
      :level: system
      :id: SPEC_SY_001
      :implements: REQ_SY_M_001, ER_M_001
      :concerns: safety

      Power guard is an electronics-based mechanism that prevents motor
      activation when no movement command is actively asserted.
      It is realised redundantly on both the column controller and the
      master controller; both must independently fail for the guard to
      be defeated.

Phase 3b — Preliminary Risk Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PRA is conducted over the system architecture to identify hazards
that the design may introduce, enable, or fail to prevent, following
ISO 14971 clause 5.

**Activities**

1. For each subsystem and interface, ask: *"What can go wrong, and how
   could it harm a patient, user, or bystander?"*
2. Document each source of potential harm as a ``hazard`` artefact.
3. Document each combination of hazard situation, probability, and severity
   as a ``risk`` artefact, linked from the hazard via ``:causes:``.
4. For each unacceptable risk, derive one or more risk-control measure
   requirements (``req`` with ``concerns: safety``), linked via
   ``:mitigates:``.
5. Where a design decision already mitigates a risk, create a ``spec``
   artefact with ``concerns: safety`` and ``:mitigates:``.
6. Feed new risk-control requirements back into the Phase 2 baseline before
   proceeding to Phase 4.

**Example** — hazard, risk, and risk-control measure:

.. code-block:: rst

   .. hazard:: Unintended table movement
      :id: HAZ_001
      :probability: medium

      The table may move without a deliberate user command,
      e.g. due to a single stuck button or spurious signal.

   .. risk:: Patient injury due to unintended movement
      :id: RSK_001
      :severity: high
      :causes: HAZ_001

      Uncontrolled table movement can cause the patient to fall
      or be crushed by a moving segment.

   .. req:: Redundant button press detection
      :level: system
      :id: REQ_SY_M_001
      :concerns: safety
      :mitigates: RSK_001, HAZ_001

      The system shall provide safe button press detection so that
      the system can be certain the user truly intends the commanded
      movement before acting on it.

**Cybersecurity note**: Where a threat identified during cybersecurity
threat modelling (per :ref:`sop-cybersec:sop-cybersec`) can lead to a hazardous
situation, the resulting risk-control requirement shall carry
``concerns: safety, cybersecurity``.

**Example** — dual-concern risk-control requirement:

.. code-block:: rst

   .. req:: Authenticated firmware update channel
      :level: system
      :id: REQ_SY_SEC_001
      :concerns: safety, cybersecurity
      :mitigates: RSK_010

      The system shall only accept firmware update packages that are
      cryptographically signed by an authorised key.

**Traceability gate**: All ``risk`` artefacts shall have at least one
mitigating ``req`` or ``spec`` before Phase 4 may begin.


Phase 4 — Derive Software Requirements
---------------------------------------

Software requirements specify the behaviour of the software element
in terms that the software development team can implement and verify.
They are assigned ``level: software`` (or ``level: detailed_software``
for fine-grained decomposition).

**Activities**

1. Review all system requirements (``level: system``) and system design
   specifications (``level: system``) allocated to software.
2. For each allocated item, derive one or more software requirements that
   collectively satisfy it.
3. Link each software requirement to its parent(s) via ``:derives:``.
4. Propagate ``concerns`` and ``mitigates`` links from parent system-level
   risk-control requirements where the software requirement is the
   implementing mechanism.
5. Assign a ``release`` milestone to prioritise the requirement.
6. For design constraints (e.g. mandated OS, communication protocol),
   add ``constraint: true``.
7. Submit the software requirements baseline to independent review.

**Example** — software requirement derived from a system requirement:

.. code-block:: rst

   .. req:: Keep button pressed for moving
      :level: software
      :release: mvp
      :id: REQ_SW_001
      :derives: REQ_SY_001, REQ_SY_002

      The software shall only move a segment while the corresponding
      movement button is continuously held by the user, and shall stop
      immediately upon button release.

**Example** — software-level risk-control requirement:

.. code-block:: rst

   .. req:: Drive command integrity check
      :level: software
      :release: mvp
      :id: REQ_SW_M_002
      :concerns: safety
      :mitigates: RSK_001, HAZ_003
      :derives: REQ_SY_M_001

      The software shall encode drive commands with a verifiable
      integrity code so that the motor actuator can detect and discard
      corrupted commands.

**Example** — software constraint requirement:

.. code-block:: rst

   .. req:: C and C++ language for embedded control software
      :level: software
      :id: REQ_CON_001
      :constraint: true

      The embedded control software shall be implemented in C or C++
      conforming to the project's applicable coding standard.

**Traceability gate**: Each software requirement shall carry a
``:derives:`` link to at least one system-level ``req`` or ``spec``,
or to a risk-control decision (``mitigates`` link).


Phase 5 — Software Design Specifications
-----------------------------------------

Software design specifications describe *how* the software realises its
requirements. They are assigned ``level: software`` (or
``level: detailed_software`` for unit-level design).

**Activities**

1. For each software requirement or group of cohesive requirements, author
   one or more ``spec`` artefacts describing the design decision that
   implements them.
2. Link each specification to the requirement(s) it implements via
   ``:implements:``.
3. Where the specification also constitutes a risk-control mechanism,
   add ``concerns: safety`` (and/or ``cybersecurity``) and a
   ``:mitigates:`` link.
4. Verify that no software requirement is left without a corresponding
   specification before the phase closes.
5. Submit the design specification set to independent review.

**Example** — software design specification:

.. code-block:: rst

   .. spec:: Command message integrity check
      :level: software
      :id: SPEC_SW_005
      :implements: REQ_SW_M_002
      :concerns: safety

      Drive commands transmitted over CAN shall include a CRC field
      computed over the command payload.  The receiver shall discard
      any command whose CRC does not match the payload, and shall
      emit a diagnostic log entry.

      CAN 2.0 hardware CRC covers transit errors; this application-level
      CRC additionally covers logical content integrity.

**Example** — detailed software design specification:

.. code-block:: rst

   .. spec:: Motor stop on missing heartbeat
      :level: detailed_software
      :id: SPEC_SW_042
      :implements: REQ_SW_F00, REQ_SW_G02
      :concerns: safety

      The motor controller firmware shall monitor a heartbeat signal
      from the master controller with a period of 25 ms ± 5 ms.
      If two consecutive heartbeats are missed, all motor outputs
      shall be de-energised within one control cycle (≤ 10 ms).

**Traceability gate**: Every ``spec`` shall implement at least one
``req``.  Every ``req`` at ``level: software`` shall be implemented
by at least one ``spec`` before the design baseline is closed.


Phase 6 — Test Case Authoring
-------------------------------

Test cases provide objective evidence that software requirements are met.
They are authored in parallel with, or immediately after, Phase 4.

**Activities**

1. For each ``req`` at ``level: software`` or ``level: detailed_software``,
   author at least one ``test`` artefact with a clear pass/fail criterion.
2. Link each test to the requirement it verifies via ``:verifies:``.
3. For risk-control requirements (carrying ``concerns: safety``), ensure
   that the test exercises the specific safety mechanism and that its
   result constitutes objective evidence of risk reduction.
4. Follow :ref:`sop-verif:sop-verif` for test planning, execution, and evidence
   retention.

**Example** — test case:

.. code-block:: rst

   .. test:: Verify drive command CRC rejection
      :id: TC_SW_M_002_01
      :verifies: REQ_SW_M_002

      **Setup**: Motor controller in Active state; CAN interface connected.

      **Action**: Inject a drive command with a deliberately corrupted CRC.

      **Expected result**: The motor controller discards the command,
      no motor movement occurs, and a CRC-error diagnostic entry is logged.

**Traceability gate**: No software requirement carrying ``concerns: safety``
may be closed without at least one passing test result linked via
``:verifies:``.


Cyclic Improvement and Re-entry Points
=======================================

This procedure is **iterative**, not waterfall.  The following events
shall trigger a re-entry into the cycle at the appropriate phase:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Trigger
     - Re-entry point
   * - New or changed stakeholder need
     - Phase 1; propagate changes forward through Phases 2–6.
   * - Architecture change (e.g. new subsystem, new interface)
     - Phase 3; repeat PRA over the changed area; update risk-control
       requirements; propagate through Phases 4–6.
   * - New hazard or risk identified during implementation or test
     - Phase 3b; derive risk-control requirement; propagate through Phases 4–6.
   * - Software requirement gap identified during design (Phase 5)
     - Phase 4; add missing requirement; update traceability.
   * - Verification anomaly or test failure (Phase 6)
     - Phase 4 or 5, depending on whether the root cause is a missing
       requirement or a design error.
   * - Change request or problem report post-release
     - Phase 2 or 3, depending on whether the root cause is at system
       or design level.

All re-entries shall be documented with a change rationale referencing
the triggering problem report, risk record, or change request.  Impacts
on the risk management file shall be assessed per ISO 14971 clause 10.


Traceability Completeness Checks
==================================

The Sphinx build enforces the following automated checks via
sphinx-needs schema validation and constraint rules.  A build failure
or warning in any of these checks blocks promotion to the next milestone.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Check
     - Failing condition
   * - ``req-level-required``
     - A ``req`` artefact is missing the ``level`` field.
   * - ``need-category-required``
     - A ``need`` artefact is missing the ``category`` field.
   * - ``concerns-valid-values``
     - A ``concerns`` field contains a value other than ``safety`` or
       ``cybersecurity``.
   * - ``sw_req_must_have_test``
     - A ``req`` at ``level: software`` has no incoming ``verifies`` link.
   * - ``risk_must_have_control``
     - A ``risk`` artefact has no incoming ``mitigates`` link.
   * - ``risk_control_must_be_tested``
     - A requirement with ``origin: risk_control`` has no incoming
       ``verifies`` link.

In addition, the traceability matrix in the project's system-level and
software-level documents shall be reviewed manually at each milestone
gate to confirm end-to-end coverage from ``need`` through ``test``.


Records
=======

The following records shall be retained as controlled documents:

- Requirements baseline (system and software ``req`` artefacts)
- Design specification baseline (system and software ``spec`` artefacts)
- Risk management records (``hazard`` and ``risk`` artefacts and their
  mitigating links)
- Traceability reports generated by the Sphinx build
- Review evidence (pull request discussions, sign-off commits)
- Test specifications and executed test results (per :ref:`sop-verif:sop-verif`)

All records are stored in the Git repository and published as part of the
Sphinx-rendered documentation per :ref:`sop-docctl:sop-docctl`.


IEC 62304 Clause Mapping
=========================

.. list-table::
   :header-rows: 1
   :widths: 45 20 35

   * - Activity
     - IEC 62304 Clause
     - Covered by Phase
   * - Software requirements analysis
     - 5.2
     - Phase 2, Phase 4
   * - Software architectural design
     - 5.3
     - Phase 3a, Phase 5
   * - Software detailed design
     - 5.4
     - Phase 5 (detailed_software level)
   * - Software unit implementation
     - 5.5
     - :ref:`sop-impl:sop-impl`
   * - Software integration and verification
     - 5.6
     - Phase 6, :ref:`sop-verif:sop-verif`
   * - Software risk management contribution
     - 4.2 / ISO 14971 cl.10
     - Phase 3b


Deviations
==========

Any deviation from this procedure shall be documented with a rationale,
risk assessment, and approval per the :ref:`sop-docctl:sop-docctl` change
control process.

Glossary
========

.. include:: _glossary_terms.rst

.. glossary::

   Stakeholder Need
     A high-level statement of a goal, expectation, or constraint expressed
     by a user, operator, or other affected party, independent of any solution.
     Captured using the ``need`` artefact type (prefix ``N_``).

   System Requirement
     A solution-neutral, verifiable statement of what the system as a whole
     shall do or be, derived from stakeholder needs or risk-control decisions.
     Captured using the ``req`` artefact type at ``level: system``
     (prefix ``REQ_``).

   System Specification
     A design decision at system level describing *how* the system realises
     one or more system requirements — typically architectural in nature.
     Captured using the ``spec`` artefact type at ``level: system``
     (prefix ``SPEC_SY_``).

   Software Requirement
     A verifiable statement of what the software element shall do, derived
     from system requirements or from system design decisions.
     Captured using the ``req`` artefact type at ``level: software``
     (prefix ``REQ_``).

   Software Design Specification
     A design decision describing how a software element realises one or more
     software requirements.
     Captured using the ``spec`` artefact type at ``level: software``
     (prefix ``SPEC_SW_``).

   Hazard
     A potential source of harm to a patient, user, or third party.
     Captured using the ``hazard`` artefact type (prefix ``HAZ_``).

   Risk
     The combination of the probability of occurrence of a hazard-related
     situation and its severity.
     Captured using the ``risk`` artefact type (prefix ``RSK_``).

   Risk-Control Measure
     A design decision or requirement intended to reduce a risk to an
     acceptable level. Implemented as a ``req`` or ``spec`` artefact with
     a ``mitigates`` link to the relevant ``risk`` or ``hazard``.

   Concerns
     A cross-cutting domain classification applied to requirements and
     specifications that contribute to safety or cybersecurity.
     Valid values: ``safety``, ``cybersecurity``.

   Traceability Link
     A directed relationship between two artefacts expressing a semantic
     dependency. See :ref:`sop-req_design/links`.

   Design Constraint
     A requirement that narrows the solution space by mandating a specific
     technology, platform, or architectural choice.
     Marked with the ``constraint: true`` field.

   Preliminary Risk Analysis
     A risk analysis performed during system design to identify hazards
     introduced or influenced by design decisions, before detailed software
     requirements are written.
