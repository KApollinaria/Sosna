from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.service import Service as FirefoxService
from webdriver_manager.common import GeckoDriverManager


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get('http://the-internet.herokuapp.com/inputs')

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "input"))
)

input_field.send_keys("Sky")

input_field.clear()

input_field.send_keys("Pro")


driver.quit()
