from base.test_base import TestBase


class TestFindOnlineAction(TestBase):

    def test_find_online_action(self):

        self.main_page.is_opened()
        assert self.main_page.is_opened() == True, "Страница не соответствует ожидаемой"

        self.about_page.click_top_sellers()
        assert self.top_selling_page.is_opened(
        ) == True, "Страница не соответствует ожидаемой"

        self.top_selling_page.click_more_top_sellers()
        assert self.top_sellers_page.is_opened(
        ) == True, "Страница не соответствует ожидаемой"

        self.top_sellers_page.select_checkbox_os()
        assert self.top_sellers_page.is_checkbox_os_selected() == True, "Чекбокс не выбран"

        self.top_sellers_page.open_num_players_menu()
        self.top_sellers_page.select_checkbox_LAN_COOP()
        assert self.top_sellers_page.is_checkbox_LAN_COOP_selected() == True, "Чекбокс не выбран"

        self.top_sellers_page.select_checkbox_indie()
        self.top_sellers_page.select_checkbox_indie()
        self.top_sellers_page.select_checkbox_action()
        assert self.top_sellers_page.is_action_checkbox_selected() == True, "Чекбокс не выбран"
        assert self.top_sellers_page.games_search_result_list(
        ) == self.top_sellers_page.games_search_result_qty(), "Количество игр не соответствует"

        first_game_info = self.top_sellers_page.first_game_info()
        self.top_sellers_page.click_on_first_game()
        assert self.chosen_game_page.is_opened(
        ) == True, "Страница не соответствует ожидаемой"
        assert first_game_info == self.chosen_game_page.chosen_game_info(
        ), "Данные на страницах не соответствуют"
