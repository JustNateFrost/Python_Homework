import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_sum(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = browser.find_element(By.XPATH, '//*[@id="delay"]')
    delay.clear()
    delay.send_keys("45")

    browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    WebDriverWait(browser, 45).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))
    res = browser.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text
    assert res == "15"
