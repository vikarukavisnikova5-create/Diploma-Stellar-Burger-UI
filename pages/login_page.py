import allure
from data import LOGIN_URL
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step('Авторизоваться')
    def login(self, email, password):
        self.open(LOGIN_URL)
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.find(MainPageLocators.ORDER_BUTTON)