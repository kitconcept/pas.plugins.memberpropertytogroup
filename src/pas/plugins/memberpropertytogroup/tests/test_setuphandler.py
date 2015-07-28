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
        from pas.plugins.memberpropertytogroup.setuphandlers import _add_plugin
        result = _add_plugin(self.aclu, pluginid=PLUGINID)
        self.assertIs(result, None)
        self.assertIn(PLUGINID, self.aclu.objectIds())

        from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
        mptg = self.aclu[PLUGINID]
        self.assertIsInstance(mptg, MPTGPlugin)

        from pas.plugins.memberpropertytogroup.setuphandlers import TITLE
        result = _add_plugin(self.aclu, pluginid=PLUGINID)
        self.assertEqual(result, TITLE + ' already installed.')

    def test_removeplugin(self):
        # add before remove
        PLUGINID = 'mptg'
        from pas.plugins.memberpropertytogroup.setuphandlers import _add_plugin
        _add_plugin(self.aclu, pluginid=PLUGINID)
        self.assertIn(PLUGINID, self.aclu.objectIds())

        # now remove it
        from pas.plugins.memberpropertytogroup.setuphandlers import _remove_plugin  # noqa
        _remove_plugin(self.aclu, pluginid=PLUGINID)
        self.assertNotIn(PLUGINID, self.aclu.objectIds())
