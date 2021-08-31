Changelog
=========

2.1.1 (2021-08-31)
------------------

- Fix property matching.
  [ericof]


2.1.0 (2021-08-31)
------------------

- Property matching now supports '*' both in the start and in the end of the value.
  [ericof]


2.0.0 (2021-07-21)
------------------

- Plone 5.2 compatibility.
  [timo]

- Drop Python 2, Plone < 5.2 compatibility.
  [ericof]

- Implement package uninstall (#12).
  [ericof]


1.1 (2018-03-05)
----------------

- Plone 5.1 compatibility.
  [timo]

- Make plugins (by default inactive) ``getGroupMembers`` pluggable, so that
  integrators may provide its own utility providing new ``IGetGroupMembers``
  interface promising to return the actual group members.
  [jensens]


1.0 (2016-04-04)
----------------

- Identical to 1.0a7.
  [timo]


1.0a7 (2015-10-25)
------------------

- Control panel markup and JS refactoring.
  [sneridagh]


1.0a6 (2015-10-21)
------------------

- Plone 3 compatibility fixes.
  [csenger]


1.0a5 (2015-10-21)
------------------

- Fix js to work with Plone 3.
  [csenger]

- Move add/remove buttons in controlpanel above the save/cancel buttons.
  [csenger]


1.0a4 (2015-10-19)
------------------

- Add upgrade step for registry entries that have been added in 1.0a3.
  [timo]


1.0a3 (2015-10-12)
------------------

- New feature: As administrator I can create a group based on multiple member properties.
  [sneridagh]


1.0a2 (2015-09-09)
------------------

- Fix Scenario: As administrator I can create a group based on member
  properties prefixes
  [jensens]

- Ignore empty lines in controlpanel input.
  [jensens]


1.0a1 (2015-08-06)
------------------

- Initial release.
  [timo, jensens]
