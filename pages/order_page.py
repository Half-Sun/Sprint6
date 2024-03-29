from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.about_important_locators import ImportantLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
import allure

class OrderPage(BasePage):

    @allure.step("Set first page of order with details: name='{name}', lastname='{last_name}', ...")
    def set_first_page_order(self, name_locator, name, last_name_locator, last_name, address_locator, address,
                             station_locator_1, station_locator_2, mobile_locator, mobile,
                             next_button_locator):
        self.input_data_to_element(name_locator, name)
        self.input_data_to_element(last_name_locator, last_name)
        self.input_data_to_element(address_locator, address)
        self.click_on_element(station_locator_1)
        self.click_on_element(station_locator_2)
        self.input_data_to_element(mobile_locator, mobile)
        self.click_on_element(next_button_locator)

    @allure.step("Check text of element using locator: {locator}")
    def check_first_page_order(self, locator):
        return self.get_text_from_element(locator)

    @allure.title("Scroll to question using locator: {locator}")
    def scroll_to_bottom_order_button(self):
        self.scroll_to_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)


    @allure.step("Set second page of order with details: date='{date_locator_2}', rental_period='{rental_period_locator_2}', ...")
    def set_second_page_order(self, date_locator_1, date_locator_2, rental_period_locator_1, rental_period_locator_2,
                              color_locator, comment_locator, comment, order_button_locator):
        self.click_on_element(date_locator_1)
        self.click_on_element(date_locator_2)
        self.click_on_element(rental_period_locator_1)
        self.click_on_element(rental_period_locator_2)
        self.click_on_element(color_locator)
        self.input_data_to_element(comment_locator, comment)
        self.click_on_element(order_button_locator)

    @allure.title("Redirect to Yandex")
    def redirect_to_yandex_and_verify(self):
        EXPECTED_REDIRECT_URL = "https://sso.passport.yandex.ru"

        allure.step("Click on the Yandex logo")
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)

        allure.step("Switch to the new opened tab")
        self.driver.switch_to.window(self.driver.window_handles[1])

        allure.step("Wait until Yandex URL is loaded")
        WebDriverWait(self.driver, 40).until(EC.url_contains(EXPECTED_REDIRECT_URL))

        allure.step("Verify Yandex URL is displayed")
        assert EXPECTED_REDIRECT_URL in self.driver.current_url
