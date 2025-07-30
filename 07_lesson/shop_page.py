from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
  def __init__(self, driver):
    self.driver = driver
    self.search_box = (By.NAME, 'q')
    self.results_selector = (By.CSS_SELECTOR, 'div.g')

  def shop_for(self, button_text):
    enter_username = self.driver.find_element(By.CSS_SELECTOR, "button[text()='{button_text}']")
    enter_password = self.driver.find_element(By.CSS_SELECTOR, "button[type='{button_text}']")

  def click_button(self, button_text):
    button = self.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()

  def input(self, first_name, last_name, postal_code):
    first_name_field = self.driver.find_element(By.ID, "first-name")
    last_name_field = self.driver.find_element(By.ID, "last-name")
    postal_code_field = self.driver.find_element(By.ID, "postal-code")

  def total_cost(self, summary_total_label):
    total_cost = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_cost_value = float(total_cost.split("$")[1])

  def get_shop_results(self):
    WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located(self.results_selector)
    )
