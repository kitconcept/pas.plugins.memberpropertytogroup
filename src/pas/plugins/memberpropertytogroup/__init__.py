from AccessControl.Permissions import add_user_folders
from pas.plugins.memberpropertytogroup.plugin import manage_addMPTGPlugin
from pas.plugins.memberpropertytogroup.plugin import manage_addMPTGPluginForm
from pas.plugins.memberpropertytogroup.plugin import MPTGPlugin
from pas.plugins.memberpropertytogroup.plugin import tpl_dir
from Products.PluggableAuthService import registerMultiPlugin


def initialize(context):
    """Initializer called when used as a Zope 2 product.

    This is referenced from configure.zcml. Regstrations as a "Zope 2 product"
    is necessary for GenericSetup profiles to work, for example.

    Here, we call the Archetypes machinery to register our content types
    with Zope and the CMF.
    """
    registerMultiPlugin(MPTGPlugin.meta_type)
    icon = tpl_dir / "mptg.png"
    context.registerClass(
        MPTGPlugin,
        permission=add_user_folders,
        icon=icon,
        constructors=(manage_addMPTGPluginForm, manage_addMPTGPlugin),
        visibility=None,
    )
