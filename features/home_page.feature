Feature: Home Page
  @sanity
  Scenario: Check that the URL is correct
    Given I m on the home page
    Then The URL of the home page is "https://magento.softwaretestingboard.com/"