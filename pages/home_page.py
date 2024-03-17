from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    HOME_PAGE_URL = "https://magento.softwaretestingboard.com/"
    SEARCH_BAR = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[title='Search']")
    PRODUCT = (By.CSS_SELECTOR, ".product.name.product-item-name")

    def open(self):
        self.driver.get(self.HOME_PAGE_URL)
        assert self.HOME_PAGE_URL == "https://magento.softwaretestingboard.com/"

    def search_bar_is_displayed(self):
        assert self.find(self.SEARCH_BAR).is_displayed(), 'Search bar not displayed'

    def type_therm(self, therm):
        self.type(self.SEARCH_BAR, therm)

    def check_number_of_elements_after_search(self, expected_num):
        product_list = self.wait_for_elements(self.PRODUCT)
        assert len(product_list) == int(
            expected_num), f"Expected {expected_num} elements, but found {len(product_list)}."

    def click_search_button(self):
        self.find(self.SEARCH_BUTTON).click()
