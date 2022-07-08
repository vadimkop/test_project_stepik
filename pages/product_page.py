from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_product_name(self):
        submit_basket = self.browser.find_element(*ProductPageLocators.SUBMIT_BASKET)
        submit_basket.click()
        self.solve_quiz_and_get_code()
        assert "The shellcoder's handbook" == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Wrong product name"

    def should_be_add_to_basket_price(self):
        submit_basket = self.browser.find_element(*ProductPageLocators.SUBMIT_BASKET)
        submit_basket.click()
        self.solve_quiz_and_get_code()
        assert "9,99" in self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text, "Wrong product price"