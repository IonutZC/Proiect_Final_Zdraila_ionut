from behave import *

@given('I m on the home page')
def step_impl(context):
    context.home_page.open()

@then('The URL of the page is "https://magento.softwaretestingboard.com/"')
def step_impl(context):
    context.home_page.is_url_correct("https://magento.softwaretestingboard.com/")