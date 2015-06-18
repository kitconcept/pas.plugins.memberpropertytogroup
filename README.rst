
.. image:: https://coveralls.io/repos/kitconcept/pas.plugins.memberpropertytogroup/badge.svg
  :target: https://coveralls.io/r/kitconcept/pas.plugins.memberpropertytogroup

.. image:: https://badge.waffle.io/kitconcept/pas.plugins.memberpropertytogroup.png?label=ready&title=Ready
 :target: https://waffle.io/kitconcept/pas.plugins.memberpropertytogroup
 :alt: 'Stories in Ready'

.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

=============================================================================
pas.plugins.memberpropertytogroup
=============================================================================

Plone PAS plugin that allows to create virtual groups based on member properties.

The main use case are organisations that have an existing LDAP infrastructure that organise groups through member properties instead of  DAP groups.
If you have a vanilla Plone site without LDAP you most likely do not need this plugin.


Features
--------

- Can be bullet points


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

If you want to help with the development (improvement, update, bug-fixing, ...) of ``pas.plugins.memberpropertytogroup`` this is a great idea!

- `Source code at Github <https://github.com/kitconcept/pas.plugins.memberpropertytogroup>`_
- `Issue tracker at Github <https://github.com/kitconcept/pas.plugins.memberpropertytogroup/issues>`_ or same
  `issues on Kanban board at Waffle.io <https://waffle.io/kitconcept/pas.plugins.memberpropertytogroup>`_

Maintainers are Timo Stollenwerk and Jens Klein.

We appreciate any contribution and if a release is needed to be done on pypi, please just contact one of us.


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

The development of this plugin has been kindly sponsored by `Bonn University`_.

.. image:: http://www3.uni-bonn.de/logo.png
   :height: 164px
   :width: 222px
   :scale: 50 %
   :alt: Bonn University
   :align: right

Icon by `FamFamFam <http://famfamfam.com/>`_


License
-------

The project is licensed under the GPLv2.


.. _Bonn University: http://www3.uni-bonn.de/
