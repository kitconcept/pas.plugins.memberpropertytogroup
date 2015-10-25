# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from pas.plugins.memberpropertytogroup.interfaces import NUMBER_OF_FIELDS
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


def update_registry(context):
    registry = getUtility(IRegistry)
    registry.registerInterface(IPasPluginsMemberpropertytogroupSettings)


def add_show_fields_property(context):
    update_registry(context)
    registry = getUtility(IRegistry)
    mtpg_settings = registry.forInterface(
        IPasPluginsMemberpropertytogroupSettings
    )

    all_filled = True

    for index in range(1, NUMBER_OF_FIELDS):
        if not getattr(mtpg_settings, 'group_property_' + str(index)) and \
           not getattr(mtpg_settings, 'valid_groups_' + str(index)):
            # First empty field, set the index to the control field
            mtpg_settings.showing_fields = index
            all_filled = False
            break

    if all_filled:
        mtpg_settings.showing_fields = 10
