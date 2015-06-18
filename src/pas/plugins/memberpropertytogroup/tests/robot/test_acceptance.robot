# ============================================================================
# ACCEPTANCE TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s pas.plugins.memberpropertytogroup -t test_example.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src pas.plugins.memberpropertytogroup.testing.PAS_PLUGINS_MPTG_PLONE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/pas/plugins/memberpropertytogroup/tests/robot/test_example.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As administrator I can create a group based on member properties
  Pass Execution  Not implemented yet
  Given a user 'John Doe' with the property 'usertype' = 'employee'
    and a logged-in manager
   When I create a virtual group 'Employees' based on the property 'usertype' = 'employee'
   Then the user 'John Doe' is member of the group 'Employees'

Scenario: As reviewer I can grant permissions based on member properties groups
  Pass Execution  Not implemented yet
  Given a user 'John Doe' with the property 'usertype' = 'employee'
    and a virtual group 'Employees' based on the member property 'usertype' with the value 'employee'
    and a logged-in reviewer
   When I grant the user 'John Doe' the 'edit' permission on a folder
   Then the user 'John Doe' can edit the folder

Scenario: As administrator I can create a group based on multiple member properties
  Pass Execution  Not implemented yet
  Given a user 'John Doe' with the property 'usertype' = 'employee'
    and a user 'Jane Doe' with the property 'city' = 'bonn'
    and a logged-in manager
   When I create a virtual group 'Employees' based on the property 'usertype' = 'employee'
    and I create a virtual group 'Locals' based on the property 'city' = 'bonn'
   Then the user 'John Doe' is member of the group 'Employees'
    and the user 'Jane Doe' is member of the group 'Locals'

Scenario: As administrator I can create a group based on member properties prefixes
  Pass Execution  Not implemented yet
  Given a user 'John Doe' with the property 'student_id' = '1234567'
    and a logged-in manager
   When I create a virtual group 'Students' based on the property 'student' = '123*'
   Then the user 'John Doe' is member of the group 'Students'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in manager
  Pass

a logged-in reviewer
  Pass

a user '${user}' with the property '${property}' = '${value}'
  Pass


# --- WHEN -------------------------------------------------------------------

I create a virtual group '${group}' based on the property '${property}' = '${value}'
  Pass

I grant the user '${user}' the '${permission}' permission on a folder
  Pass


# --- THEN -------------------------------------------------------------------

the user '${user}' is member of the group '${group}'
  Pass

the user '${user}' can edit the folder
  Pass
