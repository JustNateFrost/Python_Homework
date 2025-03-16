from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

element = driver.find_element(By.CSS_SELECTOR, ".example > input:nth-child(2)")
element.send_keys("1000")
sleep(2)
element.clear()
sleep(2)
element.send_keys("999")
sleep(2)

driver.quit()