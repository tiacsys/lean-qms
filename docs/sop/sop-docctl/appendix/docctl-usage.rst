.. _sop/sop-docctl/appendix-docctl-usage:

docctl Command-Line Tool
*************************

This page documents ``docctl``, an optional command-line helper (at the
qms-base repo root) that automates the commits described in
:ref:`sop/sop-docctl/review-and-approval-workflow`: setting the right
``.. doc_control::`` fields, committing with the correct subject line and
trailers, checking the ordering and segregation-of-duties rules, and
tagging the release. Using it is not required by :ref:`sop-docctl`:
performing the same steps by hand with plain ``git`` commands satisfies
the policy equally well. The tool exists purely to make the correct
outcome easier to reach and harder to get wrong.

Prerequisites
=============

- ``git config user.name`` / ``git config user.email`` configured —
  docctl reads these as the acting identity for the commit trailers.
- A configured GPG signing key — commits are made with ``git commit -s
  -S`` (signed-off and GPG-signed); an unconfigured signing key is a hard
  failure, not silently skipped.

Listing documents
==================

.. code-block:: console

   $ ./docctl.py list
   ptcc_kempert-volker_001
   sop-cybersec
   sop-docctl
   sop-impl
   sop-req_design
   sop-soupval
   sop-swdp
   sop-toolval
   sop-verif

Only document-ids that resolve to exactly one ``.. doc_control::``
directive are listed — the same set the ``author``/``review``/``approve``
subcommands can operate on.

Authoring
=========

.. code-block:: console

   $ ./docctl.py author sop-docctl --version 1.1

Sets ``:author:`` to the caller's identity (and ``:version:``, if
``--version`` is given), then commits with subject
``docs(sop-docctl): Author version 1.1`` and a ``Signed-off-by:``
trailer.

Review
======

.. code-block:: console

   $ ./docctl.py review sop-docctl

Refuses to run unless ``:author:`` is already set (i.e. ``author`` ran
first) and — segregation of duties — refuses if the commit that set
``:author:`` was made by the same person now running ``review``
(identified by committer e-mail, via ``git blame`` on that field). Pass
``--force`` to override either check. On success, sets ``:reviewed_by:``
and commits with subject ``docs(sop-docctl): Review version <version>``,
a ``Signed-off-by:`` and a ``Reviewed-by:`` trailer.

Approval
========

.. code-block:: console

   $ ./docctl.py approve sop-docctl --effective-date 2026-08-01

Refuses to run unless ``:reviewed_by:`` is set *and* backed by an actual
commit (not just a value typed into the file). Pass ``--force`` to
override. On success, sets ``:approved_by:`` and ``:approval_date:`` (and
``:effective_date:``, if given), commits with subject
``docs(sop-docctl): Approve version <version>`` and an ``Approved-by:``
trailer, then creates a signed tag ``sop-docctl/<version>`` on that
commit — see :ref:`sop/sop-docctl/released-versions`.

Bumping to a new version
=========================

.. code-block:: console

   $ ./docctl.py bump-version sop-docctl --minor
   $ ./docctl.py bump-version sop-docctl --major

Starts a new version cycle for an already-released document — see
:ref:`sop/sop-docctl/starting-an-updated-version`. Refuses if the
document is classified as a Record (Records use their own
edition-per-folder versioning, not major.minor). ``--minor`` (the
default) bumps ``x.Y`` -> ``x.Y+1``; ``--major`` bumps ``X.y`` ->
``X+1.0``. On success:

- sets ``:version:`` to the new version;
- removes ``:author:``, ``:reviewed_by:``, ``:approved_by:`` and
  ``:approval_date:`` from the ``.. doc_control::`` directive entirely
  (not just blanks them), so doc_control.py's own "not-authored-yet" /
  "not-reviewed-yet" / "not-approved-yet" placeholders take over until
  the new version is actually authored/reviewed/approved again;
- if a release tag ``<document-id>/<old version>`` exists, sets the
  document's ``.. git_changelog::`` directive's ``:rev-list:`` to
  ``<document-id>/<old version>..HEAD``, so the rendered change history
  covers only this new version's commits;
- commits everything with subject
  ``docs(sop-docctl): Bump version to <new version>`` and a
  ``Signed-off-by:`` trailer.

Registry resolution
====================

By default, ``docctl`` resolves document-ids against ``documents.yaml``
at the qms-base repo root (next to the script). Pass ``--registry`` to
point it at a different registry file.
