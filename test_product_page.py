import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    book_name = page.get_name(ProductPageLocators.BOOK_NAME)
    book_price = page.get_price(ProductPageLocators.BOOK_PRICE)

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    book_message_name = page.get_name(ProductPageLocators.BOOK_IN_BASKET_NAME)
    book_message_price = page.get_price(ProductPageLocators.BASKET_PRICE)

    page.should_be_book_in_message(book_name, book_message_name, book_price, book_message_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser, link)

    product_page.open()
    product_page.go_to_basket()

    basket_page = BasketPage(browser, link)

    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_text()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.email = str(time.time()) + "@fakemail.org"
        self.password = str(time.time())
        self.link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.user = LoginPage(browser, self.link)
        self.user.open()
        self.user.register_new_user(self.email, self.password)
        self.user.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = ProductPage(browser, self.link)
        self.page.open()

        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = ProductPage(browser, self.link)
        self.page.open()

        self.book_name = self.page.get_name(ProductPageLocators.BOOK_NAME)
        self.book_price = self.page.get_price(ProductPageLocators.BOOK_PRICE)

        self.page.add_product_to_basket()
        self.page.solve_quiz_and_get_code()

        self.book_message_name = self.page.get_name(ProductPageLocators.BOOK_IN_BASKET_NAME)
        self.book_message_price = self.page.get_price(ProductPageLocators.BASKET_PRICE)

        self.page.should_be_book_in_message(self.book_name, self.book_message_name, self.book_price, self.book_message_price)
