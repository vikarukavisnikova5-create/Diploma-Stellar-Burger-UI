import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage

@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Счётчик «Выполнено за всё время» увеличивается после заказа')
    def test_total_counter_increases(self, logged_in_driver):
        main, feed = MainPage(logged_in_driver), FeedPage(logged_in_driver)
        main.click_feed()
        before = feed.get_total_counter()
        main.click_constructor()
        main.create_order()
        main.click_feed()
        assert feed.wait_counter_increased(feed.get_total_counter, before) > before

    @allure.title('Счётчик «Выполнено за сегодня» увеличивается после заказа')
    def test_today_counter_increases(self, logged_in_driver):
        main, feed = MainPage(logged_in_driver), FeedPage(logged_in_driver)
        main.click_feed()
        before = feed.get_today_counter()
        main.click_constructor()
        main.create_order()
        main.click_feed()
        assert feed.wait_counter_increased(feed.get_today_counter, before) > before

    @allure.title('Номер нового заказа появляется в разделе «В работе»')
    def test_new_order_appears_in_work(self, logged_in_driver):
        main, feed = MainPage(logged_in_driver), FeedPage(logged_in_driver)
        number = main.create_order()
        main.click_feed()
        assert feed.is_order_in_work(number)