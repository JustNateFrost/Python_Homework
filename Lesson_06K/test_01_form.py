import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_color(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[1]/label/input').send_keys("Иван")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[2]/label/input').send_keys("Петров")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[1]/label/input').send_keys("Ленина, 55-3")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[1]/label/input').send_keys("test@skypro.com")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[2]/label/input').send_keys("+7985899998787")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[3]/label/input').send_keys("Москва")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[4]/label/input').send_keys("Россия")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[1]/label/input').send_keys("QA")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[2]/label/input').send_keys("SkyPro")
    browser.find_element(By.XPATH, '/html/body/main/div/form/div[5]/div/button').click()

    red_color = "rgba(132, 32, 41, 1)"
    green_color = "rgba(15, 81, 50, 1)"

    color_zip = browser.find_element(
        By.XPATH, '//*[@id="zip-code"]').value_of_css_property("color")
    color_first = browser.find_element(
        By.XPATH, '//*[@id="first-name"]').value_of_css_property("color")
    color_first = browser.find_element(
        By.XPATH, '//*[@id="last-name"]').value_of_css_property("color")
    color_address = browser.find_element(
        By.XPATH, '//*[@id="address"]').value_of_css_property("color")
    color_email = browser.find_element(
        By.XPATH, '//*[@id="e-mail"]').value_of_css_property("color")
    color_phone = browser.find_element(
        By.XPATH, '//*[@id="phone"]').value_of_css_property("color")
    color_city = browser.find_element(
        By.XPATH, '//*[@id="city"]').value_of_css_property("color")
    color_country = browser.find_element(
        By.XPATH, '//*[@id="country"]').value_of_css_property("color")
    color_job = browser.find_element(
        By.XPATH, '//*[@id="job-position"]').value_of_css_property("color")
    color_company = browser.find_element(
        By.XPATH, '//*[@id="company"]').value_of_css_property("color")

    assert color_zip == red_color
    assert color_first == green_color
    assert color_first == green_color
    assert color_address == green_color
    assert color_email == green_color
    assert color_phone == green_color
    assert color_city == green_color
    assert color_country == green_color
    assert color_job == green_color
    assert color_company == green_color
