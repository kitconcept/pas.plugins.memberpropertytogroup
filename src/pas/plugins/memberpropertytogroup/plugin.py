# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
from pas.plugins.memberpropertytogroup.interfaces import IMPTGPlugin
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from plone.registry.interfaces import IRegistry
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PlonePAS import interfaces as plonepas_interfaces
from Products.PluggableAuthService.interfaces import plugins as pas_interfaces
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
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
        pas_interfaces.IGroupsPlugin,
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

    def _principal_by_id(self, principal_id):
        """lookup principal by id
        """
        pas = self._getPAS()
        return pas.getUserById(principal_id)

    def _configured_property(self):
        """get configured key to fetch the group property from propertysheet
        """
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(
            IPasPluginsMemberpropertytogroupSettings,
        )
        return settings.group_property

    def _sheet_plugins_of_principal(self, principal):
        pas = self._getPAS()
        sheet_plugins = pas.plugins.listPlugins(
            pas_interfaces.IPropertiesPlugin
        )
        return dict(sheet_plugins)

    def _group_property_of_principal(self, principal):
        """get property with group information from principal
        """
        key = self._configured_property()
        sheet_plugins = self._sheet_plugins_of_principal(principal)
        for sheet_id in principal.listPropertysheets():
            sheet_provider = sheet_plugins[sheet_id]
            sheet = sheet_provider.getPropertiesForUser(principal)
            value = sheet.getProperty(key)
            if value:
                return value
        return None

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
        group_prop_id = self._group_property_of_principal(principal)
        print principal.getId(), " has group prop ", group_prop_id

        # check if group is valid
        pas = self._getPAS()
        group_plugins = pas.plugins.listPlugins(
            plonepas_interfaces.group.IGroupIntrospection
        )
        for plugin_id, plugin in group_plugins:
            group = plugin.getGroupById(group_prop_id)
            if group:
                return (group.getId(), )
        return tuple()


InitializeClass(MPTGPlugin)
