from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

for x in range(1, 5):
    driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

delete = driver.find_elements(By.CLASS_NAME, "added-manually")
print(len(delete))
