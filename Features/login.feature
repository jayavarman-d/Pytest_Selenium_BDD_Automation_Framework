Feature: Login Functionality

  Background: User opens the website

  Scenario Outline: Login Invalid (credential mismatch)
    Given User is on the login page
    When User enters invalid Username "<username>"
    And User enters invalid Password "<password>"
    When User Clicks signin button

    Examples:
      | username | password |
      | Demo     | demo866  |
      | trial    | trial__  |

  Scenario: Valid Login
    Given User is on the login page
    When User enters valid Username
    When User enters valid Password
    When User Clicks signin button
    Then Page will be redirected to customer Account page
