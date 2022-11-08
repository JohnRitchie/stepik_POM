from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.click_to_element(ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def get_name(self, element):
        return self.browser.find_elements(*element)[0].text

    def get_price(self, element):
        return self.browser.find_elements(*element)[0].text.strip(' £')

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_book_in_message(self, book_name, book_message_name, book_price, book_message_price):
        assert book_name == book_message_name and book_price == book_message_price
