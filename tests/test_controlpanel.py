from AccessControl import Unauthorized
from pas.plugins.memberpropertytogroup import interfaces as ifaces
from plone import api
from plone.app.testing import logout
from plone.registry import Registry

import pytest


@pytest.fixture
def anon_portal(portal):
    logout()
    return portal


@pytest.fixture
def registry(portal):
    registry = Registry()
    registry.registerInterface(ifaces.IPasPluginsMemberpropertytogroupSettings)
    return registry


def test_validator(portal):
    from zope.interface import Invalid

    with pytest.raises(Invalid):
        ifaces.validate_valid_groups(["1"])
    with pytest.raises(Invalid):
        ifaces.validate_valid_groups(["1|2|3|4|5|6"])


def test_memberpropertytogroup_controlpanel_view(portal, http_request):
    view = api.content.get_view(
        "memberpropertytogroup-controlpanel", portal, http_request
    )
    assert view is not None


def test_memberpropertytogroup_controlpanel_view_protected(anon_portal):
    with pytest.raises(Unauthorized):
        anon_portal.restrictedTraverse("@@memberpropertytogroup-controlpanel")


def test_memberpropertytogroup_in_controlpanel(portal):
    controlpanel = api.portal.get_tool("portal_controlpanel")
    assert "memberpropertytogroup" in [
        a.getAction(portal)["id"] for a in controlpanel.listActions()
    ]


def test_record_group_property(registry):
    record = registry.records[
        "pas.plugins.memberpropertytogroup.interfaces."
        "IPasPluginsMemberpropertytogroupSettings.group_property"
    ]
    assert "group_property" in ifaces.IPasPluginsMemberpropertytogroupSettings
    assert record.value == ""


def test_record_valid_groups(registry):
    record = registry.records[
        "pas.plugins.memberpropertytogroup.interfaces."
        "IPasPluginsMemberpropertytogroupSettings.valid_groups"
    ]
    assert "valid_groups" in ifaces.IPasPluginsMemberpropertytogroupSettings
    assert record.value == []
