"""Setup tests for this package."""
import pytest


PACKAGE_NAME = "pas.plugins.memberpropertytogroup"


@pytest.fixture
def uninstall(installer):
    installer.uninstall_product(PACKAGE_NAME)


def test_product_installed(installer):
    """Test if pas.plugins.memberpropertytogroup is installed."""
    assert installer.is_product_installed(PACKAGE_NAME) is True


def test_browserlayer(browser_layers):
    """Test that IPasPluginsMemberpropertytogroupLayer is registered."""
    from pas.plugins.memberpropertytogroup import interfaces as ifaces

    assert ifaces.IPasPluginsMemberpropertytogroupLayer in browser_layers


def test_configlet_install(controlpanel_actions):
    """Test if control panel is installed."""
    assert "memberpropertytogroup" in controlpanel_actions


def test_product_uninstalled(uninstall, installer):
    """Test if pas.plugins.memberpropertytogroup is uninstalled."""
    assert installer.is_product_installed(PACKAGE_NAME) is False


def test_browserlayer_removed(uninstall, browser_layers):
    """Test that IPasPluginsMemberpropertytogroupLayer is removed."""
    from pas.plugins.memberpropertytogroup import interfaces as ifaces

    assert ifaces.IPasPluginsMemberpropertytogroupLayer not in browser_layers


def test_configlet_removed(uninstall, controlpanel_actions):
    """Test if control panel is installed."""
    assert "memberpropertytogroup" not in controlpanel_actions
