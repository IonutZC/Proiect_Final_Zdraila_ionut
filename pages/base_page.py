from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(Browser):

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def message_error_is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def is_url_correct(self, expected_url):
        return self.driver.current_url == expected_url

    def wait_for_elements(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []
