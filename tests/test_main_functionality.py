import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage

@allure.feature('Основная функциональность')
class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor_opens_constructor(self, driver):
        page = MainPage(driver)
        page.click_feed()
        page.click_constructor()
        assert page.is_constructor_opened()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_feed_opens_feed(self, driver):
        MainPage(driver).click_feed()
        assert FeedPage(driver).is_feed_opened()

    @allure.title('Клик на ингредиент открывает окно с деталями')
    def test_click_ingredient_opens_details(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        assert page.is_ingredient_details_opened()

    @allure.title('Окно с деталями закрывается кликом по крестику')
    def test_close_ingredient_details(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        page.close_modal()
        assert page.is_modal_closed()

    @allure.title('Счётчик ингредиента увеличивается при добавлении в заказ')
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        before = page.get_bun_counter()
        page.add_bun_to_order()
        assert page.get_bun_counter() > before
