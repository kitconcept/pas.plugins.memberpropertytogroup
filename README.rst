.. image:: https://travis-ci.org/kitconcept/pas.plugins.memberpropertytogroup.svg?branch=master
    :target: https://travis-ci.org/kitconcept/pas.plugins.memberpropertytogroup

.. image:: https://coveralls.io/repos/kitconcept/pas.plugins.memberpropertytogroup/badge.svg
  :target: https://coveralls.io/r/kitconcept/pas.plugins.memberpropertytogroup

.. image:: https://landscape.io/github/kitconcept/pas.plugins.memberpropertytogroup/master/landscape.svg?style=plastic
  :target: https://landscape.io/github/kitconcept/pas.plugins.memberpropertytogroup/master
  :alt: Code Health

.. image:: https://readthedocs.org/projects/paspluginsmemberpropertytogroup/badge/?version=latest
  :target: https://readthedocs.org/projects/paspluginsmemberpropertytogroup/?badge=latest
  :alt: Documentation Status

.. image:: https://badge.waffle.io/kitconcept/pas.plugins.memberpropertytogroup.png?label=ready&title=Ready
 :target: https://waffle.io/kitconcept/pas.plugins.memberpropertytogroup
 :alt: 'Stories in Ready'

.. image:: https://img.shields.io/pypi/dm/pas.plugins.memberpropertytogroup.svg
    :target: https://pypi.python.org/pypi/pas.plugins.memberpropertytogroup/
    :alt: Downloads

.. image:: https://img.shields.io/pypi/v/pas.plugins.memberpropertytogroup.svg
    :target: https://pypi.python.org/pypi/pas.plugins.memberpropertytogroup/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/pas.plugins.memberpropertytogroup.svg
    :target: https://pypi.python.org/pypi/pas.plugins.memberpropertytogroup/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/l/pas.plugins.memberpropertytogroup.svg
    :target: https://pypi.python.org/pypi/pas.plugins.memberpropertytogroup/
    :alt: License


.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.


=============================================================================
pas.plugins.memberpropertytogroup
=============================================================================

Plone PAS plugin to create virtual groups based on member properties.

The main use case are organisations that have an existing LDAP infrastructure that organises groups through member properties instead of LDAP groups.

If you have a vanilla Plone site without LDAP, you most likely do not need this plugin.


Features
--------

- `Create virtual groups based on member properties <http://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-virtual-groups-based-on-member-properties>`_
- `Create virtual groups based on multiple member properties <http://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-virtual-groups-based-on-multiple-member-properties>`_
- `Create virtual group based on a member properties prefix <http://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-virtual-group-based-on-a-member-properties-prefix>`_
- `Grant local permissions based on virtual member properties groups <http://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/grant_permissions.html#grant-local-permissions-based-on-virtual-member-properties-groups>`_


Documentation
-------------

The full documentation for integrators and developers can be found in the "docs" folder. It is also available online at http://paspluginsmemberpropertytogroup.readthedocs.org.


Installation
------------

Install pas.plugins.memberpropertytogroup by adding it to your buildout::

   [buildout]

    ...

    eggs =
        pas.plugins.memberpropertytogroup


and then run "bin/buildout".

If you are on Plone 3, you need to include the plone.app.registry KGS (know good set) and add the [plone3] extras to fetch the additonal dependencies that are not part of Plone 3::

    [buildout]
    extends =
        http://dist.plone.org/release/3.3.6/versions.cfg
        http://good-py.appspot.com/release/plone.app.registry/1.0b2?plone=3.3.6

    ...

    eggs =
        pas.plugins.memberpropertytogroup [plone3]

You can find a working example of a Plone 3 buildout here: https://github.com/kitconcept/pas.plugins.memberpropertytogroup/blob/master/plone-3.3.x.cfg


Contribute
----------

- `Source code at Github <https://github.com/kitconcept/pas.plugins.memberpropertytogroup>`_
- `Issue tracker at Github <https://github.com/kitconcept/pas.plugins.memberpropertytogroup/issues>`_ or same
  `issues on Kanban board at Waffle.io <https://waffle.io/kitconcept/pas.plugins.memberpropertytogroup>`_
- `Documentation at ReadTheDocs <http://paspluginsmemberpropertytogroup.readthedocs.org>`_:


Support
-------

If you are having issues, `please let us know <https://github.com/kitconcept/pas.plugins.memberpropertytogroup/issues>`_.


Development
-----------

Plone 3
    There must be an ``python2.4`` binary available in system path, then::

        $ bootstrap-3.3.x.sh

Plone 4
    There must be an ``python`` binary available in system path pointing to Python 2.7 , then::

        $ bootstrap-4.3.x.sh

Plone 5
    There must be an ``python`` binary available in system path pointing to Python 2.7 , then::

        $ bootstrap-5.0.x.sh


Credits
-------

.. image:: http://www3.uni-bonn.de/logo.png
   :height: 164px
   :width: 222px
   :scale: 75 %
   :alt: Bonn University
   :align: center
   :target: http://uni-bonn.de

The development of this plugin has been kindly sponsored by `Bonn University`_.

.. image:: http://www.kitconcept.com/images/logo-200px.png
   :height: 200px
   :width: 65px
   :scale: 300 %
   :alt: kitconcept
   :align: center
   :target: http://www.kitconcept.com/

Developed by `kitconcept`_.

Icon by `FamFamFam <http://famfamfam.com/>`_


License
-------

The project is licensed under the GPLv2.


.. _Bonn University: http://www3.uni-bonn.de/
.. _kitconcept: http://www.kitconcept.com/
