# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MPTG_ZOPE_FIXTURE  # noqa
import mock
import unittest


class TestPluginHelpers(unittest.TestCase):
    """check if helpers work
    """

    layer = PAS_PLUGINS_MPTG_ZOPE_FIXTURE

    def setUp(self):
        """Custom shared utility setup for tests."""
        # create plugin
        from pas.plugins.memberpropertytogroup.plugin import manage_addMPTGPlugin  # noqa
        self.aclu = self.layer['app'].acl_users
        manage_addMPTGPlugin(self.aclu, 'mptg')
        self.plugin = self.aclu['mptg']

        # mock property
        from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
        mock_property_key = mock.patch.object(
            MPTGPlugin,
            '_configured_property',
            mock.Mock(wraps=MPTGPlugin._configured_property)
        )
        self.mocked_property_key = mock_property_key.start()
        self.addCleanup(mock_property_key.stop)

        mock_sheets_plugins = mock.patch.object(
            MPTGPlugin,
            '_sheet_plugins_of_principal',
            mock.Mock(wraps=MPTGPlugin._sheet_plugins_of_principal)
        )
        self.mocked_sheet_plugins = mock_sheets_plugins.start()
        self.addCleanup(mock_sheets_plugins.stop)

    def test_group_property_of_principal(self):
        # mock a user with sheet
        from Products.PluggableAuthService.PropertiedUser import PropertiedUser
        mock_user = PropertiedUser('mockuser')
        mock_user.addPropertysheet(
            'testsheet',
            {'testproperty': 'mockgroup'},
        )
        self.mocked_property_key.return_value = 'testproperty'

        # mock sheets provider
        class MockProvider(object):
            def getPropertiesForUser(self, principal):
                return mock_user._propertysheets['testsheet']

        self.mocked_sheet_plugins.return_value = {
            'testsheet': MockProvider()
        }

        value = self.plugin._group_property_of_principal(mock_user)
        self.assertEqual(value, 'mockgroup')


class TestGroupPlugin(unittest.TestCase):
    """interface pas_interfaces.plugin.IGroupPlugin

    Test if above interface works as expected
    """



