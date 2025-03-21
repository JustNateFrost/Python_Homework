from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[1]/div[1]/label/input')
first.send_keys("Иван")
second = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[1]/div[2]/label/input')
second.send_keys("Петров")
address = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[2]/div[1]/label/input')
address.send_keys("Ленина, 55-3")
email = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[3]/div[1]/label/input')
email.send_keys("test@skypro.com")
phone = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[3]/div[2]/label/input')
phone.send_keys("+7985899998787")
city = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[2]/div[3]/label/input')
city.send_keys("Москва")
country = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[2]/div[4]/label/input')
country.send_keys("Россия")
job = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[4]/div[1]/label/input')
job.send_keys("QA")
company = driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[4]/div[2]/label/input')
company.send_keys("SkyPro")

driver.find_element(
    By.XPATH, '/html/body/main/div/form/div[5]/div/button').click()


def test_zip():
    red_color = "rgba(132, 32, 41, 1)"
    color_zip = driver.find_element(
        By.XPATH, '//*[@id="zip-code"]').value_of_css_property("color")
    assert color_zip == red_color


def test_first():
    green_color = "rgba(15, 81, 50, 1)"
    color_first = driver.find_element(
        By.XPATH, '//*[@id="first-name"]').value_of_css_property("color")
    assert color_first == green_color


def test_second():
    green_color = "rgba(15, 81, 50, 1)"
    color_first = driver.find_element(
        By.XPATH, '//*[@id="last-name"]').value_of_css_property("color")
    assert color_first == green_color


def test_address():
    green_color = "rgba(15, 81, 50, 1)"
    color_address = driver.find_element(
        By.XPATH, '//*[@id="address"]').value_of_css_property("color")
    assert color_address == green_color


def test_email():
    green_color = "rgba(15, 81, 50, 1)"
    color_email = driver.find_element(
        By.XPATH, '//*[@id="e-mail"]').value_of_css_property("color")
    assert color_email == green_color


def test_phone():
    green_color = "rgba(15, 81, 50, 1)"
    color_phone = driver.find_element(
        By.XPATH, '//*[@id="phone"]').value_of_css_property("color")
    assert color_phone == green_color


def test_city():
    green_color = "rgba(15, 81, 50, 1)"
    color_city = driver.find_element(
        By.XPATH, '//*[@id="city"]').value_of_css_property("color")
    assert color_city == green_color


def test_country():
    green_color = "rgba(15, 81, 50, 1)"
    color_country = driver.find_element(
        By.XPATH, '//*[@id="country"]').value_of_css_property("color")
    assert color_country == green_color


def test_job():
    green_color = "rgba(15, 81, 50, 1)"
    color_job = driver.find_element(
        By.XPATH, '//*[@id="job-position"]').value_of_css_property("color")
    assert color_job == green_color


def test_company():
    green_color = "rgba(15, 81, 50, 1)"
    color_company = driver.find_element(
        By.XPATH, '//*[@id="company"]').value_of_css_property("color")
    assert color_company == green_color
