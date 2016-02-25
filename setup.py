# -*- coding: utf-8 -*-
"""Installer for the pas.plugins.memberpropertytogroup package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='pas.plugins.memberpropertytogroup',
    version='1.0a8.dev0',
    description='Plone PAS plugin to create virtual groups based on member properties.',  # noqa
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone PAS LDAP',
    author='Timo Stollenwerk',
    author_email='tisto@plone.org',
    url='http://pypi.python.org/pypi/pas.plugins.memberpropertytogroup',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['pas', 'pas.plugins'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
    ],
    extras_require={
        'plone3': [
            'plone.registry',
            'plone.app.registry',
        ],
        'test': [
            'mock',
            'plone.app.dexterity',
            'plone.app.testing',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
