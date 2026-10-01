from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    FEED_LINK = (By.XPATH, "//p[contains(text(), 'Лента')]")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    BUN_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"
                             "/parent::a//p[contains(@class, 'counter_counter__num')]")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"
                                    "//button[contains(@class, 'Modal_modal__close')]")
    CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")



