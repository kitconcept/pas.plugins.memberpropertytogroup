# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.interfaces import _
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from plone.app.registry.browser import controlpanel
from z3c.form.browser.textlines import TextLinesFieldWidget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MemberpropertiestogroupSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPasPluginsMemberpropertytogroupSettings
    label = _(u"Member Properties To Group Settings")
    description = _(u"")

    def updateFields(self):
        super(MemberpropertiestogroupSettingsEditForm, self).updateFields()
        self.fields['valid_groups'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_1'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_2'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_3'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_4'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_5'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_6'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_7'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_8'].widgetFactory = TextLinesFieldWidget
        self.fields['valid_groups_9'].widgetFactory = TextLinesFieldWidget

    def updateWidgets(self):
        super(MemberpropertiestogroupSettingsEditForm, self).updateWidgets()


class MemberpropertiestogroupSettingsEditFormSettingsControlPanel(controlpanel.ControlPanelFormWrapper):  # noqa
    form = MemberpropertiestogroupSettingsEditForm
    index = ViewPageTemplateFile('mptg.pt')
