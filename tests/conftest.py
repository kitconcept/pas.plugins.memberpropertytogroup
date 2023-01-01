from pas.plugins.memberpropertytogroup import setuphandlers
from pas.plugins.memberpropertytogroup.testing import MPTG_ACCEPTANCE_TESTING
from pas.plugins.memberpropertytogroup.testing import MPTG_FUNCTIONAL_TESTING
from pas.plugins.memberpropertytogroup.testing import MPTG_INTEGRATION_TESTING
from pas.plugins.memberpropertytogroup.testing import MPTG_ZOPE_FIXTURE
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.base.utils import get_installer
from plone.browserlayer import utils
from plone.testing.z2 import Browser

import gocept.pytestlayer.fixture
import pytest


PLUGINID = "mptg"


_FIXTURES = (
    (MPTG_ACCEPTANCE_TESTING, "acceptance"),
    (MPTG_FUNCTIONAL_TESTING, "functional"),
    (MPTG_INTEGRATION_TESTING, "integration"),
    (MPTG_ZOPE_FIXTURE, "zope"),
)


def fixtures():
    fixtures = {}
    for item, prefix in _FIXTURES:
        fixtures.update(
            gocept.pytestlayer.fixture.create(
                item,
                session_fixture_name=f"{prefix}_session",
                class_fixture_name=f"{prefix}_class",
                function_fixture_name=prefix,
            )
        )
    return fixtures


globals().update(fixtures())


@pytest.fixture()
def portal(integration):
    return integration["portal"]


@pytest.fixture
def http_request(integration):
    return integration["request"]


@pytest.fixture
def installer(portal):
    return get_installer(portal)


@pytest.fixture
def browser_layers(portal):
    return utils.registered_layers()


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
