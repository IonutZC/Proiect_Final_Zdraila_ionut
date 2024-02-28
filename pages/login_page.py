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

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        self.type(self.INPUT_EMAIL, email)

    def set_password(self, password):
        self.type(self.INPUT_PASSWORD, password)

    def click_login_button(self):
        self.find(self.BUTTON_LOGIN).click()

    def main_error_message_is_displayed(self):
        return self.find(self.ERROR_MESSAGE).is_displayed()

    def main_error_message_contains_text(self, text):
        return text in self.get_text(self.ERROR_MESSAGE)

    def email_error_message_is_displayed(self):
        return self.find(self.INVALID_EMAIL_MESSAGE).is_displayed()

    def email_error_message_contains_text(self, text):
        return text in self.get_text(self.INVALID_EMAIL_MESSAGE)









