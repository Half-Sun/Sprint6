from selenium.webdriver.firefox.options import Options
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


