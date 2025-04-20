import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        """
        Эта функция инициализирует браузер
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Перейти на сайт с оформлением заказа")
    def open(self) -> None:
        """
        Эта функция открывает сайт
        """
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    @allure.step("Вести персональные данные")
    def data(self) -> None:
        """
        Эта функция вводит в поля имя, фамилию и индекс, нажимает на кнопку Continue
        """
        self.driver.find_element(By.ID, "first-name").send_keys("Анна")
        self.driver.find_element(By.ID, "last-name").send_keys("Зайцева")
        self.driver.find_element(By.ID, "postal-code").send_keys("246801")
        self.driver.find_element(By.ID, "continue").click()

    def total(self) -> str:
        """
        Эта функция ожидает итоговую стоимость покупки
        Возвращает текст полученной стоимости
        """
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        return total
