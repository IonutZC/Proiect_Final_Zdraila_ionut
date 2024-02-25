from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):
    ACCOUNT_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account"

    def open(self):
        self.driver.get(self.ACCOUNT_PAGE_URL)
