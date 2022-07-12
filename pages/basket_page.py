from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket url is not presented"

    def should_be_empty_message_in_basket(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGES).text, "The basket isn't empty, but should be "

    def should_be_basket_without_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FULL), "The basket isn't empty, but should be"

    def should_be_basket_is_empty(self):
        self.should_be_basket_url()
        self.should_be_empty_message_in_basket()
        self.should_be_basket_without_products()

