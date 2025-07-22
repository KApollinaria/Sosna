from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from seleniun.webdriver.chrome.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get('http://uitestingplayground.com/dynamicid')

for i in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
    driver.click()
    alart = driver.switch_to.alert
    alart.accept()
    driver.refresh

sleep(50)
