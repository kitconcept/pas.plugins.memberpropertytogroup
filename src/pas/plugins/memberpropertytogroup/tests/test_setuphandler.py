# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MPTG_ZOPE_FIXTURE  # noqa

import unittest


class TestPluginForGroupCapability(unittest.TestCase):
    """interface plonepas_interfaces.capabilities.IGroupCapability

    Test if above interface works as expected
    """

    layer = PAS_PLUGINS_MPTG_ZOPE_FIXTURE

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.aclu = self.layer['app'].acl_users

    def test_addplugin(self):
        PLUGINID = 'mptg'
        from pas.plugins.memberpropertytogroup.setuphandlers import _addPlugin
        result = _addPlugin(self.aclu, pluginid=PLUGINID)
        self.assertIs(result, None)
        self.assertIn(PLUGINID, self.aclu.objectIds())

        from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
        mptg = self.aclu[PLUGINID]
        self.assertIsInstance(mptg, MPTGPlugin)

        from pas.plugins.memberpropertytogroup.setuphandlers import TITLE
        result = _addPlugin(self.aclu, pluginid=PLUGINID)
        self.assertEqual(result, TITLE + ' already installed.')

