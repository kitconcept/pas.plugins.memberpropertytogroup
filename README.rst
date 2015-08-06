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

- As administrator I can create a group based on member properties
- As reviewer I can grant permissions based on member properties groups
- As administrator I can create a group based on multiple member properties
- As administrator I can create a group based on member properties


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


and then running "bin/buildout".


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

        $ bootstrap-4.3.x.sh


Credits
-------

.. image:: http://www3.uni-bonn.de/logo.png
   :height: 164px
   :width: 222px
   :scale: 50 %
   :alt: Bonn University
   :align: right
   target: http://uni-bonn.de

The development of this plugin has been kindly sponsored by `Bonn University`_.

Icon by `FamFamFam <http://famfamfam.com/>`_


License
-------

The project is licensed under the GPLv2.


.. _Bonn University: http://www3.uni-bonn.de/
