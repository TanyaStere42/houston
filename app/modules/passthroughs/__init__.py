# -*- coding: utf-8 -*-
"""
Passthroughs module
============
"""

from app.extensions.api import api_v1

from app.modules import is_module_enabled

if not is_module_enabled('passthroughs'):
    raise RuntimeError('Passthroughs is not enabled')


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-variable
    """
    Init Passthroughs module.
    """
    api_v1.add_oauth_scope(
        'passthroughs:read', 'Provide access to EDM and ACM passthroughs'
    )
    api_v1.add_oauth_scope(
        'passthroughs:write', 'Provide write access to EDM and ACM passthroughs'
    )

    # Touch underlying modules
    from . import resources  # NOQA

    api_v1.add_namespace(resources.edm_pass)
