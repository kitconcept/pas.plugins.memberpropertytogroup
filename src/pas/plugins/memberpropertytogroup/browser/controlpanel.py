# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel

from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from pas.plugins.memberpropertytogroup import _


class MemberpropertiestogroupSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPasPluginsMemberpropertytogroupSettings
    label = _(u"Member Properties To Group Settings")
    description = _(u"")

    def updateFields(self):
        super(MemberpropertiestogroupSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(MemberpropertiestogroupSettingsEditForm, self).updateWidgets()


class MemberpropertiestogroupSettingsEditFormSettingsControlPanel(controlpanel.ControlPanelFormWrapper):  # noqa
    form = MemberpropertiestogroupSettingsEditForm
