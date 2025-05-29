import pytest
from pages.main_page import MainPage
from pages.about_page import AboutPage
from pages.top_selling_page import TopSelling
from pages.top_sellers_page import TopSellers
from pages.chosen_game_page import ChosenGame


class TestBase:

    main_page: MainPage
    about_page: AboutPage
    top_selling_page: TopSelling
    top_sellers_page: TopSellers
    chosen_game_page: ChosenGame

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.about_page = AboutPage(driver)
        request.cls.top_selling_page = TopSelling(driver)
        request.cls.top_sellers_page = TopSellers(driver)
        request.cls.chosen_game_page = ChosenGame(driver)
        self.main_page.open()
