<div align="center"><img alt="logo" src="https://raw.githubusercontent.com/kitconcept/pas.plugins.memberpropertytogroup/main/kitconcept.png" width="150" /></div>

<h1 align="center">pas.plugins.memberpropertytogroup</h1>

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/pas.plugins.memberpropertytogroup)](https://pypi.org/project/pas.plugins.memberpropertytogroup/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pas.plugins.memberpropertytogroup)](https://pypi.org/project/pas.plugins.memberpropertytogroup/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/pas.plugins.memberpropertytogroup)](https://pypi.org/project/pas.plugins.memberpropertytogroup/)
[![PyPI - License](https://img.shields.io/pypi/l/pas.plugins.memberpropertytogroup)](https://pypi.org/project/pas.plugins.memberpropertytogroup/)
[![PyPI - Status](https://img.shields.io/pypi/status/pas.plugins.memberpropertytogroup)](https://pypi.org/project/pas.plugins.memberpropertytogroup/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/pas.plugins.memberpropertytogroup)](https://pypi.org/project/pas.plugins.memberpropertytogroup/)

[![Code analysis checks](https://github.com/kitconcept/pas.plugins.memberpropertytogroup/actions/workflows/code-analysis.yml/badge.svg)](https://github.com/kitconcept/pas.plugins.memberpropertytogroup/actions/workflows/code-analysis.yml)
[![Tests](https://github.com/kitconcept/pas.plugins.memberpropertytogroup/actions/workflows/tests.yml/badge.svg)](https://github.com/kitconcept/pas.plugins.memberpropertytogroup/actions/workflows/tests.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/kitconcept/pas.plugins.memberpropertytogroup)](https://github.com/kitconcept/pas.plugins.memberpropertytogroup)
[![GitHub Repo stars](https://img.shields.io/github/stars/kitconcept/pas.plugins.memberpropertytogroup?style=social)](https://github.com/kitconcept/pas.plugins.memberpropertytogroup)

</div>


Plone PAS plugin to create virtual groups based on member properties.

The main use case are organisations that have an existing LDAP infrastructure that organises groups through member properties instead of LDAP groups.

If you have a vanilla Plone site without LDAP, you most likely do not need this plugin.

## Features

- [Create virtual groups based on member properties](https://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-virtual-groups-based-on-member-properties)
- [Create multiple virtual groups based member properties](https://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-multiple-virtual-groups-based-on-member-properties)
- [Create virtual group based on a member properties prefix](https://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/create_virtual_groups.html#create-virtual-group-based-on-a-member-properties-prefix)
- [Grant local permissions based on virtual member properties groups]( https://paspluginsmemberpropertytogroup.readthedocs.org/en/latest/features/grant_permissions.html#grant-local-permissions-based-on-virtual-member-properties-groups)

## Installation

Add **pas.plugins.memberpropertytogroup** to the Plone installation using `pip`:

```bash
pip install pas.plugins.memberpropertytogroup
```

or add it as a dependency on your package's `setup.py`

```python
    install_requires = [
        "pas.plugins.memberpropertytogroup",
        "Plone",
        "plone.restapi",
        "setuptools",
    ],
```

Start Plone and activate the plugin in the addons control-panel.


## Source Code and Contributions

If you want to help with the development (improvement, update, bug-fixing, ...) of `pas.plugins.memberpropertytogroup` this is a great idea!

- [Issue Tracker](https://github.com/kitconcept/pas.plugins.memberpropertytogroup/issues)
- [Source Code](https://github.com/kitconcept/pas.plugins.memberpropertytogroup/)
- [Documentation](https://paspluginsmemberpropertytogroup.readthedocs.org)

We appreciate any contribution and if a release is needed to be done on PyPI, please just contact one of us.

Development
-----------

You need a working `python` environment (system, virtualenv, pyenv, etc) version 3.7 or superior.

Then install the dependencies and a development instance using:

```bash
make build
```

To run tests for this package:

```bash
make test
```

By default we use the latest Plone version in the 6.x series.

## Credits

The development of this plugin has been kindly sponsored by [Bonn University](http://www3.uni-bonn.de/) and [Helmholtz Zentrum Berlin](https://www.helmholtz-berlin.de/).


<img alt="Bonn University" src="http://www3.uni-bonn.de/logo.png" width="200px" />

<img alt="Helmholtz Zentrum Berlin" src="https://raw.githubusercontent.com/kitconcept/pas.plugins.memberpropertytogroup/main/hzb-logo.svg" width="200px" />


Developed by [kitconcept](https://www.kitconcept.com/)

<img alt="kitconcept GmbH" src="https://raw.githubusercontent.com/kitconcept/pas.plugins.memberpropertytogroup/main/kitconcept.png" width="200px" />

Icon by [FamFamFam](https://famfamfam.com/)

## License

The project is licensed under the GPLv2.
