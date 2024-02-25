from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time



class RegisterPage(BasePage):
    REGISTER_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    REGISTER_BUTTON = (By.CLASS_NAME, "primary")
    REGISTER_EMAIL_INPUT = (By.ID, "email_address")
    def open(self):
        self.driver.get(self.REGISTER_PAGE_URL)
        time.sleep(6)


    def is_register_button_displayed(self):
       return self.find(self.REGISTER_BUTTON).is_displayed()


    def click_register_button(self):
        self.find(self.REGISTER_BUTTON).click()

    def set_register_email(self, email):
        self.type(self.REGISTER_EMAIL_INPUT, email)




