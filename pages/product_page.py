from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        submit_basket = self.browser.find_element(*ProductPageLocators.SUBMIT_BASKET)
        submit_basket.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(*ProductPageLocators.ALERT_INNER).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Wrong product name"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text, "Wrong product price"
        capture_path = 'C:/capture/your_desired_filename.png'
        self.browser.save_screenshot(capture_path)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message isn't dissappeared, but should be"