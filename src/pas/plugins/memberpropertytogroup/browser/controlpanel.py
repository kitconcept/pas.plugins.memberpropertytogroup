# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.interfaces import _
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from plone.app.registry.browser import controlpanel
from z3c.form.browser.textlines import TextLinesFieldWidget


class MemberpropertiestogroupSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPasPluginsMemberpropertytogroupSettings
    label = _(u"Member Properties To Group Settings")
    description = _(u"")

    def updateFields(self):
        super(MemberpropertiestogroupSettingsEditForm, self).updateFields()
        self.fields['valid_groups'].widgetFactory = TextLinesFieldWidget

    def updateWidgets(self):
        super(MemberpropertiestogroupSettingsEditForm, self).updateWidgets()


class MemberpropertiestogroupSettingsEditFormSettingsControlPanel(controlpanel.ControlPanelFormWrapper):  # noqa
    form = MemberpropertiestogroupSettingsEditForm
