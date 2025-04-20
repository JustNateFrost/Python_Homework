import allure
from selenium.webdriver.common.by import By


class AutoPage:
    def __init__(self, driver):
        """
        Эта функция инициализирует браузер
        """
        self.driver = driver

    @allure.step("Открыть сайт с магазином в браузере")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизоваться в системе")
    def enter(self) -> None:
        """
        Эта функция вводит в поля логин и пароль, нажимает на кнопку Login
        """
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
