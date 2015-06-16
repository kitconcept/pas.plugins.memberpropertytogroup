
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

Plone PAS plugin that allows to create virtual groups based on member
properties.

The main use case are organisations that have an existing LDAP infrastructure
that organise groups through member properties instead of LDAP groups. If you
have a vanilla Plone site without LDAP you most likely do not need this
plugin.


Credits
-------

The development of this plugin has been kindly sponsored by `Bonn University`_.

.. image:: http://www3.uni-bonn.de/logo.png
   :height: 164px
   :width: 222px
   :scale: 50 %
   :alt: Bonn University
   :align: right


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


and then running "bin/buildout"


Contribute
----------

- Issue Tracker: https://github.com/kitconcept/pas.plugins.memberpropertytogroup/issues / https://waffle.io/kitconcept/pas.plugins.memberpropertytogroup
- Source Code: https://github.com/kitconcept/pas.plugins.memberpropertytogroup

Development
-----------

Plone 3::

  $ mkdir downloads
  $ python2.4 plone-3.3.x-bootstrap.py -c plone-3.3.x.cfg
  $ bin/buildout -c plone-3.3.x.cfg


License
-------

The project is licensed under the GPLv2.


.. _Bonn University: http://www3.uni-bonn.de/
