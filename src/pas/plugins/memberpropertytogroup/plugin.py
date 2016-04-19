# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from pas.plugins.memberpropertytogroup.interfaces import IGetGroupMembers
from pas.plugins.memberpropertytogroup.interfaces import IMPTGPlugin
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from pas.plugins.memberpropertytogroup.interfaces import NUMBER_OF_FIELDS
from plone.registry.interfaces import IRegistry
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PlonePAS import interfaces as plonepas_interfaces
from Products.PlonePAS.plugins.group import PloneGroup
from Products.PluggableAuthService.interfaces import plugins as pas_interfaces
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.UserPropertySheet import UserPropertySheet
from zope.component import queryUtility
from zope.interface import implements

import logging
import os

logger = logging.getLogger(__name__)
tpl_dir = os.path.join(os.path.dirname(__file__), 'browser')


def manage_addMPTGPlugin(context, id, title='', RESPONSE=None, **kw):
    """Create an instance of a MPTG Plugin.
    """
    plugin = MPTGPlugin(id, title, **kw)
    context._setObject(plugin.getId(), plugin)
    if RESPONSE is not None:
        RESPONSE.redirect('manage_workspace')


manage_addMPTGPluginForm = PageTemplateFile(
    os.path.join(tpl_dir, 'add_plugin.pt'),
    globals(),
    __name__='addMPTGPlugin'
)


