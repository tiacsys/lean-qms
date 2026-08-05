Lean QMS for Medical Software
*****************************


This website is the **viewpoint of effective versions** of software related SOP's.

The **document control** is done in a git repository. The git repository is
`Software relevant SOP's <https://github.com/almedso/lean-qms-medsw>`_
If you lack appropriate access ask the responsible person
`Volker Kempert <mailto:volker.kempert@almedso.de>`.


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

   flowchart LR
       A["SOP's in git<br><small style='color:gray'>Rst- files</small>"]
       B["SOP's on web<br><small style='color:gray'>Linked html pages</small>"]
       A e1@-->|rendered</small>| B


The concpet of organizing controlled documents as required by ISO 62304 can
found at :doc:`overview`.

Software SOPs
=============

Each SOP is built and released as its own controlled document (one PDF per
SOP). Use the *Documents* switcher in the sidebar to jump directly into a
specific SOP, or follow the tiles / links below:

.. container:: grid

   .. container:: grid-item

      :ref:`Doc Control <sop-docctl:sop-docctl>`

   .. container:: grid-item

      :ref:`Sw Development <sop-swdp:sop-swdp>`

   .. container:: grid-item

      :ref:`Req & Design <sop-req_design:sop-req_design>`

   .. container:: grid-item

      :ref:`Implementation <sop-impl:sop-impl>`

   .. container:: grid-item

      :ref:`Verification <sop-verif:sop-verif>`

   .. container:: grid-item

      :ref:`Cybersecurity <sop-cybersec:sop-cybersec>`

   .. container:: grid-item

      :ref:`Tool Validation <sop-toolval:sop-toolval>`

   .. container:: grid-item

      :ref:`SouP Validation <sop-soupval:sop-soupval>`

- :ref:`sop-docctl:sop-docctl` — Software Lifecycle Documentation Control Procedure
- :ref:`sop-swdp:sop-swdp` — SOP-Software — Software Development Procedure
- :ref:`sop-req_design:sop-req_design` — SOP — Software Requirement and Design Procedure
- :ref:`sop-impl:sop-impl` — SOP-Software — Implementation Procedure
- :ref:`sop-verif:sop-verif` — SOP-Software — Verification Procedure
- :ref:`sop-cybersec:sop-cybersec` — SOP-Software — Cybersecurity Procedures
- :ref:`sop-toolval:sop-toolval` — SOP-Software — Tool Validation Procedure
- :ref:`sop-soupval:sop-soupval` — SOP-Software of Unknown Provenance Validation Procedure

Each SOP's document-specific templates are published as an HTML-only
appendix of that SOP's own document (not part of the PDF). The
cross-cutting compliance-record template below applies across all SOPs.
