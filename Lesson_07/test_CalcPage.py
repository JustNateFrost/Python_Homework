import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_sum(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.delay()
    calc_page.num()
    calc_page.wait_res()
    result = calc_page.wait_res()

    assert result == "15"
