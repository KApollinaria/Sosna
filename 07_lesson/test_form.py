import pytest
from selenium import webdriver
from form_page import Form

@pytest.fixture()
def driver():
  driver = webdriver.Firefox()
  yield driver
  driver.quit()

def test_form(driver):
  driver.maximize_window()
  driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
  form.first-name("Иван")
  form.last-name("Петров")
  form.address("Ленина, 55-3")
  form.e-mail("test@skypro.com")
  form.phone("+7985899998787")
  form.city("Москва")
  form.country("Россия")
  form.job-position("QA")
  form.company("SkyPro")
  
  form.click_button("submit")
  form.red_pole("#zip_code")
  form.green_pole("#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company")
  form.get_form_results()