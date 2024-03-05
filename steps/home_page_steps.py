from behave import *

@given('I m on the home page')
def step_impl(context):
    context.home_page.open()

@then('The URL of the page is "{url}"')
def step_impl(context, url):
    context.home_page.is_url_correct(url)