from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)
element = driver.find_element(
    By.CSS_SELECTOR, ".modal-footer > p:nth-child(1)")
element.click()
sleep(2)
driver.quit()
