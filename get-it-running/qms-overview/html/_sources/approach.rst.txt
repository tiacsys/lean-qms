
Medical Device Development with a Git-based / Sphinx-based QMS
==============================================================

**Traceable • Reproducible • Auditable • Compliant**

This document provides an overview of a modern documentation-centric quality
management approach for medical device software development using:

* Git
* GitHub / GitLab / Azure Cloud
* Sphinx
* CI/CD pipelines
* Pull-request based reviews
* Immutable audit trails

The approach is especially suitable for:

* IEC 62304 software lifecycle processes
* ISO 13485 documentation control
* ISO 14971 risk management integration
* FDA traceability expectations
* Reproducible engineering environments

Introduction
------------

Traditional medical device quality management systems are often based on:

* Office documents
* Shared drives
* Manual reviews
* Detached traceability systems
* Spreadsheet-driven evidence tracking

A Git-based QMS instead treats:

* documentation,
* requirements,
* architecture,
* verification,
* procedures,
* and evidence

as version-controlled engineering artifacts.

This creates:

* complete history,
* immutable change tracking,
* reproducible documentation,
* review evidence,
* and auditability directly inside the engineering workflow.

Core Building Blocks
------------------------

Git
~~~

Git acts as the central version-controlled evidence store.

Git provides:

* change history
* branching
* immutable commit records
* tags/releases
* provenance tracking
* review linkage

Typical use:

* requirements
* procedures
* source code
* risk files
* verification documents
* architecture documentation
* CI reports

GitHub / GitLab / Azure Cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The forge platform provides:

* pull requests / merge requests
* review workflows
* approvals
* issue tracking
* branch protection
* release management
* CI integration

Typical regulatory-relevant controls:

* required reviewers
* signed commits
* protected main branch
* merge commit enforcement
* review approval tracking

Sphinx Documentation System
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx acts as the structured documentation generation layer.

Sphinx provides:

* HTML output
* PDF output
* cross references
* glossary integration
* document numbering
* requirement linkage
* reproducible builds

Documentation becomes:

* modular
* reviewable
* traceable
* testable
* version controlled

CI/CD Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continuous integration pipelines generate:

* documentation builds
* test reports
* static analysis reports
* SBOMs
* release artifacts
* audit evidence

CI pipelines also enforce:

* quality gates
* build reproducibility
* linting
* review policies
* traceability checks

Infrastructure as Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Infrastructure and build environments should also be version controlled.

Examples:

* Dockerfiles
* CI pipeline definitions
* deployment scripts
* toolchain definitions
* reproducible development environments

This improves:

* reproducibility
* onboarding
* auditability
* environment consistency

QMS / DMS Function Coverage
----------------------------

The following sections describe how classical QMS and DMS functions are realized inside the Git/Sphinx workflow.

Document Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implemented through:

* Git version control
* immutable history
* pull requests
* release tagging
* branch protection

Capabilities:

* document versioning
* history tracking
* rollback capability
* release baselines
* change attribution

Review and Approval
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implemented through:

* pull request reviews
* reviewer assignments
* approval policies
* merge restrictions
* review trailers

Typical workflow:

1. change proposed
2. pull request created
3. reviewers assigned
4. review comments resolved
5. approvals granted
6. merge commit created

Possible audit trailers:

.. code::

    Reviewed-by: Alice Example [alice@example.com](mailto:alice@example.com)
    Approved-by: Bob Example [bob@example.com](mailto:bob@example.com)
    Signed-off-by: Carol Example [carol@example.com](mailto:carol@example.com)

Change Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implemented through:

* commits
* branches
* pull requests
* issue linkage
* release tags

Every change can be traced to:

* author
* timestamp
* rationale
* issue/requirement
* review discussion
* approval record

Traceability
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Traceability is established through bi-directional linking.

Examples:

* requirement -> implementation
* implementation -> test
* issue -> commit
* risk -> mitigation
* CAPA -> corrective change

Possible linking mechanisms:

* issue references
* Sphinx cross references
* requirement identifiers
* commit trailers
* CI-generated traceability matrices

Records and Evidence
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Evidence is generated continuously during development.

Examples:

* Git history
* pull request discussions
* approvals
* CI logs
* generated reports
* test artifacts
* releases
* signed binaries

The Git repository becomes an immutable engineering evidence chain.

Training and Competence
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Procedures and guidance can be maintained directly in Sphinx.

Examples:

* onboarding guides
* coding standards
* review procedures
* release workflows
* risk management procedures
* verification procedures

Advantages:

