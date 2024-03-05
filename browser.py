from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class Browser:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.close()
