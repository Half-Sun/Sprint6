import pytest
from conftest import driver
from locators.about_important_locators import ImportantLocators
from pages.about_important_page import ImportantQuestionsPage
from data import questions_data
import allure


class TestImportantQuestions:

    @allure.step("Parameterized test - Check the answers of important questions")
    @pytest.mark.parametrize(
        'question_data',
        questions_data
    )
    def test_check_answer_on_question(self, driver, question_data):
        important_questions_page = ImportantQuestionsPage(driver)

        allure.step("Scroll to the important questions section")
        important_questions_page.scroll_to_question(ImportantLocators.QUESTIONS_AREA)

        allure.step("Get the text of the answer")
        actual_answer = important_questions_page.get_answer_text(
            ImportantLocators.QUESTION_LOCATOR,
            ImportantLocators.ANSWER_LOCATOR,
            question_data["num"]
        )

        allure.step("Verify the answer text matches the expected data")
        assert actual_answer == question_data["expected_answer"]
