# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING  # noqa
from plone import api

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:  # Plone < 5.1
    HAS_INSTALLER = False
else:
    HAS_INSTALLER = True

import unittest


class TestSetup(unittest.TestCase):
    """Test that pas.plugins.memberpropertytogroup is properly installed."""

    layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if HAS_INSTALLER:
            self.installer = get_installer(self.portal)
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pas.plugins.memberpropertytogroup is installed."""
        if HAS_INSTALLER:
            self.assertTrue(
                self.installer.is_product_installed(
                    'pas.plugins.memberpropertytogroup')
            )
        else:
            self.assertTrue(
                self.installer.isProductInstalled(
                    'pas.plugins.memberpropertytogroup'
                )
            )

    def test_browserlayer(self):
        """Test that IPasPluginsMemberpropertytogroupLayer is registered."""
        from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupLayer  # noqa
        from plone.browserlayer import utils
        self.assertIn(IPasPluginsMemberpropertytogroupLayer,
                      utils.registered_layers())


# class TestUninstall(unittest.TestCase):

#     layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

#     def setUp(self):
#         self.portal = self.layer['portal']
#         if HAS_INSTALLER:
#             self.installer = get_installer(self.portal)
#             self.installer.uninstall_product(
#                 'pas.plugins.memberpropertytogroup')
#         else:
#             self.installer = api.portal.get_tool('portal_quickinstaller')
#             self.installer.uninstallProducts(
#                 ['pas.plugins.memberpropertytogroup'])

#     def test_product_uninstalled(self):
#         if HAS_INSTALLER:
#             self.assertFalse(
#                 self.installer.is_product_installed(
#                     'pas.plugins.memberpropertytogroup')
#             )
#         else:
#             self.assertFalse(
#                 self.installer.isProductInstalled(
#                     'pas.plugins.memberpropertytogroup'
#                 )
#             )

#     def test_browserlayer_removed(self):
#         """Test that IPasPluginsMemberpropertytogroupLayer is removed."""
#         from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupLayer  # noqa
#         from plone.browserlayer import utils
#         self.assertNotIn(IPasPluginsMemberpropertytogroupLayer,
#                          utils.registered_layers())
