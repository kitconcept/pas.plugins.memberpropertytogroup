# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.interfaces import _
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from plone.app.registry.browser import controlpanel
from z3c.form.browser.textlines import TextLinesFieldWidget
from z3c.form.interfaces import HIDDEN_MODE

try:
    from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
except ImportError:
    from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile


class MemberpropertiestogroupSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPasPluginsMemberpropertytogroupSettings
    label = _(u'Member Properties To Group Settings')
    description = _(u'')
    template = ViewPageTemplateFile('mptg_form.pt')

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
        self.widgets['showing_fields'].mode = HIDDEN_MODE

    def get_visibility_for(self, widget):
        showing_fields = int(self.widgets['showing_fields'].value)
        # Show always the first set of fields
        if widget.name.split('.')[2] == 'group_property' or \
           widget.name.split('.')[2] == 'valid_groups' or \
           widget.name.split('.')[2] == 'showing_fields':
            return 'row'

        elif int(widget.name.split('.')[2].split('_')[2]) < showing_fields:
            return 'row'

        elif int(widget.name.split('.')[2].split('_')[2]) >= showing_fields:
            return 'row field-hidden'


class MemberpropertiestogroupSettingsEditFormSettingsControlPanel(controlpanel.ControlPanelFormWrapper):  # noqa
    form = MemberpropertiestogroupSettingsEditForm
