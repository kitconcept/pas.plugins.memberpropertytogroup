from pas.plugins.memberpropertytogroup import setuphandlers
from pas.plugins.memberpropertytogroup.testing import MPTG_ACCEPTANCE_TESTING
from pas.plugins.memberpropertytogroup.testing import MPTG_FUNCTIONAL_TESTING
from pas.plugins.memberpropertytogroup.testing import MPTG_INTEGRATION_TESTING
from pas.plugins.memberpropertytogroup.testing import MPTG_ZOPE_FIXTURE
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.testing.z2 import Browser
from pytest_plone import fixtures_factory

import pytest


PLUGINID = "mptg"

pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (MPTG_ACCEPTANCE_TESTING, "acceptance"),
            (MPTG_FUNCTIONAL_TESTING, "functional"),
            (MPTG_INTEGRATION_TESTING, "integration"),
            (MPTG_ZOPE_FIXTURE, "zope"),
        )
    )
)


@pytest.fixture
def aclu(zope):
    return zope["app"].acl_users


@pytest.fixture
def plugin(aclu):
    setuphandlers._add_plugin(aclu, pluginid=PLUGINID)
    return aclu[PLUGINID]


@pytest.fixture
def browser(integration):
    browser = Browser(integration["app"])
    browser.handleErrors = False
    return browser


@pytest.fixture
def browser_auth(browser):
    browser.addHeader(
        "Authorization",
        f"Basic {SITE_OWNER_NAME}:{SITE_OWNER_PASSWORD}",
    )
    return browser
