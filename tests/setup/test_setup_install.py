"""Setup tests for this package."""


PACKAGE_NAME = "pas.plugins.memberpropertytogroup"


class TestSetupInstall:
    def test_product_installed(self, installer):
        """Test if pas.plugins.memberpropertytogroup is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IPasPluginsMemberpropertytogroupLayer is registered."""
        from pas.plugins.memberpropertytogroup import interfaces as ifaces

        assert ifaces.IPasPluginsMemberpropertytogroupLayer in browser_layers

    def test_configlet_install(self, controlpanel_actions):
        """Test if control panel is installed."""
        assert "memberpropertytogroup" in controlpanel_actions
