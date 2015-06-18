# -*- coding: utf-8 -*-
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

_ = MessageFactory('pas.plugins.memberpropertytogroup')


class IPasPluginsMemberpropertytogroupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPasPluginsMemberpropertytogroupSettings(Interface):

    example_field = schema.TextLine(
        title=_(u"Example Field"),
        description=_(u"help_example_field"),
        required=False,
        default=u'',
    )


class IMPTGPlugin(Interface):
    """Member Properties To Group Plugin"""
