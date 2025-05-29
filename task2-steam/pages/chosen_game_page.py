from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ChosenGame(BasePage):

    CHOSEN_GAME_NAME = ("xpath", "//*[@id='appHubAppName']")
    CHOSEN_GAME_YEAR = ("xpath", "//*[@class='date']")
    CHOSEN_GAME_PRICE = ("xpath", "//*[@class='discount_final_price']")
    UNIQUE_ELEMENT = ("xpath", "//span[text()='Community Hub']")

    def chosen_game_info(self):
        chosen_game_name = self.wait.until(
            EC.presence_of_element_located(self.CHOSEN_GAME_NAME)).text
        chosen_game_year = self.wait.until(
            EC.presence_of_element_located(self.CHOSEN_GAME_YEAR)).text
        chosen_game_price = self.wait.until(
            EC.presence_of_element_located(self.CHOSEN_GAME_PRICE)).text.replace(".", "")
        info_dict = {}
        info_dict["name"] = chosen_game_name
        info_dict["year"] = chosen_game_year
        info_dict["price"] = chosen_game_price
        return info_dict
