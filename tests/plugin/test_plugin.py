from pas.plugins.memberpropertytogroup.interfaces import IGetGroupMembers
from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
from Products.PluggableAuthService.interfaces.plugins import IPropertiesPlugin
from zope.component import queryUtility

import pytest


@pytest.fixture
def group_members_utility(zope):
    def func():
        return queryUtility(IGetGroupMembers)

    return func


@pytest.fixture
def valid_groups(mocker):
    mocked = mocker.patch.object(MPTGPlugin, "_valid_groups", autospec=True)
    return mocked


@pytest.fixture
def group_property_of_principal(mocker):
    mocked = mocker.patch.object(
        MPTGPlugin, "_group_property_of_principal", autospec=True
    )
    return mocked


@pytest.fixture
def get_all_groups(mocker):
    mocked = mocker.patch.object(MPTGPlugin, "_get_all_groups", autospec=True)
    return mocked


def test_getGroupsForPrincipal(plugin, valid_groups, group_property_of_principal):
    valid_groups.side_effect = [
        [["prop1", "group1", "", "", ""], ["prop2", "group2", "", "", ""]],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    group_property_of_principal.return_value = "prop1"

    assert plugin.getGroupsForPrincipal(None) == ("group1",)

    valid_groups.side_effect = [
        [["prop1", "group1", "", "", ""], ["prop2", "group2", "", "", ""]],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    group_property_of_principal.return_value = "prop2"
    assert plugin.getGroupsForPrincipal(None) == ("group2",)


def test_allowGroupAdd(plugin):
    assert plugin.allowGroupAdd("x", "y") is False


def test_allowGroupRemove(plugin):
    assert plugin.allowGroupRemove("x", "y") is False


def test_getGroupById(
    plugin, valid_groups, get_all_groups, group_property_of_principal
):
    valid_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    get_all_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    group_property_of_principal.return_value = ""
    group = plugin.getGroupById("group2")

    # id matches
    assert group.getId() == "group2"

    # username is Title
    assert group.getUserName() == "title2"

    # description, email are properties
    sheet = group.getPropertysheet(plugin.getId())
    assert sheet is not None


def test_getGroupIds(plugin, get_all_groups, group_property_of_principal):
    get_all_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    group_property_of_principal.return_value = ""
    assert plugin.getGroupIds() == ["group1", "group2"]


def test_getGroups(plugin, valid_groups, get_all_groups, group_property_of_principal):
    valid_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    get_all_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    group_property_of_principal.return_value = ""
    groups = [group for group in plugin.getGroups()]
    assert len(groups) == 2


def test_getPropertiesForUser(aclu, plugin, valid_groups, group_property_of_principal):
    valid_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    group_property_of_principal.return_value = ""
    plugin_ids = aclu.plugins.listPluginIds(IPropertiesPlugin)
    assert plugin.getId() in plugin_ids


def test_enumerateGroups(plugin, get_all_groups, group_property_of_principal):
    get_all_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    group_property_of_principal.return_value = ""
    assert len(plugin.enumerateGroups(id="group")) == 2
    assert len(plugin.enumerateGroups()) == 2
    assert len(plugin.enumerateGroups(id="group1")) == 1
    first_group_id = plugin.enumerateGroups(id="group1", exact_match=True)[0]["id"]
    assert first_group_id == "group1"
    assert plugin.enumerateGroups(id="group", exact_match=True) == []


def test_get_group_members(
    plugin, group_members_utility, valid_groups, group_property_of_principal
):
    # there is no utility be default providing the group members
    assert group_members_utility() is None

    # mock group and user with such an group
    valid_groups.return_value = [
        ["prop1", "group1", "title1", "descr1", "email1"],
        ["prop2", "group2", "title2", "descr2", "email2"],
    ]
    group_property_of_principal.return_value = "prop2"

    # by default no utility for group members fetching is present
    assert plugin.getGroupMembers("prop2") == ()

    # provide a utility and lets see if it get used
    from zope.component import provideUtility  # noqa

    def fake_group_provider(plugin, group_id):
        return ("fakeuser",)

    provideUtility(fake_group_provider, provides=IGetGroupMembers)
    assert group_members_utility() is fake_group_provider

    assert plugin.getGroupMembers("prop2") == ("fakeuser",)
