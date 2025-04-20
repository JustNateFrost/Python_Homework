import allure
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


@allure.epic("Работа с PageObject")
@allure.story("Магазин")
@allure.feature("ALLERT")
@allure.severity("critical")
@allure.title("Наличие и соответствие товаров и итоговой стоимоси при оформлении заказа")
@allure.description("После авторизации на сайте магазина добавление товаров в корзину на главной странице, проверка наличия выбранных товаров и итоговой стоимости на странице с оформлением заказа")
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
    with allure.step("Получить название первого товара"):
        name_backpack = cart_page.check_backpack()
    cart_page.check_shirt()
    with allure.step("Получить название второго товара"):
        name_shirt = cart_page.check_shirt()
    cart_page.check_onesie()
    with allure.step("Получить название третьего товара"):
        name_onesie = cart_page.check_onesie()
    cart_page.checkout()

    order_page = OrderPage(driver)
    order_page.open()
    order_page.data()
    order_page.total()
    with allure.step("Получить итоговую стоимость покупки"):
        total_sum = order_page.total()

    with allure.step("Сравнить полученное название первого товара с выбранным"):
        assert name_backpack == "Sauce Labs Backpack"
    with allure.step("Сравнить полученное название второго товара с выбранным"):
        assert name_shirt == "Sauce Labs Bolt T-Shirt"
    with allure.step("Сравнить полученное название третьего товара с выбранным"):
        assert name_onesie == "Sauce Labs Onesie"
    with allure.step("Сравнить полученную итоговую стоимость с ожидаемой"):
        assert total_sum == "Total: $58.29"
