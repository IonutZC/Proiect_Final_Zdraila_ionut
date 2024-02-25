from behave import *


@given('I am on the login page')
def step_impl(context):
    context.login_page.open()


@then('The URL of the page is "{url}"')
def step_impl(context, url):
    assert context.login_page.is_url_correct(url), "Incorrect url"


@when('I enter "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I enter "{password}" in password input')
def step_impl(context, password):
    context.login_page.set_password(password)


@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I should see "Please enter a valid email address (Ex: johndoe@domain.com)."')
def step_impl(context):
    assert context.login_page.email_error_message_is_displayed(), "Error message not displayed"
    assert (context.login_page.email_error_message_contains_text
            ("Please enter a valid email address (Ex: johndoe@domain.com)."))


@then('i should see "The account sign-in was incorrect or your account is disabled temporarily.'
      ' Please wait and try again later." message')
def step_impl(context):
    assert context.login_page.main_error_message_is_displayed(), "Error message not displayed"
    assert (context.login_page.main_error_message_contains_text
            ("The account sign-in was incorrect or your account is disabled temporarily."
             " Please wait and try again later."))

@then ('"Cutomer-Welcome" should be displeyed')
def step_impl(context):
    assert context.login_page.customer_panel_displayed(), "The panel is not displayed"

