"""Installer for the pas.plugins.memberpropertytogroup package."""
from setuptools import find_packages
from setuptools import setup


def _read_file(filename: str) -> str:
    """Read a file and return its contents."""
    data = open(filename).read()
    return f"{data}\n"


description = "Plone PAS plugin to create virtual groups based on member properties"

long_description = (
    f"{_read_file('README.rst')}"
    "Contributors\n"
    "============\n"
    f"{_read_file('CONTRIBUTORS.rst')}"
    f"{_read_file('CHANGES.rst')}"
)


setup(
    name="pas.plugins.memberpropertytogroup",
    version="2.0.0",
    description=description,
    long_description=long_description,
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
