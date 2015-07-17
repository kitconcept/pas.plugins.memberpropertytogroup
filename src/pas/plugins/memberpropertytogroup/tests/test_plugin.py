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


class TestPlugin(unittest.TestCase):

    layer = PAS_PLUGINS_MPTG_ZOPE_FIXTURE

    def setUp(self):
        # create plugin
        from pas.plugins.memberpropertytogroup.setuphandlers import _addPlugin
        self.aclu = self.layer['app'].acl_users
        _addPlugin(self.aclu, 'mptg')
        self.plugin = self.aclu['mptg']

        # mock property
        from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
        mock_group_property_of_principal = mock.patch.object(
            MPTGPlugin,
            '_group_property_of_principal',
            mock.Mock(wraps=MPTGPlugin._group_property_of_principal)
        )
        self.mocked_group_property_of_principal = mock_group_property_of_principal.start()  # noqa
        self.addCleanup(mock_group_property_of_principal.stop)

        # mock valid_groups
        mock_valid_groups = mock.patch.object(
            MPTGPlugin,
            '_valid_groups',
            mock.Mock(wraps=MPTGPlugin._valid_groups)
        )
        self.mocked_valid_groups = mock_valid_groups.start()
        self.addCleanup(mock_valid_groups.stop)

    def test_getGroupsForPrincipal(self):
        self.mocked_valid_groups.return_value = [
            ['prop1', 'group1', '', '', ''],
            ['prop2', 'group2', '', '', ''],
        ]
        self.mocked_group_property_of_principal.return_value = 'prop1'
        self.assertEqual(self.plugin.getGroupsForPrincipal(None), ('group1', ))

        self.mocked_group_property_of_principal.return_value = 'prop2'
        self.assertEqual(self.plugin.getGroupsForPrincipal(None), ('group2', ))

    def test_allowGroupAdd(self):
        self.assertFalse(self.plugin.allowGroupAdd('x', 'y'))

    def test_allowGroupRemove(self):
        self.assertFalse(self.plugin.allowGroupRemove('x', 'y'))

    def test_getGroupById(self):
        self.mocked_valid_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = ''
        group = self.plugin.getGroupById('group1')

        # id matches
        self.assertEqual('group1', group.getId())

        # username is Title
        self.assertEqual('title1', group.getUserName())

        # description, email are properties
        sheet = group.getPropertysheet(self.plugin.getId())
        self.assertIsNot(sheet, None)

    def test_getGroupIds(self):
        self.mocked_valid_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = ''
        self.assertEqual(self.plugin.getGroupIds(), ['group1', 'group2'])

    def test_getPropertiesForUser(self):
        self.mocked_valid_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = ''
        from Products.PluggableAuthService.interfaces.plugins import IPropertiesPlugin  # noqa
        plugin_ids = self.aclu.plugins.listPluginIds(IPropertiesPlugin)
        self.assertIn(self.plugin.getId(), plugin_ids)

    def test_enumerateGroups(self):
        self.mocked_valid_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = ''
        self.assertEqual(
            len(self.plugin.enumerateGroups(id='group')),
            2
        )
        self.assertEqual(
            len(self.plugin.enumerateGroups()),
            2
        )
        self.assertEqual(
            len(self.plugin.enumerateGroups(id='group1')),
            1
        )
        self.assertEqual(
            self.plugin.enumerateGroups(
                id='group1',
                exact_match=True
            )[0]['id'],
            'group1'
        )
        self.assertEqual(
            self.plugin.enumerateGroups(id='group', exact_match=True),
            []
        )
