from locators.about_important_locators import ImportantLocators
from pages.base_page import BasePage
import allure
from conftest import driver


class ImportantQuestionsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on question number: {num}")
    def click_on_question(self, num):
        locator = self.format_locators(ImportantLocators.QUESTION_LOCATOR, num)
        self.click_on_element(locator)

    @allure.step("Scroll to the important questions section")
    def scroll_to_important_questions(self):
        self.scroll_to_element(ImportantLocators.QUESTIONS_AREA)

    @allure.step("Get answer text for question {num}")
    def get_answer_text(self, num):
        question_locator = self.format_locators(ImportantLocators.QUESTION_LOCATOR, num)
        answer_locator = self.format_locators(ImportantLocators.ANSWER_LOCATOR, num)
        self.click_on_element(question_locator)
        return self.get_text_from_element(answer_locator)

    @allure.step("Get question locator")
    def get_question_locator(self, question_num):
        return self.format_locators(ImportantLocators.QUESTION_LOCATOR, question_num)
