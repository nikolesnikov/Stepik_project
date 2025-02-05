import time
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_confirm_message_with_name_of_product()
    page.should_be_message_with_cost_of_busket_after_add()
    