# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
# import time
#
# class RegisterPage(BasePage):
#     ERROR_FIRST_NAME = (By.ID, "firstname-error")
#     ERROR_LAST_NAME = (By.ID, "lastname-error")
#     ERROR_EMAIL = (By.ID, "email_address-error")
#     ERROR_PASSWORD = (By.ID, "email_address-error")
#     ERROR_CONFIRM_PASSWORD = (By.ID, "password-confirmation-error")
#     INPUT_REGISTER_FIRST_NAME = (By.ID, "firstname")
#     INPUT_REGISTER_LAST_NAME = (By.ID, "lastname")
#     INPUT_REGISTER_EMAIL = (By.ID, "email_address")
#     INPUT_REGISTER_PASSWORD = (By.ID, "password")
#     INPUT_REGISTER_CONFIRM_PASSWORD = (By.ID, "password_confirmation")
#     REGISTER_BUTTON = (By.CSS_SELECTOR, "div.primary button.action.submit.primary")
#     REGISTER_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/create"
#
#
#
#     def open(self):
#         self.driver.get(self.REGISTER_PAGE_URL)
#         time.sleep(10)
#
#     def set_email(self, email):
#         self.type(self.INPUT_REGISTER_EMAIL, email)
#
#     def click_register_button(self):
#         self.find(self.REGISTER_BUTTON).click()
#
#     def is_first_name_error_displayed(self):
#         return self.find(self.ERROR_FIRST_NAME).is_displayed()
#
#     def is_last_name_error_displayed(self):
#         return self.find(self.ERROR_LAST_NAME_NAME).is_displayed()
#
#     def is_email_error_displayed(self):
#         return self.find(self.ERROR_EMAIL).is_displayed()
#
#     def is_password_error_displayed(self):
#         return self.find(self.ERROR_PASSWORD).is_displayed()
#
#     def is_confirm_password_error_displayed(self):
#         return self.find(self.ERROR_CONFIRM_PASSWORD).is_displayed()
#
#
#
