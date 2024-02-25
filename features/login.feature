Feature: Login Page

  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the page is "https://magento.softwaretestingboard.com/customer/account/login"

  Scenario: Login without credential
    Given I am on the login page
    When I click the login button




  Scenario: Login with invalid email
    Given I am on the login page
    When I enter "email" in the email input
    And I enter "password" in password input
    And  I click the login button
    Then I should see "Please enter a valid email address (Ex: johndoe@domain.com)."



  Scenario Outline: Login with unregistered credentials
    Given I am on the login page
    When I enter "<email>" in the email input
    And I enter "<password>" in password input
    And  I click the login button
    Then i should see "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." message
    Examples:
      | email           | password  |
      | test1@gmail.com | 123456789 |
      | test2@gmail.com | 987654321 |
      | test3@gmail.com | 112233445 |


  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter "testItFactory@gmail.com" in the email input
    And I enter "Test123456" in password input
    And  I click the login button
    Then "Cutomer-Welcome" should be displeyed

