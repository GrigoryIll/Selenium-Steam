from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class TopSellers(BasePage):

    CHECKBOX_OS = (
        "xpath", "//span[contains(@data-loc, 'SteamOS + Linux')]")
    CHECKBOX_LAN_COOP = (
        "xpath", "//*[contains(@class, 'tab_filter_control_row') and @data-loc='LAN Co-op']")
    NUM_PLAYERS_MENU = (
        "xpath", "//*[text()='Narrow by number of players']")
    CHECKBOX_ACTION = (
        "xpath", "//*[contains(@class, 'tab_filter_control_row') and @data-loc='Action']")
    GENRE_TAG_MENU = (
        "xpath", "//*[text()='Narrow by tag']")
    CHECKBOX_INDIE = (
        "xpath", "//*[contains(@class, 'tab_filter_control_row') and @data-loc='Indie']")
    SEARCH_RESULT_LIST = (
        "xpath", "//*[contains(@class, 'search_result_row')]")
    SEARCH_RESULT_QTY = ("xpath", "//*[@class='search_results_count']")
    FIRST_GAME_NAME = (
        "xpath", "//*[@id='search_resultsRows']/a//*[@class='title']")
    FIRST_GAME_YEAR = (
        "xpath", "//a//*[contains(@class, 'col search_released')]")
    FIRST_GAME_PRICE = (
        "xpath", "//a//*[@class='discount_final_price']")
    NUM_PLAYERS_MENU_OPENED = (
        "xpath", "//*[@class='block_content block_content_inner' and @style='display: block;']")
    UNIQUE_ELEMENT = (
        "xpath", "//*[@role='button']//*[text()='Narrow by Price']")

    def select_checkbox_os(self):
        element = self.wait.until(EC.presence_of_element_located(
            self.CHECKBOX_OS))
        self.scroll.scroll_to_element(element)
        self.wait.until(EC.element_to_be_clickable(
            self.CHECKBOX_OS)).click()

    def is_checkbox_os_selected(self):
        element = self.wait.until(EC.element_to_be_clickable(
            self.CHECKBOX_OS))
        if "checked" in element.get_attribute("class"):
            return True
        else:
            return False

    def open_num_players_menu(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.NUM_PLAYERS_MENU))
        element.click()

    def select_checkbox_LAN_COOP(self):
        self.wait.until(EC.presence_of_element_located(
            self.NUM_PLAYERS_MENU_OPENED))
        element = self.wait.until(EC.element_to_be_clickable(
            self.CHECKBOX_LAN_COOP))
        element.click()

    def is_checkbox_LAN_COOP_selected(self):
        element = self.wait.until(EC.visibility_of_element_located(
            self.CHECKBOX_LAN_COOP))
        if "checked" in element.get_attribute("class"):
            return True
        else:
            return False

    def select_checkbox_indie(self):
        element = self.wait.until(EC.element_to_be_clickable(
            self.CHECKBOX_INDIE))
        element.click()

    def select_checkbox_action(self):
        element = self.wait.until(EC.element_to_be_clickable(
            self.CHECKBOX_ACTION))
        element.click()

    def is_action_checkbox_selected(self):
        element = self.wait.until(EC.visibility_of_element_located(
            self.CHECKBOX_ACTION))
        if "checked" in element.get_attribute("class"):
            return True
        else:
            return False

    def games_search_result_list(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(self.SEARCH_RESULT_LIST))
        return len(elements)

    def games_search_result_qty(self):
        element = self.wait.until(EC.visibility_of_element_located(
            self.SEARCH_RESULT_QTY))
        element.is_displayed()
        element = element.text
        games_qty = ""
        for symbol in element:
            if not symbol.isdigit():
                continue
            else:
                games_qty += symbol
        return int(games_qty)

    def first_game_info(self):
        first_game_name = self.wait.until(
            EC.presence_of_element_located(self.FIRST_GAME_NAME)).text
        first_game_year = self.wait.until(
            EC.presence_of_element_located(self.FIRST_GAME_YEAR)).text.strip()
        first_game_price = self.wait.until(
            EC.presence_of_element_located(self.FIRST_GAME_PRICE)).text
        info_dict = {}
        info_dict["name"] = first_game_name
        info_dict["year"] = first_game_year
        info_dict["price"] = first_game_price
        return info_dict

    def click_on_first_game(self):
        self.wait.until(EC.element_to_be_clickable(
            self.FIRST_GAME_NAME)).click()
