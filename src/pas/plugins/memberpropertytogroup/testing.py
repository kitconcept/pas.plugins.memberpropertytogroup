# -*- coding: utf-8 -*-
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.utils import getToolByName
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import Layer
from plone.testing import z2
from zope.component import provideUtility

import pas.plugins.memberpropertytogroup

try:
    # plone 5.x with PlonePAS >=5.0
    from Products.PlonePAS.setuphandlers import migrate_root_uf
except ImportError:
    # plone 3.x and 4.x with PlonePAS <5.0
    from Products.PlonePAS.Extensions.Install import migrate_root_uf


class PasPluginsMPTGZopeLayer(Layer):

    defaultBases = (
        z2.INTEGRATION_TESTING,
    )

    # Products that will be installed, plus options
    products = (
        ('Products.GenericSetup', {'loadZCML': True}, ),
        ('Products.CMFCore', {'loadZCML': True}, ),
        ('Products.PluggableAuthService', {'loadZCML': True}, ),
        ('Products.PluginRegistry', {'loadZCML': True}, ),
        ('Products.PlonePAS', {'loadZCML': True}, ),
    )

    def setUp(self):
        self.setUpZCML()

    def testSetUp(self):
        self.setUpProducts()
        provideUtility(self['app'], provides=ISiteRoot)
        migrate_root_uf(self['app'])

    def setUpZCML(self):
        """Stack a new global registry and load ZCML configuration of Plone
        and the core set of add-on products into it.
        """

        # Load dependent products's ZCML
        from zope.configuration import xmlconfig
        from zope.dottedname.resolve import resolve

        def loadAll(filename):
            for p, config in self.products:
                if not config['loadZCML']:
                    continue
                try:
                    package = resolve(p)
                except ImportError:
                    continue
                try:
                    xmlconfig.file(
                        filename,
                        package,
                        context=self['configurationContext']
                    )
                except IOError:
                    pass

        loadAll('meta.zcml')
        loadAll('configure.zcml')
        loadAll('overrides.zcml')

    def setUpProducts(self):
        """Install all old-style products listed in the the ``products`` tuple
        of this class.
        """
        for prd, config in self.products:
            z2.installProduct(self['app'], prd)


PAS_PLUGINS_MPTG_ZOPE_FIXTURE = PasPluginsMPTGZopeLayer()


class PasPluginsMPTGPloneLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=pas.plugins.memberpropertytogroup)
        z2.installProduct(app, 'pas.plugins.memberpropertytogroup')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pas.plugins.memberpropertytogroup:default')

        # Create Folder type if it does not exist (for Plone 5)
        types_tool = getToolByName(portal, "portal_types")
        if 'Folder' not in types_tool.objectIds():
            from plone.dexterity.fti import DexterityFTI
            fti = DexterityFTI('Folder')
            types_tool._setObject('Folder', fti)

        # XXX: This is robot test specific setup code which should be
        memberdata_tool = getToolByName(portal, 'portal_memberdata')
        memberdata_tool.manage_addProperty(
            id='usertype',
            value='',
            type='string'
        )
        memberdata_tool.manage_addProperty(
            id='city',
            value='',
            type='string'
        )
        memberdata_tool.manage_addProperty(
            id='student_id',
            value='',
            type='string'
        )
        mtool = getToolByName(portal, 'portal_membership')
        member = mtool.getMemberById('test_user_1_')
        member.setMemberProperties(mapping={'usertype': 'employee'})
        member.setMemberProperties(mapping={'student_id': '1234567'})
        member.setMemberProperties(mapping={'city': 'bonn'})


PAS_PLUGINS_MPTG_PLONE_FIXTURE = PasPluginsMPTGPloneLayer()


PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PAS_PLUGINS_MPTG_PLONE_FIXTURE,),
    name='PasPluginsMPTGPloneLayer:IntegrationTesting'
)


PAS_PLUGINS_MPTG_PLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PAS_PLUGINS_MPTG_PLONE_FIXTURE,),
    name='PasPluginsMPTGPloneLayer:FunctionalTesting'
)


PAS_PLUGINS_MPTG_PLONE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PAS_PLUGINS_MPTG_PLONE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PasPluginsMPTGPloneLayer:AcceptanceTesting'
)
