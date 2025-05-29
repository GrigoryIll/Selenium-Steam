from base.base_page import BasePage
from data_config.json_utility import JsonUtility
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = JsonUtility.value_from_json("links.main")
    ABOUT = (
        "xpath", "//*[@class='supernav_container']//*[contains(text(), 'About')]")
    UNIQUE_ELEMENT = (
        "xpath", "//*[@class='home_page_gutter_top']")

    def open(self):
        self.driver.get(self.PAGE_URL)

    def click_about_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ABOUT)).click()
