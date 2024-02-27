Feature: Register Page
  Scenario: Check that the URL is correct
    Given I am on the register page
    Then The URL should be "https://magento.softwaretestingboard.com/customer/account/create/"

  Scenario: Trying to register without completing require fields check that the errors are displayed
    Given I am on the register page
    When I enter "email" in the register email input
    Then The register button is displayed
    Then I click register button
