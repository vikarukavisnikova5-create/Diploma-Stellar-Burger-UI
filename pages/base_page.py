from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRAG_AND_DROP_JS = """
const source = arguments[0], target = arguments[1];
const dataTransfer = new DataTransfer();
const fire = (el, type) => el.dispatchEvent(
    new DragEvent(type, {dataTransfer, bubbles: true, cancelable: true}));
fire(source, 'dragstart');
fire(target, 'dragenter');
fire(target, 'dragover');
fire(target, 'drop');
fire(source, 'dragend');
"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        return self.find(locator).is_displayed()

    def is_hidden(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find(source_locator)
        target = self.find(target_locator)
        self.driver.execute_script(DRAG_AND_DROP_JS, source, target)