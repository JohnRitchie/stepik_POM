from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_MAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, './/button[@name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.XPATH, './/div[@class="col-sm-6 product_main"]/h1')
    BOOK_PRICE = (By.XPATH, './/div[@class="col-sm-6 product_main"]/p')
    BOOK_IN_BASKET_NAME = (By.XPATH, './/div[@class="alertinner "]/strong')
    BASKET_PRICE = (By.XPATH, './/div[@class="alertinner "]/p/strong')
    SUCCESS_MESSAGE = (By.XPATH, './/div[@class="alertinner "]')


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.XPATH, ".//p[contains(text(),'пуста')]")
    BASKET_ITEMS = (By.XPATH, ".//h2[contains(text(),'Товары в корзине')]")