class MPTGPlugin(BasePlugin):
    """Memberproperties to Group mapping PAS plugin
    """
    # using implements explicit here for python 2.4 compat.
    implements(
        IMPTGPlugin,
        pas_interfaces.IGroupEnumerationPlugin,
        pas_interfaces.IGroupsPlugin,
        pas_interfaces.IPropertiesPlugin,
        plonepas_interfaces.capabilities.IGroupCapability,
        plonepas_interfaces.group.IGroupIntrospection,
    )
    security = ClassSecurityInfo()
    meta_type = 'Member Properties To Group Plugin'
    BasePlugin.manage_options

    # Tell PAS not to swallow our exceptions
    _dont_swallow_my_exceptions = False

    def __init__(self, id, title=None, **kw):
        self._setId(id)
        self.title = title
        self.plugin_caching = True

    # ##
    # helper

    @property
    def _settings(self):
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(
            IPasPluginsMemberpropertytogroupSettings,
        )
        return settings

    def _valid_groups(self, index):
        result = []
        # Kept original field name for direct backwards compat
        if index == 0:
            index = ''
        else:
            index = '_' + str(index)
        for line in getattr(self._settings, 'valid_groups' + index):
            if not line.strip():
                continue
            result.append((line.split('|') + [''] * 5)[:5])
        return result

    def _get_all_groups(self):
        valid_groups = []
        for index in range(0, NUMBER_OF_FIELDS):
            partial_groups = self._valid_groups(index)
            if partial_groups:
                valid_groups = valid_groups + partial_groups
        return valid_groups

    def _principal_by_id(self, principal_id):
        """lookup principal by id
        """
        pas = self._getPAS()
        return pas.getUserById(principal_id)

    def _configured_property(self, index):
        """get configured key to fetch the group property from propertysheet
        """
        # Kept original field name for direct backwards compat
        if index == 0:
            index = ''
        else:
            index = '_' + str(index)
        return getattr(self._settings, 'group_property' + index)

    def _sheet_plugins_of_principal(self, principal):
        pas = self._getPAS()
        sheet_plugins = pas.plugins.listPlugins(
            pas_interfaces.IPropertiesPlugin
        )
        return dict(sheet_plugins)

    def _group_property_of_principal(self, principal, index):
        """get property with group information from principal
        """
        key = self._configured_property(index)
        sheet_plugins = self._sheet_plugins_of_principal(principal)
        for sheet_id in principal.listPropertysheets():
            sheet_provider = sheet_plugins[sheet_id]
            sheet = sheet_provider.getPropertiesForUser(principal)
            value = sheet.getProperty(key)
            if value:
                return value
        return None

    def _is_property_match(self, group_prop, group_match):
        """check a given group property of a user against a group matcher
        """
        if not isinstance(group_prop, basestring):
            return False
        star = group_match.endswith('*')
        if star:
            group_match = group_match[:-1]
        return (
            star and group_prop.startswith(group_match) or
            group_prop == group_match
        )

    # ##
    # pas_interfaces.IGroupsPlugin
    #
    #  Determine the groups to which a user belongs.

    security.declarePrivate('getGroupsForPrincipal')  # Plone3bbb

    def getGroupsForPrincipal(self, principal, request=None):
        """principal -> ( group_1, ... group_N )

        o Return a sequence of group names to which the principal
          (either a user or another group) belongs.

        o May assign groups based on values in the REQUEST object, if present
        """
        groups_matched = []
        for index in range(0, NUMBER_OF_FIELDS):
            group_prop_value = self._group_property_of_principal(principal,
                                                                 index)
            for prop, gid, title, descr, email in self._valid_groups(index):
                if self._is_property_match(group_prop_value, prop):
                    groups_matched.append(gid)
        return tuple(groups_matched)

    # ##
    # plonepas_interfaces.capabilities.IGroupCapability
    # (plone ui specific)
    #
    security.declarePublic('allowGroupAdd')

    def allowGroupAdd(self, principal_id, group_id):
        """
        True if this plugin will allow adding a certain principal to
        a certain group.
        """
        return False

    security.declarePublic('allowGroupRemove')

    def allowGroupRemove(self, principal_id, group_id):
        """
        True if this plugin will allow removing a certain principal
        from a certain group.
        """
        return False

    # ##
    # plonepas_interfaces.capabilities.IGroupIntrospection
    # (plone ui specific)

    def getGroupById(self, group_id):
        """
        Returns the portal_groupdata-ish object for a group
        corresponding to this id. None if group does not exist here!
        """
        for prop, gid, title, descr, email in self._get_all_groups():
            if gid != group_id:
                continue
            group = PloneGroup(gid, title).__of__(self)
            pas = self._getPAS()
            plugins = pas.plugins

            # add properties
            properties_provider = plugins.listPlugins(
                pas_interfaces.IPropertiesPlugin
            )
            for propfinder_id, propfinder in properties_provider:
                data = propfinder.getPropertiesForUser(group, None)
                if not data:
                    continue
                group.addPropertysheet(propfinder_id, data)

            # add subgroups
            group._addGroups(
                pas._getGroupsForPrincipal(
                    group,
                    None,
                    plugins=plugins
                )
            )
            # add roles
            role_provider = plugins.listPlugins(pas_interfaces.IRolesPlugin)
            for rolemaker_id, rolemaker in role_provider:
                roles = rolemaker.getRolesForPrincipal(group, None)
                if not roles:
                    continue
                group._addRoles(roles)
            return group
        return None

    def getGroups(self):
        """
        Returns an iteration of the available groups
        """
        return map(self.getGroupById, self.getGroupIds())

    def getGroupIds(self):
        """
        Returns a list of the available groups (ids)
        """
        return [_[1] for _ in self._get_all_groups()]

    def getGroupMembers(self, group_id):
        """
        returns the members of the given group
        we can not list group members, since this is too expensive
        thus we ask for some project specific implementation here
        if no such implementation is provided we just return an empty tuple
        """
        group_member_fetcher = queryUtility(IGetGroupMembers)
        if group_member_fetcher is None:
            return tuple()
        return group_member_fetcher(self, group_id)

    # ##
    # pas_interfaces.plugins.IPropertiesPlugin

    def getPropertiesForUser(self, group, request=None):
        group_id = group.getId()
        for prop, gid, title, descr, email in self._get_all_groups():
            if gid != group_id:
                continue
            sheet = UserPropertySheet(
                self.getId(),
                title=title,
                description=descr,
                email=email
            )
            return sheet
        return None

    # ##
    # pas_interfaces.IGroupEnumerationPlugin
    #
    #  Allow querying groups by ID, and searching for groups.
    #
    security.declarePrivate('enumerateGroups')

    def enumerateGroups(
        self,
        id=None,
        exact_match=False,
        sort_by=None,
        max_results=None,
        **kw
    ):
        """ -> ( group_info_1, ... group_info_N )

        o Return mappings for groups matching the given criteria.

        o 'id' in combination with 'exact_match' true, will
          return at most one mapping per supplied ID ('id' and 'login'
          may be sequences).

        o If 'exact_match' is False, then 'id' may be treated by
          the plugin as "contains" searches (more complicated searches
          may be supported by some plugins using other keyword arguments).

        o If 'sort_by' is passed, the results will be sorted accordingly.
          known valid values are 'id' (some plugins may support others).

        o If 'max_results' is specified, it must be a positive integer,
          limiting the number of returned mappings.  If unspecified, the
          plugin should return mappings for all groups satisfying the
          criteria.

        o Minimal keys in the returned mappings:

          'id' -- (required) the group ID

          'pluginid' -- (required) the plugin ID (as returned by getId())

          'properties_url' -- (optional) the URL to a page for updating the
                              group's properties.

          'members_url' -- (optional) the URL to a page for updating the
                           principals who belong to the group.

        o Plugin *must* ignore unknown criteria.

        o Plugin may raise ValueError for invalid critera.

        o Insufficiently-specified criteria may have catastrophic
          scaling issues for some implementations.
        """
        if id:
            kw['id'] = id
        result = []
        for prop, gid, title, descr, email in self._get_all_groups():
            record = {
                'id': gid,
                'pluginid': self.getId(),
            }
            if not kw:  # show all
                result.append(record)
                continue
            if exact_match:
                if 'id' in kw and kw['id'] == gid:
                    result.append(record)
                continue
            if gid.startswith(kw['id']):
                result.append(record)
                continue
        # todo: sort
        if max_results and len(result) > max_results:
            result = result[:max_results]
        return result

InitializeClass(MPTGPlugin)
