import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language")

@pytest.fixture(scope="function")
def browser():
    options = Options()
    #options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    #options.add_argument("--auto-open-devtools-for-tabs")
    #options.add_argument("--incognito")
    #options.add_argument('--proxy-server=%s' % 'http://ppod-proxy.ftc.ru:3128')
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    #service = Service(executable_path='./tools/chromedriver.exe')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit() 