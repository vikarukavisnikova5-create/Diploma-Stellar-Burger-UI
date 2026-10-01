import allure
from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Кликнуть на «Конструктор»')
    def click_constructor(self):
        self.click(L.CONSTRUCTOR_LINK)

    @allure.step('Кликнуть на «Лента заказов»')
    def click_feed(self):
        self.click(L.FEED_LINK)

    @allure.step('Проверить, что открыт конструктор')
    def is_constructor_opened(self):
        return self.is_visible(L.CONSTRUCTOR_TITLE)

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.click(L.BUN)

    @allure.step('Проверить, что открыто окно с деталями ингредиента')
    def is_ingredient_details_opened(self):
        return self.is_visible(L.INGREDIENT_DETAILS_TITLE)

    @allure.step('Закрыть всплывающее окно крестиком')
    def close_modal(self):
        self.click(L.MODAL_CLOSE_BUTTON)

    @allure.step('Проверить, что всплывающее окно закрыто')
    def is_modal_closed(self):
        return self.is_hidden(L.MODAL_OPENED)

    @allure.step('Получить значение счётчика ингредиента')
    def get_bun_counter(self):
        elements = self.driver.find_elements(*L.BUN_COUNTER)
        return int(elements[0].text) if elements else 0

    @allure.step('Добавить ингредиент в заказ')
    def add_bun_to_order(self):
        self.drag_and_drop(L.BUN, L.CONSTRUCTOR_BASKET)

    @allure.step('Оформить заказ и получить его номер')
    def create_order(self):
        self.add_bun_to_order()
        self.click(L.ORDER_BUTTON)
        self.wait.until(lambda d: self.get_text(L.ORDER_NUMBER) not in ('', '9999'))
        number = self.get_text(L.ORDER_NUMBER)
        self.close_modal()
        self.is_modal_closed()
        return number
