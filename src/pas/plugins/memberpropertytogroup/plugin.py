# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PlonePAS import interfaces as plonepas_interfaces
from Products.PlonePAS.plugins.group import PloneGroup
from Products.PluggableAuthService.interfaces import plugins as pas_interfaces
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from pas.plugins.memberpropertytogroup.interfaces import IMPTGPlugin
from zope.interface import implementer

import logging
import os

logger = logging.getLogger(__name__)
tpl_dir = os.path.join(os.path.dirname(__file__), 'browser')


def manage_addMPTGPlugin(dispatcher, id, title='', RESPONSE=None, **kw):
    """Create an instance of a MPTG Plugin.
    """
    plugin = MPTGPlugin(id, title, **kw)
    dispatcher._setObject(plugin.getId(), plugin)
    if RESPONSE is not None:
        RESPONSE.redirect('manage_workspace')


manage_addMPTGPluginForm = PageTemplateFile(
    os.path.join(tpl_dir, 'add_plugin.pt'),
    globals(),
    __name__='addMPTGPlugin'
)


@implementer(
    IMPTGPlugin,
    pas_interfaces.IGroupsPlugin,
    plonepas_interfaces.capabilities.IGroupCapability,
    plonepas_interfaces.group.IGroupIntrospection,
)
class MPTGPlugin(BasePlugin):
    """Memberproperties to Group mapping PAS plugin
    """
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
    # pas_interfaces.IGroupsPlugin
    #
    #  Determine the groups to which a user belongs.
    @security.private
    def getGroupsForPrincipal(self, principal, request=None):
        """principal -> ( group_1, ... group_N )

        o Return a sequence of group names to which the principal
          (either a user or another group) belongs.

        o May assign groups based on values in the REQUEST object, if present
        """
        # XXX Write me
        return tuple()

    # ##
    # plonepas_interfaces.capabilities.IGroupCapability
    # (plone ui specific)
    #
    @security.public
    def allowGroupAdd(self, principal_id, group_id):
        """
        True if this plugin will allow adding a certain principal to
        a certain group.

        -> this is not possible
        """
        return False

    @security.public
    def allowGroupRemove(self, principal_id, group_id):
        """
        True if this plugin will allow removing a certain principal
        from a certain group.

        -> this is not possible
        """
        return False

    # ##
    # plonepas_interfaces.capabilities.IGroupIntrospection
    # (plone ui specific)

    # XXX: why dont we have security declarations here?

    def getGroupById(self, group_id):
        """
        Returns the portal_groupdata-ish object for a group
        corresponding to this id. None if group does not exist here!
        """
        # group_id = decode_utf8(group_id)

        # XXX fecth Title (from registry settings?) for this plugin
        title = "READ ME FROM SOMEWHERE"

        group = PloneGroup(group_id, title).__of__(self)
        pas = self._getPAS()

        # add properties
        property_plugins = pas.plugins.listPlugins(
            pas_interfaces.IPropertiesPlugin
        )
        for propfinder_id, propfinder in property_plugins:
            data = propfinder.getPropertiesForUser(group, None)
            if data is not None:
                group.addPropertysheet(propfinder_id, data)

        # add subgroups
        group._addGroups(
            pas._getGroupsForPrincipal(group, None, plugins=pas.plugins)
        )

        # add roles
        role_plugins = pas.plugins.listPlugins(pas_interfaces.IRolesPlugin)
        for rolemaker_id, rolemaker in role_plugins:
            roles = rolemaker.getRolesForPrincipal(group, None)
            if roles is not None:
                group._addRoles(roles)

        return group

    def getGroups(self):
        """
        Returns an iteration of the available groups
        """
        return map(self.getGroupById, self.getGroupIds())

    def getGroupIds(self):
        """
        Returns a list of the available groups (ids)
        """
        return self.groups and self.groups.ids or []

    def getGroupMembers(self, group_id):
        """
        return the members of the given group
        """
        try:
            group = self.groups[group_id]
        except (KeyError, TypeError):
            return ()
        return tuple(group.member_ids)


InitializeClass(MPTGPlugin)
