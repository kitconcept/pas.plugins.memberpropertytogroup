# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin


TITLE = 'Member Property To Group plugin (pas.plugins.memberpropertytogroup)'


def isNotThisProfile(context):
    return context.readDataFile('paspluginsmptg_zope_marker.txt') is None


def _addPlugin(pas, pluginid='memberpropertytogroup'):
    installed = pas.objectIds()
    if pluginid in installed:
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


def setupPlugin(context):
    if isNotThisProfile(context):
        return
    site = context.getSite()
    pas = site.acl_users
    _addPlugin(pas)
