from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 5)

driver.get("https://www.saucedemo.com")

username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
username.send_keys("standard_user")
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce")

driver.find_element(By.XPATH, '//*[@id="login-button"]').click()


driver.find_element(
    By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(
    By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
driver.find_element(
    By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

first = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first.send_keys("Алиса")
last = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last.send_keys("Сонная")
zip = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
zip.send_keys("628400")
driver.find_element(By.XPATH, '//*[@id="continue"]').click()

waiter.until(EC.text_to_be_present_in_element((
   By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]'),
   "Total: $58.29"))


def test_total():
    sum = "Total: $58.29"
    element = driver.find_element(
        By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
    total = element.text
    assert sum == total
