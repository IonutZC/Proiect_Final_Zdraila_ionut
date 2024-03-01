import random

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class RegisterPage(BasePage):
    REGISTER_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    REGISTER_EMAIL_INPUT = (By.ID, "email_address")
    REGISTER_PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "password-confirmation")
    FIRST_NAME_ERROR = (By.ID, "firstname-error")
    LAST_NAME_ERROR = (By.ID, "lastname-error")
    REGISTER_EMAIL_ERROR = (By.ID, "email_address-error")
    REGISTER_PASSWORD_ERROR = (By.ID, "password-error")
    CONFIRM_PASSWORD_ERROR = (By.ID, "password-confirmation-error")
    SUCCESS_REGISTER_MESSAGE = (By.CLASS_NAME, "message-success")

    REGISTER_BUTTON = (By.CLASS_NAME, "primary")

    def open(self):
        self.driver.get(self.REGISTER_PAGE_URL)
        # time.sleep(6)

    def is_register_button_displayed(self):
        return self.find(self.REGISTER_BUTTON).is_displayed()

    def click_register_button(self):
        self.find(self.REGISTER_BUTTON).click()

    def first_name_error_is_displayed(self):
        return self.find(self.FIRST_NAME_ERROR).is_displayed()

    def last_name_error_is_displayed(self):
        return self.find(self.LAST_NAME_ERROR).is_displayed()

    def register_email_error_is_displayed(self):
        return self.find(self.REGISTER_EMAIL_ERROR).is_displayed()

    def register_password_error_is_displayed(self):
        return self.find(self.REGISTER_PASSWORD_ERROR).is_displayed()

    def confirm_password_error_is_displayed(self):
        return self.find(self.CONFIRM_PASSWORD_ERROR).is_displayed()
# Set inputs

    def set_first_name(self, first_name):
        self.type(self.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)

    def set_register_email(self, email):
        self.type(self.REGISTER_EMAIL_INPUT, email)

    def set_unique_register_email(self):
        number = random.randint(0, 9999999999999999999999)
        register_email = f'ITFactory.PYTA10{number}@gmail.info'
        self.set_register_email(register_email)

    def set_register_password(self, password):
        self.type(self.REGISTER_PASSWORD_INPUT, password)

    def set_confirm_password(self, confirm_password):
        self.type(self.CONFIRM_PASSWORD_INPUT, confirm_password)


# Errors
    def register_email_error_message_contains_text(self, text):
        return text in self.get_text(self.REGISTER_EMAIL_ERROR)

    def confirm_password_error_message_contains_text(self, text):
        return text in self.get_text(self.CONFIRM_PASSWORD_ERROR)

# Success message
    def success_register_message_is_displayed(self):
        return self.find(self.SUCCESS_REGISTER_MESSAGE).is_displayed()

    def success_register_message_test(self, text):
        return text == self.get_text(self.SUCCESS_REGISTER_MESSAGE)





