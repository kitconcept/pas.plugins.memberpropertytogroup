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
                    mapping={'count': count+1}
                )
            )
        if len(line.split('|')) > 5:
            raise Invalid(
                _(
                    'validate_valid_groups_too_many_pipe',
                    u"Line ${count} has too many segments.",
                    mapping={'count': count+1}
                )
            )
    return True


class IPasPluginsMemberpropertytogroupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPasPluginsMemberpropertytogroupSettings(Interface):

    group_property = schema.TextLine(
        title=_(u"Group Property"),
        description=_(
            u"Property key on users PropertySheet used as group mapping."
        ),
        required=False,
        default=u'',
    )

    valid_groups = schema.List(
        title=_(u"Valid Groups"),
        description=_(
            u"List of valid groups to be processed. "
            u"On group per line. "
            u"Format: "
            u"propertyvalue|groupid|grouptitle|groupdescription|groupemail"
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
    )


class IMPTGPlugin(Interface):
    """Member Properties To Group Plugin"""
