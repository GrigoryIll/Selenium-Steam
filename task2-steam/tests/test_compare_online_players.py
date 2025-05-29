from base.test_base import TestBase


class TestPlayersOnline(TestBase):

    def test_compare_online_players(self):

        assert self.main_page.is_opened() == True, "Страница не соответствует ожидаемой"

        self.main_page.click_about_button()
        self.about_page.is_opened()
        assert self.about_page.is_opened() == True, "Страница не соответствует ожидаемой"

        online_players = self.about_page.get_online_players()
        players_now = self.about_page.get_players_now()
        assert online_players > players_now, "Игроков онлайн меньше чем играющих"

        self.about_page.click_store_button()
        assert self.main_page.is_opened() == True, "Страница не соответствует ожидаемой"
