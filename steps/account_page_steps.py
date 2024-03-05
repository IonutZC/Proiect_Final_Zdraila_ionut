from behave import *

@Given('I am on the account page')
def step_impl(context):
    context.account_page.open()

@Then('The URL of the account page should be "{url}"')
def step_impl(context, url):
    context.account_page.is_url_correct(url)