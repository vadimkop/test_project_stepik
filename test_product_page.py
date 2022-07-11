import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail(reason="I don't expect this bug to be fixed")), "8", "9"])
def test_guest_can_add_product_to_basket_product_name(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_product_name()

def test_guest_can_add_product_to_basket_price(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_price()

@pytest.mark.skip(reason="This isn't a bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_price()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="This isn't a bug")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_price()
    page.should_be_disappeared()

