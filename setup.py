"""Installer for the pas.plugins.memberpropertytogroup package."""
from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


description = "Plone PAS plugin to create virtual groups based on member properties"

setup(
    name="pas.plugins.memberpropertytogroup",
    version="3.0.0",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone PAS LDAP",
    author="kitconcept GmbH",
    author_email="info@kitconcept.com",
    url="http://pypi.python.org/pypi/pas.plugins.memberpropertytogroup",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["pas", "pas.plugins"],
    package_dir={"": "src"},
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Plone",
        "setuptools",
    ],
    extras_require={
        "test": [
            "gocept.pytestlayer",
            "mock",
            "plone.app.testing",
            "plone.app.robotframework[debug]",
            "plone.restapi[test]",
            "pytest",
            "pytest-mock",
            "pytest-cov",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = pas.plugins.memberpropertytogroup.locales.update:update_locale
    """,
)
