from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service as FirefoxService
from webdriver_manager.common import GeckoDriverManager


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.XPATH, '//input[@id="username"]')
username_input.send_keys("tomsmith", Keys.RETURN)

password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
password_input.send_keys("SuperSecretPassword!", Keys.RETURN)

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()


driver.quit()
