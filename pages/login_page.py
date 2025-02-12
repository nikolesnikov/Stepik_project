from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from random import randrange

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.__contains__('login'), "URL doesn't contain login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = 'alex' + str(randrange(100)) + '@goondex.ru'
        password = str(randrange(10000, 99999)) + 'Zxcv'
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_password.send_keys(password)
        reg_password_confirm = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_CONFIRM)
        reg_password_confirm.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()