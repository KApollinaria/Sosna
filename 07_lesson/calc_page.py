from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
  def __init__(self, driver):
    self.driver = driver
    self.result_locator = (By.ID, "result")

  def calc_delay(self, value):
    delay_input = self.driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(value)

  def click_button(self, button_text):
    button = self.driver.find_element(By.CSS_SELECTOR, "button[text()='{button_text}']")
    button.click()

  def get_calc_results(self):
    WebDriverWait(self.driver, 50).until(
      EC.visibility_of_element_located(self.results_locator)
    )
    return result_element.txt
