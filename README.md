README.md
Project Name: Scooter Ordering System Tests

Description

This project contains automated tests for the scooter ordering system. The tests are written using Selenium WebDriver and Pytest and cover the following aspects:

Order form testing:
Tests checking the correct filling of the form from different "Order" buttons.
Tests checking the filling of the form with a comment.
Redirect testing:
Test checking the redirect to the main "Scooter" page when clicking on the logo.
Test checking the redirect to "Yandex SSO" when clicking on the "Yandex" logo.
"Important Questions" section testing:
Checking the display of answers to frequently asked questions.

Requirements:
Python 3.x
Selenium WebDriver
Pytest
allure-pytest (for generating Allure reports)
Browser driver (Chrome, Firefox, etc.)

Project Structure:
tests/: Contains test scripts.
pages/: Contains page-object classes for interacting with the web application.
locators/: Contains locators for page elements.
data/: Contains test data.
conftest.py: Contains general test configuration (web driver setup).
