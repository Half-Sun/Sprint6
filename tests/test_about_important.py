import pytest
from conftest import driver
from locators.about_important_locators import ImportantLocators
from pages.about_important_page import ImportantQuestionsPage
from data import questions_data
import allure


class TestImportantQuestions:

    @allure.title("Parameterized test - Check the answers of important questions")  # Added allure.title
    @pytest.mark.parametrize(
        'question_data',
        questions_data
    )
    def test_check_answer_on_question(self, driver, question_data):
        important_questions_page = ImportantQuestionsPage(driver)
        important_questions_page.go_to_site()
        allure.step("Scroll to the important questions section")
        important_questions_page.scroll_to_important_questions()

        allure.step("Get the text of the answer")
        actual_answer = important_questions_page.get_answer_text(
            ImportantLocators.QUESTION_LOCATOR,
            ImportantLocators.ANSWER_LOCATOR,
            question_data["num"]
        )

        allure.step("Verify the answer text matches the expected data")
        assert actual_answer == question_data["expected_answer"]
