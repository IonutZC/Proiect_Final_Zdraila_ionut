from behave import *


@Given('I am on the register page')
def step_impl(context):
    context.register_page.open()


@Then('The URL should be "https://magento.softwaretestingboard.com/customer/account/create/"')
def step_impl(context):
    context.register_page.is_url_correct("https://magento.softwaretestingboard.com/customer/account/create/")


@When("The register button is displayed")
def step_impl(context):
    context.register_page.is_register_button_displayed()


@When('I click register button')
def step_impl(context):
    context.register_page.click_register_button()


@Then('The first name error is displayed')
def step_impl(context):
    assert context.register_page.first_name_error_is_displayed(), f'First name error not displayed'


@Then('The last name error is displayed')
def step_impl(context):
    assert context.register_page.last_name_error_is_displayed(), f'Last name error not displayed'


@Then('The register email error is displayed')
def step_impl(context):
    assert context.register_page.register_email_error_is_displayed(), f'Register email error not displayed'


@Then('The password error is displayed')
def step_impl(context):
    assert context.register_page.register_password_error_is_displayed()


@Then('The confirm password is displayed')
def step_impl(context):
    assert context.register_page.confirm_password_error_is_displayed()


@When('I enter "{email}" in the register email input')
def step_impl(context, email):
    context.register_page.set_register_email(email)


@Then('I should see this "Please enter a valid email address (Ex: johndoe@domain.com)." error message')
def step_impl(context):
    assert context.register_page.register_email_error_is_displayed()
    assert context.register_page.register_email_error_message_contains_text(
        "Please enter a valid email address (Ex: johndoe@domain.com).")


@When('I enter "{password}" in register password input')
def step_impl(context, password):
    context.register_page.set_register_password(password)


@When('I enter "{confirm_password}" in the confirm password input')
def step_impl(context, confirm_password):
    context.register_page.set_confirm_password(confirm_password)


@Then('I should see "Please enter the same value again." error message')
def step_impl(context):
    assert context.register_page.confirm_password_error_is_displayed(), f'Error not displayed'
    assert context.register_page.confirm_password_error_message_contains_text('Please enter the same value again.')
