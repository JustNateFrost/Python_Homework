from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def check_backpack(self):
        backpack = self.driver.find_element(
            By.XPATH, '//*[@id="item_4_title_link"]/div').text
        return backpack
    
    def check_shirt(self):
        shirt = self.driver.find_element(
            By.XPATH, '//*[@id="item_1_title_link"]/div').text
        return shirt
    
    def check_onesie(self):
        onesie = self.driver.find_element(
            By.XPATH, '//*[@id="item_2_title_link"]/div').text
        return onesie

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
