from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_question(self, locator):
        self.driver.get('https://qa-scooter.praktikum-services.ru')
        question_element = self.find_element_and_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    def input_data_to_element(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_and_wait(locator).get_attribute('innerHTML')

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)
