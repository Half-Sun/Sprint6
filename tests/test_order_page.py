import pytest
from conftest import driver
from data import order_data, order_data_2
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
import allure


class TestOrderFirstPage:

    @allure.title("Parameterized test - Order form filled via top button")
    @pytest.mark.parametrize(
        "name, last_name, address, mobile",
        order_data
    )
    def test_first_order_page_via_top_button_is_filled(self, driver, name, last_name, address, mobile):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_top_order_button()
        order_page.set_first_page_order(name, last_name, address, mobile)
        assert order_page.get_text_from_element(OrderPageLocators.ORDER_BACK_BUTTON) == "Назад"

    @allure.title("Test - Order form filled via bottom button")
    def test_first_order_page_via_bottom_button(self, driver):
        order_first_page = OrderPage(driver)
        order_first_page.go_to_site()
        order_first_page.scroll_to_bottom_order_button()
        order_first_page.click_on_bottom_order_button()
        assert order_first_page.get_text_from_element(OrderPageLocators.ORDER_BACK_BUTTON) == "Далее"

    @allure.title("Parameterized test - Order form second page filled ")
    @pytest.mark.parametrize(
        "name, last_name, address, mobile, comment",
        order_data_2
    )
    def test_second_order_page_via_top_button_is_filled(self, driver, name, last_name, address, mobile,
                                                        comment):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_on_top_order_button()
        order_page.set_first_page_order(name, last_name, address, mobile)
        order_page.set_second_page_order(comment)
        assert "Номер заказа:" in order_page.get_text_from_element(OrderPageLocators.ORDER_SUCCESSFULLY_PLACED)

    @pytest.mark.parametrize(
        "name, last_name, address, mobile",
        order_data
    )
    @allure.title("Redirect to main page via scooter logo")
    def test_redirect_to_main_page_via_scooter(self, driver, name, last_name, address, mobile):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_on_top_order_button()
        order_page.set_first_page_order(name, last_name, address, mobile)
        order_page.click_on_logo_scooter()
        assert "Самокат" in order_page.get_text_from_element(OrderPageLocators.SCOOTER_MAIN_PAGE_TEXT)

    @allure.title("Redirect to Yandex via Yandex logo")
    def test_redirect_to_dzen_via_yandex(self,driver):
        order_first_page = OrderPage(driver)
        order_first_page.go_to_site()
        order_first_page.redirect_to_yandex_and_verify()


