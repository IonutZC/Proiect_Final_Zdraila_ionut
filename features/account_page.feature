Feature: Account Page
  @sanity
  Scenario: Check that the URL is correct
    Given I am on the account page
    Then The URL should be "https://magento.softwaretestingboard.com/customer/account/"