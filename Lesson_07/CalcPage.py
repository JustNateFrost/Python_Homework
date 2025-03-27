from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self):
        self.driver.find_element(By.XPATH, '//*[@id="delay"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="delay"]').send_keys("45")

    def num(self):
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def wait_res(self):
        self.wait.until(
            EC.text_to_be_present_in_element((
                By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))
        res = self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[1]/div').text
        return res
