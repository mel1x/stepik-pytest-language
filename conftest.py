import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose user interface language, for example: es, fr, ru")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
