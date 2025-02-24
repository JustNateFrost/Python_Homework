from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.ID, 'newButtonName')
element.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

content = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
txt = content.find_element(By.XPATH, '//*[@id="updatingButton"]').text
print(txt)
