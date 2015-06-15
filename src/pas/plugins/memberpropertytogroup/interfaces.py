# -*- coding: utf-8 -*-
from pas.plugins.memberpropertytogroup import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPasPluginsMemberpropertytogroupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPasPluginsMemberpropertytogroupSettings(Interface):

    example_field = schema.TextLine(
        title=_(u"Example Field"),
        description=_(u"help_example_field"),
        required=False,
        default=u'',
    )
