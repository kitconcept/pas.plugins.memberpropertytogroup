from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING  # noqa
from plone.app.testing import logout
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.registry import Registry
from plone.testing.z2 import Browser
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter

import unittest


class TestPasPluginsMemberpropertyToGoupControlPanel(unittest.TestCase):

    layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.registry = Registry()
        self.registry.registerInterface(IPasPluginsMemberpropertytogroupSettings)

    def test_validator(self):
        from pas.plugins.memberpropertytogroup.interfaces import validate_valid_groups  # noqa
        from zope.interface import Invalid

        with self.assertRaises(Invalid):
            validate_valid_groups(["1"])
        with self.assertRaises(Invalid):
            validate_valid_groups(["1|2|3|4|5|6"])

    def test_memberpropertytogroup_controlpanel_view(self):
        view = getMultiAdapter(
            (self.portal, self.portal.REQUEST),
            name="memberpropertytogroup-controlpanel",
        )
        self.assertTrue(view())

    def test_memberpropertytogroup_controlpanel_view_protected(self):
        from AccessControl import Unauthorized

        logout()
        self.assertRaises(
            Unauthorized,
            self.portal.restrictedTraverse,
            "@@memberpropertytogroup-controlpanel",
        )

    def test_memberpropertytogroup_in_controlpanel(self):
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.assertTrue(
            "memberpropertytogroup"
            in [a.getAction(self)["id"] for a in self.controlpanel.listActions()]
        )

    def test_record_group_property(self):
        record = self.registry.records[
            "pas.plugins.memberpropertytogroup.interfaces."
            + "IPasPluginsMemberpropertytogroupSettings.group_property"
        ]
        self.assertTrue("group_property" in IPasPluginsMemberpropertytogroupSettings)
        self.assertEquals(record.value, "")

    def test_record_valid_groups(self):
        record = self.registry.records[
            "pas.plugins.memberpropertytogroup.interfaces."
            + "IPasPluginsMemberpropertytogroupSettings.valid_groups"
        ]
        self.assertTrue("valid_groups" in IPasPluginsMemberpropertytogroupSettings)
        self.assertEquals(record.value, [])


class ControlpanelFunctionalTest(unittest.TestCase):

    layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

    def setUp(self):
        app = self.layer["app"]
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.portal_url = self.portal.absolute_url()
        self.browser = Browser(app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            "Authorization",
            f"Basic {SITE_OWNER_NAME}:{SITE_OWNER_PASSWORD}",
        )

    def test_empty_form(self):
        self.browser.open("%s/memberpropertytogroup-controlpanel" % self.portal_url)
        self.assertTrue("Member Properties To Group Settings" in self.browser.contents)
