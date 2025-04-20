import allure
import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.epic("Работа с PageObject")
@allure.story("Калькулятор")
@allure.feature("ALLERT")
@allure.severity("critical")
@allure.title("Набор примера на калькуляторе и получение результата")
@allure.description("После ожидания в течение заданного времени (45 секунд) получение ответа и сравнение полученного результата с ожидаемым (15)")
def test_sum(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.delay()
    calc_page.num()
    with allure.step("Дождаться ответа через 45 секунд"):
        calc_page.wait_res()
    with allure.step("Получить фактический результат"):
        result = calc_page.wait_res()
    with allure.step("Сравнить фактический результат с ожидаемым"):
        assert result == "15"
