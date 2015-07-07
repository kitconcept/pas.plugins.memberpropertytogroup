# -*- coding: utf-8 -*-
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

_ = MessageFactory('pas.plugins.memberpropertytogroup')


class IPasPluginsMemberpropertytogroupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPasPluginsMemberpropertytogroupSettings(Interface):

    group_property = schema.TextLine(
        title=_(u"Group Proprty"),
        description=_(
            u"Property on users PropertySheet used as group mapping."
        ),
        required=False,
        default=u'',
    )


class IMPTGPlugin(Interface):
    """Member Properties To Group Plugin"""
