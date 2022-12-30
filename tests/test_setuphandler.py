from pas.plugins.memberpropertytogroup import setuphandlers


PLUGINID = "mptg"


def test_addplugin(aclu):

    result = setuphandlers._add_plugin(aclu, pluginid=PLUGINID)
    assert result is None
    assert PLUGINID in aclu.objectIds()


def test_is_mptgplugin(plugin):
    from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin

    assert isinstance(plugin, MPTGPlugin) is True


def test_can_only_be_added_once(aclu, plugin):
    result = setuphandlers._add_plugin(aclu, pluginid=PLUGINID)
    assert result == f"{setuphandlers.TITLE} already installed."


def test_removeplugin(aclu, plugin):
    setuphandlers._remove_plugin(aclu, plugin_id=PLUGINID)
    assert PLUGINID not in aclu.objectIds()
