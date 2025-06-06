Feature: Filter Functionality

Scenario: Checking Filters in the Conditioner Page
  Given the user is on the Conditioner Page
  When User clicks on the sort by Name A-Z
  And User clicks on the sort by Name Z-A
  When User clicks on the sort by Price Low > High
  And User clicks on the sort by Price High > Low
  When User clicks on the sort by Rating Highest
  And User clicks on the sort by Rating Lowest
  When User clicks on the sort by Date New>Old
  And User clicks on the sort by Date Old>New
  Then User can edit any Filters
