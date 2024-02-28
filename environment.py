from browser import Browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.register_page import RegisterPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.home_page = HomePage()
    context.account_page = AccountPage()
    context.register_page = RegisterPage()


def after_all(context):
    context.browser.close()
