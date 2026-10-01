import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.feed_page_locators import FeedPageLocators as L
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class FeedPage(BasePage):

    @allure.step('Проверить, что открыта лента заказов')
    def is_feed_opened(self):
        return self.is_visible(L.FEED_TITLE)

    def _get_counter(self, locator):
        return int(self.get_text(locator).replace(' ', ''))

    @allure.step('Получить счётчик «Выполнено за всё время»')
    def get_total_counter(self):
        return self._get_counter(L.TOTAL_COUNTER)

    @allure.step('Получить счётчик «Выполнено за сегодня»')
    def get_today_counter(self):
        return self._get_counter(L.TODAY_COUNTER)

    @allure.step('Дождаться увеличения счётчика')
    def wait_counter_increased(self, getter, old_value):
        WebDriverWait(self.driver, 30).until(lambda d: getter() > old_value)
        return getter()

    @allure.step('Проверить, что заказ появился в разделе «В работе»')
    def is_order_in_work(self, number):
        number = number.lstrip('0')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(L.order_in_work(number)))
        return True