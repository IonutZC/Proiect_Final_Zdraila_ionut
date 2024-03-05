Feature: Register Page
  Background:
    Given I am on the register page

  @sanity
  Scenario: Check that the URL is correct
    Then The URL should be "https://magento.softwaretestingboard.com/customer/account/create/"

  @negative
  Scenario: Trying to register without completing require fields check that the errors are displayed
    When The register button is displayed
    And I click register button
    Then The first name error is displayed
    And The last name error is displayed
    And The register email error is displayed
    And The password error is displayed
    And The confirm password is displayed

  @negative
  Scenario: Trying to register with invalid email displays error
    When I enter "email" in the register email input
    And I click register button
    Then I should see this "Please enter a valid email address (Ex: johndoe@domain.com)." error message

  @negative
  Scenario Outline: Trying to register with different passwords displays errors
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

@positive
Scenario: Register by completing required fields with valid  data
  When I enter "PYTA10" in the first name input
  And I enter "ITFactory" in the last name input
  And I enter a unique email in the register email input
  And I enter "Test912345678" in register password input
  And I enter "Test912345678" in the confirm password input
  And I click register button
  Then The success message is displayed
  And I should see "Thank you for registering with Main Website Store." success message






