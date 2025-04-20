import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        """
            Эта функция инициализирует браузер
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    @allure.step("Открыть сайт с калькулятором в браузере")
    def open(self):
        """
        Эта функция открывает сайт
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Очистить и ввести в окно задержки значение 45")
    def delay(self):
        """
        Эта функция очищает и вводит значение 45 в окно для задержки
        """
        self.driver.find_element(By.XPATH, '//*[@id="delay"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="delay"]').send_keys("45")

    @allure.step("Набрать в калькуляторе пример 7+8=")
    def num(self):
        """
        Эта функция набирает пример 7+8=
        """
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def wait_res(self) -> str:
        """
        Эта функция ожидает результат
        Возвращает текст полученного результата
        """
        self.wait.until(
            EC.text_to_be_present_in_element((
                By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))
        res = self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[1]/div').text
        return res
