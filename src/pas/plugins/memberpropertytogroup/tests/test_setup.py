# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING  # noqa
from Products.CMFCore.utils import getToolByName

import unittest


class TestSetup(unittest.TestCase):
    """Test that pas.plugins.memberpropertytogroup is properly installed."""

    layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """Test if pas.plugins.memberpropertytogroup is installed with
           portal_quickinstaller.
        """
        self.assertTrue(
            self.installer.isProductInstalled(
                'pas.plugins.memberpropertytogroup'
            )
        )
        self.assertIn('memberpropertytogroup', self.portal.acl_users)

    def test_uninstall(self):
        """Test if pas.plugins.memberpropertytogroup is cleanly uninstalled."""
        self.installer.uninstallProducts(['pas.plugins.memberpropertytogroup'])
        self.assertFalse(
            self.installer.isProductInstalled(
                'pas.plugins.memberpropertytogroup'
            )
        )
        # self.assertNotIn('memberpropertytogroup', self.portal.acl_users)

    def test_browserlayer(self):
        """Test that IPasPluginsMemberpropertytogroupLayer is registered."""
        from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupLayer  # noqa
        from plone.browserlayer import utils
        self.assertTrue(
            IPasPluginsMemberpropertytogroupLayer in utils.registered_layers()
        )
