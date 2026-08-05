

:orphan:

.. _tpl-swrs:

MyProject — Software Development Requirement Specification
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

.. _control:

.. doc_control::
   :version: 1.0
   :based_on_template: 001
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

This document contains the Software Requirement Specification and (:term:`SwRS`)
Detailed Software Requirement Specification (:term:`DSwRS`)
of **MyProject**.


Purpose
-------

The purpose of this document is to manage all software requirements,

- such that they are easy to access by developers and testers
  (the last released version)
- such that traceability is granted to system requirements, system design
  and risk mitigation requirements.
- such that they comply with QMS System directly, and therefore indirectly with
  regulatory requirements.

Scope
-----

This document is the **only place** where **software requirements** are managed.

Top-level software requirements are derived from (and therefore "derive referenced")
from system requirements, risk mitigation requirements and/or system design.

Detailed software requirements are derived from (and therefore "derive referenced")
from softare requirements, risk mitigation requirements and/or software design


.. Handlining higher level requirement items

   like system requirement are managed somewhere else,

   this git repo is not primary source. there are pulled, in a controlled
   manual/semiautomatic process. This injection needs to be carefully documentted
   and supervised, to guarantee data integrity across different versions of
   requirements.


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



Software Requirement Specification
==================================

HMI related functional Requirements
-----------------------------------


System related functional Requirements
--------------------------------------


Risk Mitigation functional Requirements
---------------------------------------

(safety requirements)

Performance Requirements
------------------------


Security related Requirements
-----------------------------




Detailed Software Requirement Specification
===========================================

DSwRS - Unit ABC
----------------

DSwRS - Unit DEF
----------------

DSwRS - Unit GHI
----------------
