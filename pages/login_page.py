from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login"
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "pass")
    BUTTON_LOGIN = (By.ID, "send2")
    ERROR_MESSAGE = (By.CLASS_NAME, "message-error")
    INVALID_EMAIL_MESSAGE = (By.ID, "email-error")
    WELCOME_MESSAGE = (By.CLASS_NAME, "customer-welcome")
    PASSWORD_ERROR = (By.ID, "pass-error")

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)
        assert self.LOGIN_PAGE_URL == "https://magento.softwaretestingboard.com/customer/account/login", "Incorrect URL"

    def set_email(self, email):
        self.type(self.INPUT_EMAIL, email)

    def set_password(self, password):
        self.type(self.INPUT_PASSWORD, password)

    def click_login_button(self):
        self.find(self.BUTTON_LOGIN).click()

    def main_error_message_is_displayed(self):
        assert self.message_error_is_displayed(self.ERROR_MESSAGE), "Error message not displayed "

    def main_error_message_contains_text(self, text):
        assert text in self.get_text(self.ERROR_MESSAGE), "Incorrect text message"

    def email_error_message_is_displayed(self):
        assert self.message_error_is_displayed(self.INVALID_EMAIL_MESSAGE), "Email error not displayed"

    def password_error_message_is_displayed(self):
        assert self.message_error_is_displayed(self.PASSWORD_ERROR), "Password error not displayed"

    def email_error_message_contains_text(self, text):
        assert text in self.get_text(self.INVALID_EMAIL_MESSAGE), "Incorrect error message "
