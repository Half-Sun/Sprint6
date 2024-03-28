from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class OrderPage(BasePage):

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

    def check_first_page_order(self, locator):
        return self.get_text_from_element(locator)

    def set_second_page_order(self, date_locator_1, date_locator_2, rental_period_locator_1, rental_period_locator_2,
                              color_locator,
                              comment_locator, comment, locator):
        self.click_on_element(date_locator_1)
        self.click_on_element(date_locator_2)
        self.click_on_element(rental_period_locator_1)
        self.click_on_element(rental_period_locator_2)
        self.click_on_element(color_locator)
        self.input_data_to_element(comment_locator, comment)
        self.click_on_element(locator)


