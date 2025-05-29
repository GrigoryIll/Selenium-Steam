from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class TopSelling(BasePage):

    MORE_TOP_SELLERS = (
        "xpath", "//*[@class='DialogButton _DialogLayout Primary Focusable']")
    UNIQUE_ELEMENT = (
        "xpath", "//*[@class='DialogButton _DialogLayout Primary Focusable']")

    def click_more_top_sellers(self):
        element = self.wait.until(EC.presence_of_element_located(
            self.MORE_TOP_SELLERS))
        self.scroll.scroll_to_element(element)
        self.wait.until(EC.element_to_be_clickable(
            self.MORE_TOP_SELLERS)).click()
