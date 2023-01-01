from pas.plugins.memberpropertytogroup.testing import MPTG_ACCEPTANCE_TESTING
from pathlib import Path
from plone.app.testing import ROBOT_TEST_LEVEL
from plone.testing import layered

import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    current_dir = Path(__file__).parent.resolve()
    robot_dir = current_dir / "robot"
    robot_tests = [
        f"{path}".replace(f"{current_dir}/", "")
        for path in robot_dir.glob("test_*.robot")
    ]
    for robot_test in robot_tests:
        robottestsuite = robotsuite.RobotTestSuite(robot_test)
        robottestsuite.level = ROBOT_TEST_LEVEL
        suite.addTests(
            [
                layered(robottestsuite, layer=MPTG_ACCEPTANCE_TESTING),
            ]
        )
    return suite
