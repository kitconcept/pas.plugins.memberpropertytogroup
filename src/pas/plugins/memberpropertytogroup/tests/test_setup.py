"""Setup tests for this package."""
from pas.plugins.memberpropertytogroup.testing import (
    PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING,
)  # noqa
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that pas.plugins.memberpropertytogroup is properly installed."""

    layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if pas.plugins.memberpropertytogroup is installed."""
        self.assertTrue(
            self.installer.is_product_installed("pas.plugins.memberpropertytogroup")
        )

    def test_browserlayer(self):
        """Test that IPasPluginsMemberpropertytogroupLayer is registered."""
        from pas.plugins.memberpropertytogroup.interfaces import (
            IPasPluginsMemberpropertytogroupLayer,
        )  # noqa
        from plone.browserlayer import utils

        self.assertIn(IPasPluginsMemberpropertytogroupLayer, utils.registered_layers())

    def test_configlet_install(self):
        """Test if control panel is installed."""
        controlpanel = self.portal.portal_controlpanel
        installed = [a.getAction(self)["id"] for a in controlpanel.listActions()]
        self.assertTrue("memberpropertytogroup" in installed)


class TestUninstall(unittest.TestCase):

    layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)
        self.installer.uninstall_product("pas.plugins.memberpropertytogroup")

    def test_product_uninstalled(self):
        self.assertFalse(
            self.installer.is_product_installed("pas.plugins.memberpropertytogroup")
        )

    def test_browserlayer_removed(self):
        """Test that IPasPluginsMemberpropertytogroupLayer is removed."""
        from pas.plugins.memberpropertytogroup.interfaces import (
            IPasPluginsMemberpropertytogroupLayer,
        )  # noqa
        from plone.browserlayer import utils

        self.assertNotIn(
            IPasPluginsMemberpropertytogroupLayer, utils.registered_layers()
        )

    def test_configlet_removed(self):
        """Test if control panel is removed."""
        controlpanel = self.portal.portal_controlpanel
        installed = [a.getAction(self)["id"] for a in controlpanel.listActions()]
        self.assertFalse("memberpropertytogroup" in installed)
