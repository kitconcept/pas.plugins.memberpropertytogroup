# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import pas.plugins.memberpropertytogroup


class PasPluginsMemberpropertytogroupLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=pas.plugins.memberpropertytogroup)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pas.plugins.memberpropertytogroup:default')


PAS_PLUGINS_MEMBERPROPERTYTOGROUP_FIXTURE = PasPluginsMemberpropertytogroupLayer()


PAS_PLUGINS_MEMBERPROPERTYTOGROUP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PAS_PLUGINS_MEMBERPROPERTYTOGROUP_FIXTURE,),
    name='PasPluginsMemberpropertytogroupLayer:IntegrationTesting'
)


PAS_PLUGINS_MEMBERPROPERTYTOGROUP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PAS_PLUGINS_MEMBERPROPERTYTOGROUP_FIXTURE,),
    name='PasPluginsMemberpropertytogroupLayer:FunctionalTesting'
)


PAS_PLUGINS_MEMBERPROPERTYTOGROUP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PAS_PLUGINS_MEMBERPROPERTYTOGROUP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PasPluginsMemberpropertytogroupLayer:AcceptanceTesting'
)
