from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    COST_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    COST_OF_BASKET_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    NAME_OF_PRODUCT_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM_BLOCK = (By.ID, "basket_formset")