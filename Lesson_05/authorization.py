from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")
sleep(2)
login = driver.find_element(By.CSS_SELECTOR, ".fa")
login.click()
sleep(2)

driver.quit()