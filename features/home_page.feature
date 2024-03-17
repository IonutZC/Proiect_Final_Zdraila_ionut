Feature: Home Page

  @sanity
  Scenario: Check that the URL is correct
    Given I m on the home page
    Then The URL of the home page is "https://magento.softwaretestingboard.com/"

  @positive
  Scenario: Check that the search bar is displayed
    Given I m on the home page
    Then The search bar is displayed

  @positive
  Scenario Outline: Check the number of items displayed after search
    Given I m on the home page
    When  I enter "<therm>" in search bar
    And I click search button
    Then I should see "<expected_count>" elements
    Examples:
      | therm      | expected_count |
      | Sweatshirt | 11             |
      | shirt      | 5              |
      | tops       | 4              |
