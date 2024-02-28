Feature: Register Page
  Scenario: Check that the URL is correct
    Given I am on the register page
    Then The URL should be "https://magento.softwaretestingboard.com/customer/account/create/"

  Scenario: Trying to register without completing require fields check that the errors are displayed
    Given I am on the register page
    When The register button is displayed
    And I click register button
    Then The first name error is displayed
    And The last name error is displayed
    And The register email error is displayed
    And The password error is displayed
    And The confirm password is displayed

  Scenario: Trying to register with invalid email displays error
    Given I am on the register page
    When I enter "email" in the register email input
    And I click register button
    Then I should see this "Please enter a valid email address (Ex: johndoe@domain.com)." error message


  Scenario Outline: Trying to register with different passwords displays errors
    Given I am on the register page
    When I enter "<password>" in register password input
    And I enter "<confirm_password>" in the confirm password input
    And I click register button
    Then I should see "Please enter the same value again." error message
    Examples:
      | password    | confirm_password |
      | Test612423  | test123          |
      | Test816556  | test78569        |
      | Test5216846 | 12345678901      |
      | Test8888555 | 95621452585      |







