# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin

TITLE = 'Member Property To Group plugin (pas.plugins.memberpropertytogroup)'
DEFAULTID = 'memberpropertytogroup'


def _add_plugin(pas, pluginid=DEFAULTID):
    if pluginid in pas.objectIds():
        return TITLE + ' already installed.'
    plugin = MPTGPlugin(pluginid, title=TITLE)
    pas._setObject(pluginid, plugin)
    plugin = pas[plugin.getId()]  # get plugin acquisition wrapped!
    for info in pas.plugins.listPluginTypeInfo():
        interface = info['interface']
        if not interface.providedBy(plugin):
            continue
        pas.plugins.activatePlugin(interface, plugin.getId())
        pas.plugins.movePluginsDown(
            interface,
            [x[0] for x in pas.plugins.listPlugins(interface)[:-1]],
        )


def setup_plugin(context):
    if context.readDataFile('paspluginsmemberpropertytogroup_marker.txt') is not None:  # noqa
        _add_plugin(context.getSite().acl_users)


def _remove_plugin(pas, pluginid=DEFAULTID):
    if pluginid in pas.objectIds():
        pas.manage_delObjects([pluginid])


def remove_plugin(context):
    if context.readDataFile('paspluginsmemberpropertytogroup_uninstall.txt') is not None:  # noqa
        _remove_plugin(context.getSite().acl_users)
