"""Setup tests for this package."""
import pytest


PACKAGE_NAME = "pas.plugins.memberpropertytogroup"


@pytest.fixture
def uninstall(installer):
    installer.uninstall_product(PACKAGE_NAME)


@pytest.fixture
def cp_actions(portal):
    controlpanel = portal.portal_controlpanel
    return [a.getAction(portal)["id"] for a in controlpanel.listActions()]


def test_product_installed(installer):
    """Test if pas.plugins.memberpropertytogroup is installed."""
    assert installer.is_product_installed(PACKAGE_NAME) is True


def test_browserlayer(browser_layers):
    """Test that IPasPluginsMemberpropertytogroupLayer is registered."""
    from pas.plugins.memberpropertytogroup import interfaces as ifaces

    assert ifaces.IPasPluginsMemberpropertytogroupLayer in browser_layers


def test_configlet_install(cp_actions):
    """Test if control panel is installed."""
    assert "memberpropertytogroup" in cp_actions


def test_product_uninstalled(uninstall, installer):
    """Test if pas.plugins.memberpropertytogroup is uninstalled."""
    assert installer.is_product_installed(PACKAGE_NAME) is False


def test_browserlayer_removed(uninstall, browser_layers):
    """Test that IPasPluginsMemberpropertytogroupLayer is removed."""
    from pas.plugins.memberpropertytogroup import interfaces as ifaces

    assert ifaces.IPasPluginsMemberpropertytogroupLayer not in browser_layers


def test_configlet_removed(uninstall, cp_actions):
    """Test if control panel is installed."""
    assert "memberpropertytogroup" not in cp_actions
