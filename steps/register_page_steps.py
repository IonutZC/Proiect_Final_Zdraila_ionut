from behave import *


@Given('I am on the register page')
def step_impl(context):
    context.register_page.open()


@Then('The URL should be "https://magento.softwaretestingboard.com/customer/account/create/"')
def step_impl(context):
    context.register_page.is_url_correct("https://magento.softwaretestingboard.com/customer/account/create/")


@Then("The register button is displayed")
def step_impl(context):
    context.register_page.is_register_button_displayed()


@Then('I click register button')
def step_impl(context):
    context.register_page.click_register_button()

@When('I enter "email" in the register_email input')
def step_impl(context, email):
    context.login_page.set_register_email(email)

