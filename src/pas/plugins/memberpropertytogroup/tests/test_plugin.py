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

    def test_something(self):
        pass
