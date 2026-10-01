from selenium.webdriver.common.by import By

class FeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")

    @staticmethod
    def order_in_work(number):
        return (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList') "
                          "and not(contains(@class, 'orderListReady'))]"
                          f"/li[contains(., '{number}')]")