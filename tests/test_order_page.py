import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import order_data, order_data_2
from conftest import driver
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
import allure


class TestOrderFirstPage:

    @allure.step("Parameterized test - Order form filled via top button")
    @pytest.mark.parametrize(
        "name, last_name, address, mobile",
        order_data
    )
    def test_first_order_page_via_top_button_is_filled(self, driver, name, last_name, address, mobile):
        order_first_page = OrderPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru')

        # Detailed steps for clarity
        allure.step("Click on the top 'Order' button")
        order_first_page.click_on_element(OrderPageLocators.TOP_ORDER_BUTTON)

        allure.step("Fill in the order form")
        order_first_page.set_first_page_order(OrderPageLocators.ORDER_INPUT_NAME, name,
                                               OrderPageLocators.ORDER_INPUT_LAST_NAME, last_name,
                                               OrderPageLocators.ORDER_INPUT_ADDRESS, address,
                                               OrderPageLocators.ORDER_INPUT_STATION_ALL,
                                               OrderPageLocators.ORDER_INPUT_STATION,
                                               OrderPageLocators.ORDER_INPUT_MOBILE, mobile,
                                               OrderPageLocators.ORDER_NEXT_BUTTON)

        allure.step("Verify 'Back' button is displayed")
        assert order_first_page.get_text_from_element(OrderPageLocators.ORDER_BACK_BUTTON) == "Назад"

    @allure.step("Test - Order form filled via bottom button")
    def test_first_order_page_via_bottom_button(self, driver):
        order_first_page = OrderPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru')
        allure.step("Scroll down to the bottom 'Order' button")
        order_first_page.scroll_to_question(OrderPageLocators.BOTTOM_ORDER_BUTTON)
        allure.step("Click on the bottom 'Order' button")
        order_first_page.click_on_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)
        allure.step("Verify 'Далее' (Next) button is displayed")
        assert order_first_page.get_text_from_element(OrderPageLocators.ORDER_BACK_BUTTON) == "Далее"

    @allure.step("Parameterized test - Order form filled via top button and comment added")
    @pytest.mark.parametrize(
        "name, last_name, address, mobile",
        order_data
    )
    @pytest.mark.parametrize(
        "comment",
        order_data_2
    )
    def test_second_order_page_via_top_button_is_filled(self, driver, name, last_name, address, mobile,
                                                        comment):  # Notice driver argument
        order_second_page = OrderPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru')
        order_second_page.click_on_element(OrderPageLocators.TOP_ORDER_BUTTON)
        allure.step("Fill in the first page of the order form")
        order_second_page.set_first_page_order(OrderPageLocators.ORDER_INPUT_NAME, name,
                                               OrderPageLocators.ORDER_INPUT_LAST_NAME, last_name,
                                               OrderPageLocators.ORDER_INPUT_ADDRESS, address,
                                               OrderPageLocators.ORDER_INPUT_STATION_ALL,
                                               OrderPageLocators.ORDER_INPUT_STATION,
                                               OrderPageLocators.ORDER_INPUT_MOBILE, mobile,
                                               OrderPageLocators.ORDER_NEXT_BUTTON)
        allure.step("Fill in the second page of the order form")
        order_second_page.set_second_page_order(OrderPageLocators.ORDER_INPUT_WHEN_1,
                                                OrderPageLocators.ORDER_INPUT_WHEN_2,
                                                OrderPageLocators.ORDER_INPUT_RENTAL_PERIOD_1,
                                                OrderPageLocators.ORDER_INPUT_RENTAL_PERIOD_2,
                                                OrderPageLocators.ORDER_INPUT_COLOR,
                                                OrderPageLocators.ORDER_INPUT_COMMENT, comment,
                                                OrderPageLocators.ORDER_INPUT_WANNA_ORDER)
        order_second_page.click_on_element(OrderPageLocators.ORDER_INPUT_WANNA_ORDER_YES_BUTTON)
        allure.step("Verify 'Номер заказа' is displayed")
        assert "Номер заказа:" in order_second_page.get_text_from_element(OrderPageLocators.ORDER_SUCCESSFULLY_PLACED)


    @pytest.mark.parametrize(
        "name, last_name, address, mobile",
        order_data
    )

    @allure.step("Test - Redirect to main page via scooter logo")
    def test_redirect_to_main_page_via_scooter(self, driver, name, last_name, address, mobile):
        order_first_page = OrderPage(driver)
        driver.get('https://qa-scooter.praktikum-services.ru')

        allure.step("Click on the top 'Order' button")
        order_first_page.click_on_element(OrderPageLocators.TOP_ORDER_BUTTON)

        allure.step("Fill in the first page of the order form")
        order_first_page.set_first_page_order(OrderPageLocators.ORDER_INPUT_NAME, name,
                                               OrderPageLocators.ORDER_INPUT_LAST_NAME, last_name,
                                               OrderPageLocators.ORDER_INPUT_ADDRESS, address,
                                               OrderPageLocators.ORDER_INPUT_STATION_ALL,
                                               OrderPageLocators.ORDER_INPUT_STATION,
                                               OrderPageLocators.ORDER_INPUT_MOBILE, mobile,
                                               OrderPageLocators.ORDER_NEXT_BUTTON)

        allure.step("Click on the 'Самокат' logo")
        order_first_page.click_on_element(OrderPageLocators.LOGO_SCOOTER)

        allure.step("Verify 'Самокат' text is displayed")
        assert "Самокат" in order_first_page.get_text_from_element(OrderPageLocators.SCOOTER_MAIN_PAGE_TEXT)

    @allure.step("Test - Redirect to Yandex via Yandex logo")
    def test_redirect_to_dzen_via_yandex(self, driver):
        order_first_page = OrderPage(driver)
        EXPECTED_REDIRECT_URL = "https://sso.passport.yandex.ru"
        driver.get('https://qa-scooter.praktikum-services.ru')

        allure.step("Click on the Yandex logo")
        order_first_page.click_on_element(OrderPageLocators.YANDEX_LOGO)

        allure.step("Switch to the new opened tab")
        driver.switch_to.window(driver.window_handles[1])

        allure.step("Wait until Yandex URL is loaded")
        WebDriverWait(driver, 40).until(EC.url_contains("https://sso.passport.yandex.ru"))

        allure.step("Verify Yandex URL is displayed")
        assert EXPECTED_REDIRECT_URL in driver.current_url


