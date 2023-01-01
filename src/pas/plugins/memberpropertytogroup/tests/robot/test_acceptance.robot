# ============================================================================
# MEMBERPROPERTY TO GROUP ACCEPTANCE TESTS
# ============================================================================

*** Variables ***

${BROWSER}  chrome


*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***

Scenario: As administrator I can create a group based on member properties
  Given a user with the property 'usertype' = 'employee'
    and a logged-in manager
   When I create a virtual group 'Employees' with the property 'usertype' = 'employee'
   Then the user is member of the group 'Employees'

Scenario: As reviewer I can grant permissions based on member properties groups
  Given a user with the property 'usertype' = 'employee'
    and a virtual group 'Employees' with the property 'usertype' = 'employee'
    and a logged-in manager
   When I grant the virtual group 'Employees' the 'Edit' permission on a folder
   Then the user can edit the folder

Scenario: As administrator I can create a group based on multiple member properties
  # Pass Execution  Not implemented yet
  Given a user 'John Doe' with the property 'usertype' = 'employee'
    and a user 'Jane Doe' with the property 'city' = 'bonn'
    and a logged-in manager
   When I create a virtual group 'Employees' with the property 'usertype' = 'employee'
    and I add another virtual group 'Locals' with the property 'city' = 'bonn' in slot 1
   Then the user 'John Doe' is member of the group 'Employees'
    and the user 'Jane Doe' is member of the group 'Locals'

Scenario: As administrator I can create a group based on member properties prefixes
  Given a user with the property 'student_id' = '1234567'
    and a logged-in manager
   When I create a virtual group 'Students' with the property 'student_id' = '123*'
   Then the user is member of the group 'Students'


*** Keywords ***

# --- Given ------------------------------------------------------------------

a logged-in manager
  Enable Autologin As  Manager

a logged-in reviewer
  Enable Autologin As  Reviewer

a user with the property '${property}' = '${value}'
  Go To  ${PLONE_URL}

a user '${user}' with the property '${property}' = '${value}'
  Go To  ${PLONE_URL}

a virtual group '${group}' with the property '${property}' = '${value}'
  Enable autologin as  Manager
  Go to  ${PLONE_URL}/@@memberpropertytogroup-controlpanel
  Click button  Add property
  Input text  form.widgets.group_property  ${property}
  Input text  form.widgets.valid_groups  ${value}|${group}|${group}|${group} (Virtual Group)|my-virtual-group@example.com
  Execute Javascript	window.scrollTo(0,document.body.scrollHeight);
  Click Button  Save
  Wait until page contains  Changes saved


# --- WHEN -------------------------------------------------------------------

I create a virtual group '${group}' with the property '${property}' = '${value}'
  Go to  ${PLONE_URL}/@@memberpropertytogroup-controlpanel
  Click button  Add property
  Input text  form.widgets.group_property  ${property}
  Input text  form.widgets.valid_groups  ${value}|${group}|${group}|${group} (Virtual Group)|my-virtual-group@example.com
  Capture screenshot  memberpropertytogroup-controlpanel-${group}.png
  Execute Javascript	window.scrollTo(0,document.body.scrollHeight);
  Click Button  Save
  Wait until page contains  Changes saved

I add another virtual group '${group}' with the property '${property}' = '${value}' in slot ${slot}
  Go to  ${PLONE_URL}/@@memberpropertytogroup-controlpanel
  Execute Javascript	window.scrollTo(0,document.body.scrollHeight);
  Click button  Add property
  Input text  form.widgets.group_property_${slot}  ${property}
  Input text  form.widgets.valid_groups_${slot}  ${value}|${group}|${group}|${group} (Virtual Group)|my-virtual-group@example.com
  Capture screenshot  memberpropertytogroup-controlpanel-${group}.png
  Execute Javascript	window.scrollTo(0,document.body.scrollHeight);
  Click Button  Save
  Wait until page contains  Changes saved

I grant the virtual group '${group}' the 'Edit' permission on a folder
  Create content  type=Folder  id=folder  title=Folder
  Go to  ${PLONE_URL}/folder/@@sharing
  Wait until page contains element  css=#sharing-user-group-search
  Input text  css=#sharing-user-group-search  ${group}
  Click button  css=#sharing-search-button
  Wait until page contains element  xpath=//table[@id='user-group-sharing']//td[@title='${group}']
  Select checkbox  xpath=//table[@id='user-group-sharing']//td[@title='${group}']/following-sibling::td[2]/input
  Capture screenshot  grant-virtual-group-permission-on-folder.png
  # XXX after capture the selection was reset: select again
  Select checkbox  xpath=//table[@id='user-group-sharing']//td[@title='${group}']/following-sibling::td[2]/input
  Execute Javascript	window.scrollTo(0,document.body.scrollHeight);
  Click Button  Save
  Wait until page contains  Changes saved


# --- THEN -------------------------------------------------------------------

the user is member of the group '${group}'
  Go To  ${PLONE_URL}/@@usergroup-usermembership?userid=test_user_1_
  Wait until page contains  Current group memberships
  Page Should Contain Element  //table[@summary='Group Memberships Listing']//tr/td//*[text()[contains(., '${group}')]]  limit=1
  Capture screenshot  the-user-is-member-of-the-group-${group}.png

the user ${user} is member of the group '${group}'
  Go To  ${PLONE_URL}/@@usergroup-usermembership?userid=test_user_1_
  Wait until page contains  Current group memberships
  Page Should Contain Element  //table[@summary='Group Memberships Listing']//tr/td//*[text()[contains(., '${group}')]]  limit=1
  Capture screenshot  the-user-JohnDoe-is-member-of-the-group-${group}.png

the user can edit the folder
  Disable autologin
  Enable autologin as  test_user_1_
  Go to  ${PLONE_URL}/folder
  Wait until page contains  Edit
  Click element  xpath=//*[contains(text(), 'Edit')]
  Wait until page contains  Site Map
  Page should contain  Edit
  Page should contain element  xpath=//*[@value='Save']
  Capture screenshot  the-user-can-edit-the-folder.png


# --- HELPER -----------------------------------------------------------------

Capture screenshot
  [Arguments]  ${filename}
  # Base path is './test_acceptance/Scenario_[...]/
  Set Window Size  1920  1080
  Capture Page Screenshot  filename=../../docs/source/_screenshots/${filename}
