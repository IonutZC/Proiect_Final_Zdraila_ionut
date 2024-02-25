from behave import *


@given('I am on the  account page')
def step_impl(context):
    context.account_page.open()


@then('The URL should be  "https://magento.softwaretestingboard.com/customer/account"')
def step_impl(context):
    assert context.account_page.is_url_correct("https://magento.softwaretestingboard.com/customer/account")