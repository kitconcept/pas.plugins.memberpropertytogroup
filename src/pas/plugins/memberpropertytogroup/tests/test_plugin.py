# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MPTG_ZOPE_FIXTURE  # noqa
from pas.plugins.memberpropertytogroup.testing import PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING  # noqa
from plone.registry import Registry
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

        value = self.plugin._group_property_of_principal(mock_user, 0)
        self.assertEqual(value, 'mockgroup')

    def test_is_property_match_equals(self):
        TESTS_EQUAL = [
            ('foo', 'foo'),
            ('foobar', 'foo*'),
            ('foo', 'foo*'),
        ]
        for prop, match in TESTS_EQUAL:
            self.assertTrue(
                self.plugin._is_property_match(prop, match),
                'Problem with pair prop=' + prop + ', match=' + match
            )

    def test_is_property_match_NoneType(self):
        self.assertFalse(
            self.plugin._is_property_match(None, '123*'),
        )


class TestPlugin(unittest.TestCase):

    layer = PAS_PLUGINS_MPTG_ZOPE_FIXTURE

    def setUp(self):
        # create plugin
        from pas.plugins.memberpropertytogroup.setuphandlers import _add_plugin
        self.aclu = self.layer['app'].acl_users
        _add_plugin(self.aclu, 'mptg')
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

        # mock _get_all_groups
        mock_get_all_groups = mock.patch.object(
            MPTGPlugin,
            '_get_all_groups',
            mock.Mock(wraps=MPTGPlugin._get_all_groups)
        )
        self.mocked_get_all_groups = mock_get_all_groups.start()
        self.addCleanup(mock_get_all_groups.stop)

    def test_getGroupsForPrincipal(self):
        self.mocked_valid_groups.side_effect = [
            [['prop1', 'group1', '', '', ''], ['prop2', 'group2', '', '', '']],
            [], [], [], [], [], [], [], [], [],
        ]
        self.mocked_group_property_of_principal.return_value = 'prop1'
        self.assertEqual(self.plugin.getGroupsForPrincipal(None), ('group1', ))

        self.mocked_valid_groups.side_effect = [
            [['prop1', 'group1', '', '', ''], ['prop2', 'group2', '', '', '']],
            [], [], [], [], [], [], [], [], [],
        ]
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
        self.mocked_get_all_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = ''
        group = self.plugin.getGroupById('group2')

        # id matches
        self.assertEqual('group2', group.getId())

        # username is Title
        self.assertEqual('title2', group.getUserName())

        # description, email are properties
        sheet = group.getPropertysheet(self.plugin.getId())
        self.assertIsNot(sheet, None)

    def test_getGroupIds(self):
        self.mocked_get_all_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = ''
        self.assertEqual(self.plugin.getGroupIds(), ['group1', 'group2'])

    def test_getGroups(self):
        self.mocked_valid_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_get_all_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = ''
        self.assertEqual(
            len(self.plugin.getGroups()),
            2
        )

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
        self.mocked_get_all_groups.return_value = [
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

    def test_get_group_members(self):
        # there is no utility be default providing the group members
        from zope.component import queryUtility
        from pas.plugins.memberpropertytogroup.interfaces import \
            IGetGroupMembers
        self.assertIsNone(queryUtility(IGetGroupMembers))

        # mock group and user with such an group
        self.mocked_valid_groups.return_value = [
            ['prop1', 'group1', 'title1', 'descr1', 'email1'],
            ['prop2', 'group2', 'title2', 'descr2', 'email2'],
        ]
        self.mocked_group_property_of_principal.return_value = 'prop2'

        # by default no utility for group members fetching is present
        self.assertEqual(
            self.plugin.getGroupMembers('prop2'),
            (),
        )

        # provide a utility and lets see if it get used
        from zope.component import provideUtility

        def fake_group_provider(plugin, group_id):
            return ('fakeuser',)

        provideUtility(fake_group_provider, provides=IGetGroupMembers)
        self.assertIs(
            queryUtility(IGetGroupMembers),
            fake_group_provider,
        )

        self.assertEqual(
            self.plugin.getGroupMembers('prop2'),
            ('fakeuser',),
        )


class TestPluginBasic(unittest.TestCase):
    """Test that pas.plugins.memberpropertytogroup basic plugin functions."""

    layer = PAS_PLUGINS_MPTG_PLONE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.registry = Registry()
        self.registry.registerInterface(
            IPasPluginsMemberpropertytogroupSettings
        )

    # def test_valid_groups(self):
    #     import ipdb;ipdb.set_trace()
    #     pass
