from browser import Browser


class BasePage(Browser):
    pass

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
