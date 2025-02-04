import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    service = Service(executable_path='C:/chromedriver/chromedriver.exe')
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
