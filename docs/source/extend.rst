Extensibility
=============

Reason for custom code
----------------------

``pas.plugins.memberpropertytogroup`` has one shortcoming:
With this approach it is not possible to list the groups a members in a performant way.
One would have to loop over all member instances for each group id,
which gets expensive soon if there are many users.

Specific backends - or user providers - offering its specific ways to get around this.
I.e for users stored in a SQL database the group may be queried efficiently.
The same may apply for LDAP, dependent on how the users are stored.
For other storages or for the default Plone users this does not apply

Solution
--------

The plugins method ``getGroupMembers`` is responsible to return the members of a given group.
There a utility component is queried providing the interface ``pas.plugins.memberpropertytogroup.interfaces.IGetGroupMembers``.
If there is no utility found an empty tuple is returned.
This is the default behavior.

Integrators using this module may provide their own solution by registering a utility for this interface.
In case a utility was found, it gets called with the plugin instance and the group id as parameters.
The result of the call is then considered as a list of members of the group and returned as is.


Example
-------

Here is a simple but complete example for a specific ``IGetGroupMembers`` providing function.

In a file ``getgroupmembers.py``:

.. code:: python

    from pas.plugins.memberpropertytogroup.interfaces import IGetGroupMembers
    from zope.component import provider

    @provider(IGetGroupMembers)
    def example_group_member_fetcher(plugin, group_id):
        # ... here the real code to get the groups members
        # fake here as example
        group_members = ('foo', 'bar', 'baz')
        return group_members

And a line of zcml configuration in ``configure.xml``:


.. code:: xml

    ...
    <utility component=".getgroupmembers.example_group_member_fetcher" />
    ...
