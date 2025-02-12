from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
    
    def should_be_confirm_message_with_name_of_product(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        name_of_product_from_message = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_FROM_MESSAGE)
        assert name_of_product.text == name_of_product_from_message.text, "Name of product from message != name of product from the card"

    def should_be_message_with_cost_of_busket_after_add(self):
        cost_of_product = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT)
        cost_of_basket_from_message = self.browser.find_element(*ProductPageLocators.COST_OF_BASKET_FROM_MESSAGE)
        assert cost_of_product.text == cost_of_basket_from_message.text, "Cost of basket != cost of product that was add"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but not should be"

    def element_should_disappered(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappered, but should be"
    