from selenium.webdriver.common.by import By

'''
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
'''


class LoginPageLocators:
    LOGIN_PAGE = (By.ID, "login_form")
    REGISTER_PAGE = (By.ID, "register_form")


class ProductPageLocators:
    SUBMIT_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ALERT_INNER = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BASKET_PRICE = (
    By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner ")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    BASKET_SHOW = [By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a"]
    BASKET_FULL = (By.ID, "basket_formset")
    BASKET_EMPTY_MESSAGES = (By.ID, "content_inner")
