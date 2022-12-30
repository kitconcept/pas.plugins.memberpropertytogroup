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
    version="2.1.2.dev0",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    keywords="Python Plone PAS LDAP",
    author="kitconcept GmbH",
    author_email="info@kitconcept.com",
    url="http://pypi.python.org/pypi/pas.plugins.memberpropertytogroup",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["pas", "pas.plugins"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Plone",
        "setuptools",
    ],
    extras_require={
        "test": [
            "mock",
            "plone.api",
            "plone.app.testing",
            "plone.app.robotframework",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
