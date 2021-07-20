from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


TITLE = "Member Property To Group plugin (pas.plugins.memberpropertytogroup)"
DEFAULTID = "memberpropertytogroup"


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return ["pas.plugins.memberpropertytogroup:uninstall"]


def _add_plugin(pas, pluginid=DEFAULTID):
    if pluginid in pas.objectIds():
        return TITLE + " already installed."
    plugin = MPTGPlugin(pluginid, title=TITLE)
    pas._setObject(pluginid, plugin)
    plugin = pas[plugin.getId()]  # get plugin acquisition wrapped!
    for info in pas.plugins.listPluginTypeInfo():
        interface = info["interface"]
        if not interface.providedBy(plugin):
            continue
        pas.plugins.activatePlugin(interface, plugin.getId())
        pas.plugins.movePluginsDown(
            interface,
            [x[0] for x in pas.plugins.listPlugins(interface)[:-1]],
        )


def setup_plugin(context):
    data = context.readDataFile("paspluginsmemberpropertytogroup_marker.txt")
    if data is not None:
        _add_plugin(context.getSite().acl_users)


def _remove_plugin(pas, plugin_id=DEFAULTID):
    if plugin_id in pas.objectIds():
        pas.manage_delObjects([plugin_id])


def uninstall(context):
    """Uninstall the plugin."""
    site = api.portal.get()
    _remove_plugin(site.acl_users)
