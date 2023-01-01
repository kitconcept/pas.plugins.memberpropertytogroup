from pas.plugins.memberpropertytogroup.plugin import manage_addMPTGPlugin
from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
from Products.PluggableAuthService.PropertiedUser import PropertiedUser

import pytest


PLUGINID = "mptg"


@pytest.fixture
def plugin(aclu):
    manage_addMPTGPlugin(aclu, PLUGINID)
    return aclu[PLUGINID]


@pytest.fixture
def mock_user():
    mock_user = PropertiedUser("mockuser")
    mock_user.addPropertysheet(
        "testsheet",
        {"testproperty": "mockgroup"},
    )
    return mock_user


@pytest.fixture
def property_key(mocker):
    mocked = mocker.patch.object(MPTGPlugin, "_configured_property", autospec=True)
    mocked.return_value = "testproperty"
    return mocked


@pytest.fixture
def sheet_plugins(mocker, mock_user):
    mocked = mocker.patch.object(
        MPTGPlugin, "_sheet_plugins_of_principal", autospec=True
    )

    # mock sheets provider
    class MockProvider:
        def getPropertiesForUser(self, principal):
            return mock_user._propertysheets["testsheet"]

    mocked.return_value = {"testsheet": MockProvider()}
    return mocked


def test_group_property_of_principal(plugin, mock_user, property_key, sheet_plugins):
    value = plugin._group_property_of_principal(mock_user, 0)
    assert value == "mockgroup"


@pytest.mark.parametrize(
    "prop,match",
    [
        ("foo", "foo"),
        ("foobar", "foo*"),
        ("foo", "foo*"),
        ("foo", "*foo*"),
        ("foo", "*foo"),
        ("foa", "*fo[ao]"),
        ("foab", "*fo[ao]*"),
        ("foobar", "*bar*"),
    ],
)
def test_is_property_match_equals(plugin, prop, match):
    assert plugin._is_property_match(prop, match) is True


def test_is_property_match_NoneType(plugin):
    assert plugin._is_property_match(None, "123*") is False
