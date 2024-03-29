from locators.about_important_locators import ImportantLocators
from pages.base_page import BasePage
import allure

class ImportantQuestionsPage(BasePage):

    @allure.title("Click on question using locator: {locator}")
    def click_on_question(self, locator):
        self.click_on_element(locator)

    @allure.title("Scroll to question using locator: {locator}")
    def scroll_to_important_questions(self):
        self.scroll_to_element(ImportantLocators.QUESTIONS_AREA)

    @allure.step("Get answer text for question {num}")
    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
