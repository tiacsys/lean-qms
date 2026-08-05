

:orphan:

.. _tpl-swds:

MyProject — Software Development Design Specification
************************************************************

.. Commentary

   Is to guide you turning the document into a project specific
   requirement specification document that is under full QMS control

.. todo::

  1. Replace MyProject by your project name everywhere in this document
  2. Replace MyProjectAbbr by your project abbreviation in this document
  3. Replace MyProduct by your product name everywhere in this document

.. todo::

   Verify Inter-Sphinx appropriate link configuration

.. doc_control::
   :version: 1.0
   :based_on_template: tpl-swd_001
   :owner: MyProject
   :classification: Specification
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

This document contains the Software Design Specification and (:term:`SwDS`)
Detailed Software Design Specification (:term:`DSwDS`)
of **MyProject**.


Purpose
-------

The purpose of this document is to manage the software design,

- such that it is easy to access by developers and testers
  (the last released version)
- such that traceability is granted to software requirements, system design
  and risk mitigation requirements.
- such that they comply with QMS System directly, and therefore indirectly with
  regulatory requirements.

Scope
-----

This document is the **nearby place** where **software design** is described
and design decisions are documented.


Top-level software design is derived from (and therefore "derive referenced")
from software requirements, risk mitigation requirements and/or system design.

Detailed software design addresses the building blocks underneath it is derived
from (and therefore "derive referenced") from detailed softare requirements,
risk mitigation requirements and/or software design.


.. Info: the SwDS and SwRS are side - by side

  on purpose following the
  `Twin Peak Model <https://t2informatik.de/en/smartpedia/twin-peaks-model/?noredirect=en-US>`_

  The series of commits addressing requirement refinement and design refinement, while
  constantly CI checking mandatory traces allows for maximum data integrity across different
  version and allows for fast corrections.
  The management happens in a workflow and tooling (git, ci check, text documents),
  developers are very familiar with.


Change History
--------------

The history of this document is recorded within the git repository by the
commit messages. The following document history proposition is the result
of a query to the git repository.

.. code::

  # does not work straight on github, final solution on azure - resolve it over there
  .. git_changelog ::
	  :filename_filter: docs/qms/MyProjectAbbr-swrs.rst


References
----------

.. add this here if you overwrite a certain procedure of SOP

  Requirements of standards this SOP implements or complies with:

  - IEC 62304:2006 + A1:2015 - Medical device software — Software life cycle processes
    - Clause xyz


Applied SOP's


- SOP-SWDP :ref:`sop-swdp` - SOP for medical software development


Definitions
-----------

..

  Add project specific terms here, that are not part of any SOP yet.
  Do as you go.


No project specific terms defined.

.. explain ID-system


Software Design Specification
==============================

.. todo:: add arc24 template here
