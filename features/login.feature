Feature: Login Page
  Background:
    Given I am on the login page

  @sanity
  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the page is "https://magento.softwaretestingboard.com/customer/account/login"

#  Scenario: Login without credential
#    When I click the login button
#    Then The email  error is displayed
#    And Password error is displayed



  @negative
  Scenario Outline: Login with unregistered credentials
    When I enter "<email>" in the email input
    And I enter "<password>" in password input
    And  I click the login button
    Then i should see "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." message
    Examples:
      | email           | password  |
      | test1@gmail.com | 123456789 |
      | test2@gmail.com | 987654321 |
      | test3@gmail.com | 112233445 |

    @negative
  Scenario: Login with invalid email
    When I enter "email" in the email input
    And I enter "password" in password input
    And  I click the login button
    Then I should see "Please enter a valid email address (Ex: johndoe@domain.com)."


