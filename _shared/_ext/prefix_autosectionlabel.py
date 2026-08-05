# Copyright (c) 2026 TiaC Systems
# SPDX-License-Identifier: Apache-2.0
"""
Custom autosectionlabel extension with configurable prefix.

Registers sections as labels with a configurable prefix and normalized document names.

Configuration
=============

- ``autosectionlabel_prefix``: The prefix to prepend to all generated labels (default: 'section')
- ``autosectionlabel_prefix_document``: If True, include normalized document name in the label

Example
=======

Given a document ``sop/sop-docctl.rst`` with configuration:

    autosectionlabel_prefix = 'qms'
    autosectionlabel_prefix_document = True

A section titled "References" will be labeled as: ``qms_sop_docctl:References``

To link to this section from anywhere in the documentation, use:

    :ref:`qms_sop_docctl:References`
"""

from docutils import nodes
from sphinx.ext.autosectionlabel import get_node_depth
from sphinx.util.nodes import clean_astext


def prefix_register_sections_as_label(app, document):
    """Register document sections as labels with configurable prefix."""
    prefix = app.config.autosectionlabel_prefix
    domain = app.env.domains.standard_domain
    for node in document.findall(nodes.section):
        if (
            app.config.autosectionlabel_maxdepth
            and get_node_depth(node) >= app.config.autosectionlabel_maxdepth
        ):
            continue
        labelid = node['ids'][0]
        docname = app.env.current_document.docname
        title = node[0]
        ref_name = getattr(title, 'rawsource', title.astext())
        normalized_docname = docname.replace('/', '_')
        if app.config.autosectionlabel_prefix_document:
            base_name = f"{prefix}_{normalized_docname}:{ref_name}"
        else:
            base_name = f"{prefix}_{ref_name}"
        name = nodes.fully_normalize_name(base_name)
        if name in domain.labels:
            name = nodes.fully_normalize_name(f"{base_name}:{labelid}")
        sectname = clean_astext(title)

        domain.anonlabels[name] = docname, labelid
        domain.labels[name] = docname, labelid, sectname


def setup(app):
    """Set up the prefix autosectionlabel extension."""
    # Register base autosectionlabel config values
    app.add_config_value(
        'autosectionlabel_maxdepth',
        default=None,
        rebuild='env',
        types=(int, type(None))
    )
    app.add_config_value(
        'autosectionlabel_prefix_document',
        default=False,
        rebuild='env',
        types=bool
    )
    # Register custom prefix config value
    app.add_config_value(
        'autosectionlabel_prefix',
        default='section',
        rebuild='env',
        types=str
    )
    # Connect to the doctree-read event to register sections
    app.connect('doctree-read', prefix_register_sections_as_label)
    return {
        'version': '0.2.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
