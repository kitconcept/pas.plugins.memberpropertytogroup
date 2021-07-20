from pas.plugins.memberpropertytogroup.interfaces import _  # noqa
from pas.plugins.memberpropertytogroup.interfaces import (
    IPasPluginsMemberpropertytogroupSettings,
)
from plone.app.registry.browser import controlpanel
from z3c.form.browser.textlines import TextLinesFieldWidget
from z3c.form.interfaces import HIDDEN_MODE


try:
    from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
except ImportError:
    from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile


class MemberpropertiestogroupSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPasPluginsMemberpropertytogroupSettings
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
        # Show always the first set of fields
        if (
            widget.name.split(".")[2] == "group_property"
            or widget.name.split(".")[2] == "valid_groups"
            or widget.name.split(".")[2] == "showing_fields"
        ):
            return "row"

        elif int(widget.name.split(".")[2].split("_")[2]) < showing_fields:
            return "row"

        elif int(widget.name.split(".")[2].split("_")[2]) >= showing_fields:
            return "row field-hidden"


class MemberpropertiestogroupSettingsEditFormSettingsControlPanel(
    controlpanel.ControlPanelFormWrapper
):  # noqa
    form = MemberpropertiestogroupSettingsEditForm
