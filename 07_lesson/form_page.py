from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
  def __init__(self, driver):
    self.driver = driver

  def form_for(self, button_text):
    first_name = self.driver.find_element(By.NAME, "first-name").send_keys(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_last_name = self.driver.find_element(By.NAME, "last-name").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_address = self.driver.find_element(By.NAME, "address").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_e_mail = self.driver.find_element(By.NAME, "e-mail").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_phone = self.driver.find_element(By.NAME, "phone").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_city = self.driver.find_element(By.NAME, "city").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_country = self.driver.find_element(By.NAME, "country").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_job_position = self.driver.find_element(By.NAME, "job-position").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
    form_company = self.driver.find_element(By.NAME, "company").send_key(By.CSS_SELECTOR, "button[type='{button_text}']")
   
  def click_button(self, button_text):
    button = self.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()

  def red_pole(self, pole0):
    pole_0 = self.driver.find_element(By.CSS_SELECTOR, "pole0").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"
  
  def green_pole(self, pole):
    pole_class = driver.find_element(By.CSS_SELECTOR, "pole").get_attribute("class")
    assert pole_class == "alert py-2 alert-success"

  def get_form_results(self):
    WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located(self.results_selector)
    )
    return self.driver.find_elements()
    