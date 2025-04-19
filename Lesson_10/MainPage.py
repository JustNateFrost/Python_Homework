import allure
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Перейти на главную страницу со списком товаров")
    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    @allure.step("Выбрать товары и добавить их в корзину")
    def add(self):
        for item in ["backpack", "bolt-t-shirt", "onesie"]:
            self.driver.find_element(By.ID, f"add-to-cart-sauce-labs-{item}").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