* versioned procedures
* reviewable process documentation
* historical visibility
* controlled updates

CAPA / Corrective Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

CAPA workflows can be integrated into issue tracking systems.

Typical flow:

1. issue detected
2. CAPA created
3. investigation documented
4. corrective action implemented
5. verification executed
6. closure reviewed

All associated evidence remains linked.

## Regulatory Compliance

The approach supports:

* ISO 13485
* IEC 62304
* ISO 14971
* FDA traceability expectations

The system does not replace regulatory processes.

Instead, it provides:

* controlled documentation
* reproducible evidence
* review traceability
* audit-ready history
* engineering accountability

Documentation Structure with Sphinx
------------------------------------

A typical repository layout may look like this:

.. code ::

    docs/
    ├── index.rst
    ├── requirements/
    │   ├── index.rst
    │   └── req-001.rst
    ├── architecture/
    │   ├── index.rst
    │   └── system-overview.drawio
    ├── design/
    │   ├── index.rst
    │   └── module-x.rst
    ├── verification/
    │   ├── index.rst
    │   └── test-plan.rst
    └── quality/
        ├── index.rst
        └── risk-analysis.rst

Generated outputs:

* HTML documentation
* PDF documentation
* release archives
* CI artifacts

All documents remain linked to:

* issues
* commits
* pull requests
* requirements
* releases
* verification evidence

Typical Development Workflow
-----------------------------

1. Planning
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities:

* create issue
* define requirement
* link to standards
* define acceptance criteria

Outputs:

* requirement document
* issue ticket
* risk references

2. Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities:

* create feature branch
* implement change
* update documentation
* add tests

Outputs:

* commits
* updated docs
* verification artifacts

3. Review
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities:

* create pull request
* perform technical review
* perform quality review
* resolve comments

Outputs:

* review records
* review comments
* approval evidence

4. Approval
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities:

* required approvals granted
* CI checks pass
* branch protections validated

Outputs:

* approval state
* merge authorization

5. Merge
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities:

* merge commit created
* review trailers added
* release baseline updated

Outputs:

* immutable history entry
* audit trail
* traceable merge record

6. CI / Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities:

* build software
* run tests
* generate documentation
* run static analysis
* generate SBOM

Outputs:

* test reports
* analysis reports
* generated documentation
* release artifacts

7. Release
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities:

* tag release
* archive evidence
* publish artifacts
* export reports

Outputs:

* release package
* reproducible baseline
* archived evidence

Traceability Flow
------------------

A typical engineering traceability chain looks like:

.. mermaid::

    %%{init: {
       "theme": "base",
       "themeVariables": {
           "primaryColor": "#f8fbff",
           "primaryTextColor": "#000000",
           "primaryBorderColor": "#4a78d1",
           "lineColor": "#406090",
           "secondaryColor": "#eef5ff",
           "tertiaryColor": "#ffffff",
           "background": "#ffffff",
           "mainBkg": "#f8fbff",
           "nodeBorder": "#4a78d1"
       }
   }}%%

   flowchart TD
       RD["Architecture / Design"]
       Requirement --> RD
       RD --> Implementation
       Implementation --> Verification
       Verification --> Release


Every stage should remain linked through:

* identifiers
* references
* commits
* issues
* generated reports

Advantages of the Git/Sphinx QMS Approach
-----------------------------------------

Engineering Advantages
~~~~~~~~~~~~~~~~~~~~~~

* documentation as code
* reproducible outputs
* automated consistency checks
* integrated review workflow
* scalable collaboration

Quality Advantages
~~~~~~~~~~~~~~~~~~~~~~

* immutable audit history
* traceable approvals
* controlled procedures
* integrated evidence generation
* historical accountability

Regulatory Advantages
~~~~~~~~~~~~~~~~~~~~~~

* exportable evidence
* controlled baselines
* reproducible releases
* linked verification evidence
* review traceability

Recommended Practices
----------------------

Recommended controls for regulated projects:

* protected main branch
* merge commits only
* no squash merges
* signed commits
* mandatory reviews
* CI quality gates
* documented procedures
* reproducible CI environments
* archived release evidence

Conclusion
----------------------

A Git-based and Sphinx-based QMS approach combines:

* software engineering workflows,
* documentation control,
* traceability,
* review management,
* and audit evidence

into a unified engineering system.

Instead of treating documentation and quality activities as detached processes, the workflow integrates them directly into daily development practices.

This enables:

* continuous traceability,
* reproducible documentation,
* engineering accountability,
* and audit-ready evidence generation.
