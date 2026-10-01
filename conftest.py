import pytest
from selenium import webdriver
from data import BASE_URL
from helpers import generate_user, register_user, delete_user
from pages.login_page import LoginPage

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.set_window_size(1920, 1080)
    browser.get(BASE_URL)
    yield browser
    browser.quit()

@pytest.fixture
def user():
    user = generate_user()
    response = register_user(user)
    yield user
    delete_user(response.json()['accessToken'])

@pytest.fixture
def logged_in_driver(driver, user):
    LoginPage(driver).login(user['email'], user['password'])
    return driver