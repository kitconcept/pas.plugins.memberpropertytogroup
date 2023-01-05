"""Setup tests for this package."""
import pytest


PACKAGE_NAME = "pas.plugins.memberpropertytogroup"


class TestSetupUninstall:
    @pytest.fixture(autouse=True)
    def uninstall(self, installer):
        installer.uninstall_product(PACKAGE_NAME)

    def test_product_uninstalled(self, installer):
        """Test if pas.plugins.memberpropertytogroup is uninstalled."""
        assert installer.is_product_installed(PACKAGE_NAME) is False

    def test_browserlayer_removed(self, browser_layers):
        """Test that IPasPluginsMemberpropertytogroupLayer is removed."""
        from pas.plugins.memberpropertytogroup import interfaces as ifaces

        assert ifaces.IPasPluginsMemberpropertytogroupLayer not in browser_layers

    def test_configlet_removed(self, controlpanel_actions):
        """Test if control panel is installed."""
        assert "memberpropertytogroup" not in controlpanel_actions
