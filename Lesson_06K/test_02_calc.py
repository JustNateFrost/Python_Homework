from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 45)

driver.get(
   "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay = driver.find_element(
    By.XPATH, '//*[@id="delay"]')
delay.clear()
delay.send_keys("45")

driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

waiter.until(EC.text_to_be_present_in_element((
   By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))


def test_res():
    sum = "15"
    element = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div')
    res = element.text
    assert sum == res
