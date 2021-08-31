.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/kitconcept/pas.plugins.memberpropertytogroup/actions/workflows/main.yml/badge.svg
  :target: https://github.com/kitconcept/pas.plugins.memberpropertytogroup

.. image:: https://img.shields.io/coveralls/github/kitconcept/pas.plugins.memberpropertytogroup?style=flat-square
  :target: https://coveralls.io/r/kitconcept/pas.plugins.memberpropertytogroup

.. image:: https://img.shields.io/readthedocs/paspluginsmemberpropertytogroup?style=flat-square
  :target: https://readthedocs.org/projects/paspluginsmemberpropertytogroup/?badge=latest
  :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/pas.plugins.memberpropertytogroup.svg
    :target: https://pypi.python.org/pypi/pas.plugins.memberpropertytogroup/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/pas.plugins.memberpropertytogroup.svg
    :target: https://pypi.python.org/pypi/pas.plugins.memberpropertytogroup/
    :alt: License

|

.. image:: https://raw.githubusercontent.com/kitconcept/pas.plugins.memberpropertytogroup/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

=============================================================================
pas.plugins.memberpropertytogroup
=============================================================================

Plone PAS plugin to create virtual groups based on member properties.

The main use case are organisations that have an existing LDAP infrastructure that organises groups through member properties instead of LDAP groups.

If you have a vanilla Plone site without LDAP, you most likely do not need this plugin.


Features
--------

- `Create virtual groups based on member properties <http://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-virtual-groups-based-on-member-properties>`_
- `Create multiple virtual groups based member properties <http://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-multiple-virtual-groups-based-on-member-properties>`_
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

Plone 5
    There must be an ``python`` binary available in system path pointing to Python 3.7 or superior, then::

        $ make build-plone-5.2

Credits
-------

.. image:: http://www3.uni-bonn.de/logo.png
   :height: 164px
   :width: 222px
   :scale: 75 %
   :alt: Bonn University
   :align: center
   :target: http://uni-bonn.de

|

.. image:: https://raw.githubusercontent.com/kitconcept/pas.plugins.memberpropertytogroup/master/hzb-logo.svg
   :height: 39px
   :width: 174px
   :scale: 100 %
   :alt: Helmholtz Zentrum Berlin
   :align: center
   :target: https://www.helmholtz-berlin.de/

|

The development of this plugin has been kindly sponsored by `Bonn University`_ and `Helmholtz Zentrum Berlin`_.

.. image:: https://raw.githubusercontent.com/kitconcept/pas.plugins.memberpropertytogroup/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

Developed by `kitconcept`_.

Icon by `FamFamFam <http://famfamfam.com/>`_


License
-------

The project is licensed under the GPLv2.


.. _Bonn University: http://www3.uni-bonn.de/
.. _Helmholtz Zentrum Berlin: https://www.helmholtz-berlin.de/
.. _kitconcept: http://www.kitconcept.com/
