from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):

    @allure.step("Click on the top 'Order' button")
    def click_top_order_button(self):
        self.click_on_element(OrderPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Click on the bottom 'Order' button")
    def click_bottom_order_button(self):
        self.click_on_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Set first page of order with details: name='{name}', lastname='{last_name}', ...")
    def set_first_page_order(self, name, last_name, address, mobile):
        self.input_data_to_element(OrderPageLocators.ORDER_INPUT_NAME, name)
        self.input_data_to_element(OrderPageLocators.ORDER_INPUT_LAST_NAME, last_name)
        self.input_data_to_element(OrderPageLocators.ORDER_INPUT_ADDRESS, address)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_STATION_ALL)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_STATION)
        self.input_data_to_element(OrderPageLocators.ORDER_INPUT_MOBILE, mobile)
        self.click_on_element(OrderPageLocators.ORDER_NEXT_BUTTON)

    @allure.step("Set second page of order with details")
    def set_second_page_order(self, comment):
        self.click_on_element(OrderPageLocators.ORDER_INPUT_WHEN_1)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_WHEN_2)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_RENTAL_PERIOD_1)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_RENTAL_PERIOD_2)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_COLOR)
        self.input_data_to_element(OrderPageLocators.ORDER_INPUT_COMMENT, comment)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_WANNA_ORDER)
        self.click_on_element(OrderPageLocators.ORDER_INPUT_WANNA_ORDER_YES_BUTTON)

    @allure.step("Redirect to Yandex")
    def redirect_to_yandex_and_verify(self):
        EXPECTED_REDIRECT_URL = "https://sso.passport.yandex.ru"
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)
        self.switch_window_and_wait()
        assert EXPECTED_REDIRECT_URL in self.driver.current_url


    @allure.step("Scroll to bottom order button")
    def scroll_to_bottom_order_button(self):
        self.scroll_to_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Click on bottom order button")
    def click_on_bottom_order_button(self):
        self.click_on_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Click on top order button")
    def click_on_top_order_button(self):
        self.click_on_element(OrderPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Click on scooter logo")
    def click_on_logo_scooter(self):
        self.click_on_element(OrderPageLocators.LOGO_SCOOTER)
