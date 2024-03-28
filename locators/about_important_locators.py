from selenium.webdriver.common.by import By


class ImportantLocators:
    QUESTIONS_AREA = By.CLASS_NAME, "accordion"
    QUESTION_LOCATOR = By.CSS_SELECTOR, "#accordion__heading-{}"
    ANSWER_LOCATOR = By.CSS_SELECTOR, "#accordion__panel-{}"
