import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PAGE), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_PAGE), "Register form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("jxecthnbabrfncjnkbxbtv")
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys("jxecthnbabrfncjnkbxbtv")
        register_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        register_submit.click()
        self.should_be_authorized_user()
