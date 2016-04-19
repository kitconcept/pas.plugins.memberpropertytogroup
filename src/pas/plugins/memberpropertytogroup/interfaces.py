# -*- coding: utf-8 -*-
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.interface import Invalid
from zope.interface import invariant
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


_ = MessageFactory('pas.plugins.memberpropertytogroup')

NUMBER_OF_FIELDS = 10


def validate_valid_groups(value):
    """check that we have at least a tuple
    """
    for count, line in enumerate(value):
        if len(line.split('|')) < 2:
            raise Invalid(
                _(
                    'validate_valid_groups_not_enough_pipe',
                    u'Line ${count} needs at least property value and groupid',
                    mapping={'count': count + 1}
                )
            )
        if len(line.split('|')) > 5:
            raise Invalid(
                _(
                    'validate_valid_groups_too_many_pipe',
                    u'Line ${count} has too many segments.',
                    mapping={'count': count + 1}
                )
            )
    return True


class IPasPluginsMemberpropertytogroupLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPasPluginsMemberpropertytogroupSettings(Interface):

    group_property = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_1 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_1 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_2 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_2 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_3 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_3 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_4 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_4 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_5 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_5 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_6 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_6 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_7 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_7 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_8 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_8 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    group_property_9 = schema.TextLine(
        title=_(u'Users Group Property Field'),
        description=_(
            u'Name of property (key) on users property-sheet used as group '
            u'mapping.'
        ),
        required=False,
        default=u'',
        missing_value=u''
    )

    valid_groups_9 = schema.List(
        title=_(u'Mapped Groups'),
        description=_(
            u'Mapped groups to be processed. '
            u'On group per line. This creates valid plone groups, do not add '
            u'them at other places. '
            u'If user-property-value ends with an asterisk (*) all values '
            u'starting with the given string are matching. '
            u'Format: '
            u'user-property-value|group-id|title|description|email'
        ),
        required=False,
        value_type=schema.TextLine(),
        default=[],
        constraint=validate_valid_groups,
        missing_value=[]
    )

    showing_fields = schema.Int(
        title=_(u'Fields to show'),
        required=False,
        default=1)

    @invariant
    def validate_filled_field_couples(data):
        for index in range(0, NUMBER_OF_FIELDS):
            if index == 0:
                index = ''
            else:
                index = '_' + str(index)
            if getattr(data, 'group_property' + index) != '' and \
               getattr(data, 'valid_groups' + index) == []:
                raise Invalid(
                    _(u'The field group_property%s is filled while valid_groups%s is empty.') % (  # noqa
                        index,
                        index
                    )
                )

            if getattr(data, 'group_property' + index) == '' and \
               getattr(data, 'valid_groups' + index) != []:
                raise Invalid(
                    _(u'The field valid_groups%s is filled while group_property%s is empty.') % (  # noqa
                        index,
                        index
                    )
                )


class IMPTGPlugin(Interface):
    """Member Properties To Group Plugin"""


class IGetGroupMembers(Interface):
    """List group members from a MPTG plugin

    This is use case specific.
    By default no group members are listed.
    In some cases its possible to list members.
    This may be the case if users are from sources where a query performance
    good enough to list users.
    """

    def __call__(plugin, group_id):
        """list of members of the given group

        as defined by IGroupIntrospection.getGroupMembers
        """
