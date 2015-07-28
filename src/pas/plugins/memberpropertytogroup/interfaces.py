# -*- coding: utf-8 -*-
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.interface import Invalid
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

_ = MessageFactory('pas.plugins.memberpropertytogroup')


def validate_valid_groups(value):
    """check that we have at least a tuple
    """
    for count, line in enumerate(value):
        if len(line.split('|')) < 2:
            raise Invalid(
                _(
                    'validate_valid_groups_not_enough_pipe',
                    u"Line ${count} needs at least property value and groupid",
                    mapping={'count': count + 1}
                )
            )
        if len(line.split('|')) > 5:
            raise Invalid(
                _(
                    'validate_valid_groups_too_many_pipe',
                    u"Line ${count} has too many segments.",
                    mapping={'count': count + 1}
                )
            )
    return True


class IPasPluginsMemberpropertytogroupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPasPluginsMemberpropertytogroupSettings(Interface):

    group_property = schema.TextLine(
        title=_(u"Users Group Property Field"),
        description=_(
            u"Name of property (key) on users property-sheet used as group "
            u"mapping."
        ),
        required=False,
        default=u'',
    )

    valid_groups = schema.List(
        title=_(u"Mapped Groups"),
        description=_(
            u"Mapped groups to be processed. "
            u"On group per line. This creates valid plone groups, do not add "
            u"them at other places. "
            u"If user-property-value ends with an asterisk (*) all values "
            u"starting with the given string are matching. "
            u"Format: "
            u"user-property-value|group-id|title|description|email"
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
    )


class IMPTGPlugin(Interface):
    """Member Properties To Group Plugin"""
