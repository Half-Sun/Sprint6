from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru"
        self.driver.maximize_window()

    def go_to_site(self):
        self.driver.get(self.base_url)
    @allure.step("Scroll to element using locator: {locator}")
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Wait for element visibility using locator: {locator}")
    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Click element using locator: {locator}")
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step("Input text '{text}' into field using locator: {locator}")
    def input_data_to_element(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    @allure.step("Get text from element using locator: {locator}")
    def get_text_from_element(self, locator):
        return self.find_element_and_wait(locator).get_attribute('innerHTML')

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)
