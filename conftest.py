import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    service = Service(executable_path='C:/chromedriver/chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
