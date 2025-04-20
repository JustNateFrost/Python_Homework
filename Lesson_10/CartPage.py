import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """
        Эта функция инициализирует браузер
        """
        self.driver = driver

    @allure.step("Перейти на страницу с добавленными товарами")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get("https://www.saucedemo.com/cart.html")

    def check_backpack(self) -> str:
        """
        Эта функция находит название первого товара
        Возвращает текст полученного результата
        """
        backpack = self.driver.find_element(
            By.XPATH, '//*[@id="item_4_title_link"]/div').text
        return backpack

    def check_shirt(self) -> str:
        """
        Эта функция находит название второго товара
        Возвращает текст полученного результата
        """
        shirt = self.driver.find_element(
            By.XPATH, '//*[@id="item_1_title_link"]/div').text
        return shirt

    def check_onesie(self) -> str:
        """
        Эта функция находит название третьего товара
        Возвращает текст полученного результата
        """
        onesie = self.driver.find_element(
            By.XPATH, '//*[@id="item_2_title_link"]/div').text
        return onesie

    def checkout(self) -> None:
        """
        Эта функция нажимает на кнопку Checkout
        """
        self.driver.find_element(By.ID, "checkout").click()
