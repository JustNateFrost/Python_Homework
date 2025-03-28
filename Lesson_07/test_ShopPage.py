import pytest
from selenium import webdriver
from AutoPage import AutoPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shop(driver):
    auto_page = AutoPage(driver)
    auto_page.open()
    auto_page.enter()

    main_page = MainPage(driver)
    main_page.open()
    main_page.add()

    cart_page = CartPage(driver)
    cart_page.open()
    cart_page.check_backpack()
    name_backpack = cart_page.check_backpack()
    cart_page.check_shirt()
    name_shirt = cart_page.check_shirt()
    cart_page.check_onesie()
    name_onesie = cart_page.check_onesie()
    cart_page.checkout()

    order_page = OrderPage(driver)
    order_page.open()
    order_page.data()
    order_page.total()
    total_sum = order_page.total()

    assert name_backpack == "Sauce Labs Backpack"
    assert name_shirt == "Sauce Labs Bolt T-Shirt"
    assert name_onesie == "Sauce Labs Onesie"
    assert total_sum == "Total: $58.29"
