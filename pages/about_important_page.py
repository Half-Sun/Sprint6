from pages.base_page import BasePage


class ImportantQuestionsPage(BasePage):

    def scroll_to_question(self, locator):
        self.driver.get('https://qa-scooter.praktikum-services.ru')
        question_element = self.find_element_and_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)

    def click_on_question(self, locator):
        self.click_on_element(locator)

    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
