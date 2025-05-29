from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AboutPage(BasePage):

    STORE = (
        "xpath", "//*[@aria-label='Global Menu']//*[@data-tooltip-content='.submenu_Store']")
    ONLINE_PLAYERS = ("xpath", "//*[@class='online_stat']")
    PLAYERS_NOW = ("xpath", "//*[@class='online_stat']")
    NEW_AND_NOTEWORTHY = (
        "xpath", "//*[@id='noteworthy_tab']//*[@class='pulldown_desktop']")
    TOP_SELLERS = (
        "xpath", "//*[@class='popup_menu_item' and contains(text(), 'Sellers')]")
    UNIQUE_ELEMENT = ("xpath", "//*[@class='online_stat']")

    def get_online_players(self):
        self.wait.until(EC.presence_of_all_elements_located(
            self.ONLINE_PLAYERS))
        all_elements = self.driver.find_elements(*self.ONLINE_PLAYERS)
        online_players = ""
        for el in all_elements:
            if "ONLINE" in el.text:
                for symbol in el.text:
                    if not symbol.isdigit():
                        continue
                    else:
                        online_players += symbol
        return int(online_players)

    def get_players_now(self):
        self.wait.until(EC.presence_of_all_elements_located(
            self.PLAYERS_NOW))
        all_elements = self.driver.find_elements(*self.PLAYERS_NOW)
        players_now = ""
        for el in all_elements:
            if "PLAYING NOW" in el.text:
                for symbol in el.text:
                    if not symbol.isdigit():
                        continue
                    else:
                        players_now += symbol
        return int(players_now)

    def click_store_button(self):
        self.wait.until(EC.element_to_be_clickable(self.STORE)).click()

    def click_top_sellers(self):
        self.wait.until(EC.element_to_be_clickable(
            self.NEW_AND_NOTEWORTHY)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.TOP_SELLERS)).click()
