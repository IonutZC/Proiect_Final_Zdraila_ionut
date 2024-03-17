from behave import *


@given('I m on the home page')
def step_impl(context):
    context.home_page.open()


@then('The URL of the home page is "{url}"')
def step_impl(context, url):
    context.home_page.is_url_correct(url)


@then('The search bar is displayed')
def step_impl(context):
    context.home_page.search_bar_is_displayed()


@when('I enter "{therm}" in search bar')
def step_impl(context, therm):
    context.home_page.type_therm(therm)


@when('I click search button')
def step_impl(context):
    context.home_page.click_search_button()


@then('I should see "{expected_count}" elements')
def step_impl(context, expected_count):
    context.home_page.check_number_of_elements_after_search(expected_count)
