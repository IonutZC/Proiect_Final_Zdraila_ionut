from browser import Browser
from pages.login_page import LoginPage
from pages.home_page import HomePage
# from pages.register_page import RegisterPage
from pages.account_page import AccountPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.home_page = HomePage()
    # context.register_page = RegisterPage()
    context.account_page = AccountPage()


def after_all(context):
    context.browser.close()