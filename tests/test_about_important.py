import pytest
from conftest import driver
from pages.about_important_page import ImportantQuestionsPage
from data import questions_data
import allure


class TestImportantQuestions:

    @allure.title("Parameterized test - Check the answers of important questions")
    @pytest.mark.parametrize(
        'question_data',
        questions_data
    )
    def test_check_answer_on_question(self, driver, question_data):
        important_questions_page = ImportantQuestionsPage(driver)
        important_questions_page.go_to_site()
        important_questions_page.scroll_to_important_questions()
        actual_answer = important_questions_page.get_answer_text(question_data["num"])
        assert actual_answer == question_data["expected_answer"], "Answer mismatch"
