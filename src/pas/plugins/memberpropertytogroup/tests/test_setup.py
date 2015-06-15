# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MEMBERPROPERTYTOGROUP_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that pas.plugins.memberpropertytogroup is properly installed."""

    layer = PAS_PLUGINS_MEMBERPROPERTYTOGROUP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pas.plugins.memberpropertytogroup is installed with
           portal_quickinstaller.
        """
        self.assertTrue(
            self.installer.isProductInstalled(
                'pas.plugins.memberpropertytogroup'
            )
        )

    def test_uninstall(self):
        """Test if pas.plugins.memberpropertytogroup is cleanly uninstalled."""
        self.installer.uninstallProducts(['pas.plugins.memberpropertytogroup'])
        self.assertFalse(
            self.installer.isProductInstalled(
                'pas.plugins.memberpropertytogroup'
            )
        )

    def test_browserlayer(self):
        """Test that IPasPluginsMemberpropertytogroupLayer is registered."""
        from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupLayer  # noqa
        from plone.browserlayer import utils
        self.assertTrue(
            IPasPluginsMemberpropertytogroupLayer in utils.registered_layers()
        )
