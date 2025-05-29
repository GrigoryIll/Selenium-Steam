from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_config.scrolls import Scrolls


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)
        self.scroll = Scrolls(driver)

    def is_opened(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.UNIQUE_ELEMENT))
        return element.is_displayed()
