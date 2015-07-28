# ============================================================================
# MEMBERPROPERTY TO GROUP ACCEPTANCE TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s pas.plugins.memberpropertytogroup -t test_acceptance.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src pas.plugins.memberpropertytogroup.testing.PAS_PLUGINS_MPTG_PLONE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/pas/plugins/memberpropertytogroup/tests/robot/test_acceptance.robot
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
  Given a user with the property 'usertype' = 'employee'
    and a logged-in manager
   When I create a virtual group 'Employees' with the property 'usertype' = 'employee'
   Then the user is member of the group 'Employees'

Scenario: As reviewer I can grant permissions based on member properties groups
  Pass Execution  Not implemented yet
  Given a user with the property 'usertype' = 'employee'
    and a virtual group 'Employees' with the property 'usertype' = 'employee'
    and a logged-in reviewer
   When I grant the user the 'edit' permission on a folder
   Then the user can edit the folder

Scenario: As administrator I can create a group based on multiple member properties
  Pass Execution  Not implemented yet
  Given a user 'John Doe' with the property 'usertype' = 'employee'
    and a user 'Jane Doe' with the property 'city' = 'bonn'
    and a logged-in manager
   When I create a virtual group 'Employees' with the property 'usertype' = 'employee'
    and I create a virtual group 'Locals' with the property 'city' = 'bonn'
   Then the user 'John Doe' is member of the group 'Employees'
    and the user 'Jane Doe' is member of the group 'Locals'

Scenario: As administrator I can create a group based on member properties prefixes
  Pass Execution  Not implemented yet
  Given a user 'John Doe' with the property 'student_id' = '1234567'
    and a logged-in manager
   When I create a virtual group 'Students' with the property 'student' = '123*'
   Then the user 'John Doe' is member of the group 'Students'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in manager
  Enable Autologin As  Manager

a logged-in reviewer
  Enable Autologin As  Reviewer

a user with the property '${property}' = '${value}'
  Go To  ${PLONE_URL}

a user '${user}' with the property '${property}' = '${value}'
  Go To  ${PLONE_URL}


# --- WHEN -------------------------------------------------------------------

I create a virtual group '${group}' with the property '${property}' = '${value}'
  Go to  ${PLONE_URL}/@@memberpropertytogroup-controlpanel
  Input text  form.widgets.group_property  location
  Input text  form.widgets.valid_groups  employee|employees|Employees|Virtual Employee Group|employee@example.com
  Click button  Save
  Wait until page contains  Changes saved

I grant the user '${user}' the '${permission}' permission on a folder
  Pass


# --- THEN -------------------------------------------------------------------

the user is member of the group '${group}'
  Go To  ${PLONE_URL}/@@usergroup-usermembership?userid=test_user_1_
  Wait until page contains  Current group memberships
  Xpath Should Match X Times  //table[@summary='Group Memberships Listing']//tr/td//*[text()[contains(., '${group}')]]  1

the user '${user}' can edit the folder
  Pass
