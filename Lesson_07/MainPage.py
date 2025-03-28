from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def add(self):
        for item in ["backpack", "bolt-t-shirt", "onesie"]:
            self.driver.find_element(By.ID, f"add-to-cart-sauce-labs-{item}").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
