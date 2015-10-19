# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup.interfaces import IPasPluginsMemberpropertytogroupSettings  # noqa
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


def update_registry(context):
    registry = getUtility(IRegistry)
    registry.registerInterface(IPasPluginsMemberpropertytogroupSettings)
