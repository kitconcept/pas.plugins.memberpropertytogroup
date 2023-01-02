from pas.plugins.memberpropertytogroup import interfaces as ifaces
from pas.plugins.memberpropertytogroup.interfaces import _
from plone.app.registry.browser import controlpanel
from plone.restapi.controlpanels import RegistryConfigletPanel
from z3c.form.browser.textlines import TextLinesFieldWidget
from z3c.form.interfaces import HIDDEN_MODE
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.component import adapter
from zope.interface import Interface


class MemberpropertiestogroupSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ifaces.IPasPluginsMemberpropertytogroupSettings
    label = _("Member Properties To Group Settings")
    description = _("")
    template = ViewPageTemplateFile("mptg_form.pt")

    valid_groups = (
        "valid_groups",
        "valid_groups_1",
        "valid_groups_2",
        "valid_groups_3",
        "valid_groups_4",
        "valid_groups_5",
        "valid_groups_6",
        "valid_groups_7",
        "valid_groups_8",
        "valid_groups_9",
    )

    def updateFields(self):
        super().updateFields()
        for field_name in self.valid_groups:
            self.fields[field_name].widgetFactory = TextLinesFieldWidget

    def updateWidgets(self):
        super().updateWidgets()
        self.widgets["showing_fields"].mode = HIDDEN_MODE

    def get_visibility_for(self, widget):
        showing_fields = int(self.widgets["showing_fields"].value)
        widget_name = widget.name.split(".")[2]
        # Show always the first set of fields
        if widget_name in ("group_property", "valid_groups", "showing_fields"):
            return "row"
        widget_name_idx = int(widget_name.split("_")[2])
        if widget_name_idx < showing_fields:
            return "row"
        elif widget_name_idx >= showing_fields:
            return "row field-hidden"


class MemberpropertiestogroupSettingsEditFormSettingsControlPanel(
    controlpanel.ControlPanelFormWrapper
):  # noqa
    form = MemberpropertiestogroupSettingsEditForm


@adapter(Interface, ifaces.IPasPluginsMemberpropertytogroupLayer)
class PluginSettingsConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = ifaces.IPasPluginsMemberpropertytogroupSettings
    configlet_id = "memberpropertytogroup"
    configlet_category_id = "Products"
    title = _("Member Property To Group")
    group = ""
    schema_prefix = "pas.plugins.memberpropertytogroup.interfaces.IPasPluginsMemberpropertytogroupSettings"  # noQA
