from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.testing.z2 import Browser
import unittest2 as unittest

from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName

from plone.registry import Registry

from plone.app.testing import logout

from pas.plugins.memberpropertytogroup.testing import \
    PAS_PLUGINS_MEMBERPROPERTYTOGROUP_INTEGRATION_TESTING

from pas.plugins.memberpropertytogroup.interfaces import \
    IPasPluginsMemberpropertytogroupSettings


class TestMailchimpSettingsControlPanel(unittest.TestCase):

    layer = PAS_PLUGINS_MEMBERPROPERTYTOGROUP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.registry = Registry()
        self.registry.registerInterface(
            IPasPluginsMemberpropertytogroupSettings
        )

    def test_memberpropertytogroup_controlpanel_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="memberpropertytogroup-controlpanel")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_memberpropertytogroup_controlpanel_view_protected(self):
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(
            Unauthorized,
            self.portal.restrictedTraverse,
            '@@memberpropertytogroup-controlpanel'
        )

    def test_memberpropertytogroup_in_controlpanel(self):
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.failUnless(
            'memberpropertytogroup' in [
                a.getAction(self)['id']
                for a in self.controlpanel.listActions()
            ]
        )

    def test_record_example_field(self):
        record = self.registry.records[
            'pas.plugins.memberpropertytogroup.interfaces.' +
            'IPasPluginsMemberpropertytogroupSettings.example_field'
        ]
        self.assertTrue(
            'example_field' in IPasPluginsMemberpropertytogroupSettings
        )
        self.assertEquals(record.value, u"")


class ControlpanelFunctionalTest(unittest.TestCase):

    layer = PAS_PLUGINS_MEMBERPROPERTYTOGROUP_INTEGRATION_TESTING

    def setUp(self):
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal_url = self.portal.absolute_url()
        self.browser = Browser(app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            'Authorization',
            'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD),
        )

    def test_empty_form(self):
        self.browser.open(
            "%s/memberpropertytogroup-controlpanel" % self.portal_url
        )
        self.assertTrue(
            "Member Properties To Group Settings" in self.browser.contents
        )
