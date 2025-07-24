from time import sleep
from selenium import webdriver
from selenium.webdriver.common.service import Service as ChromeService
from webdriver_manager.common import ChromeDriverManager
from seleniun.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get('http://uitestingplayground.com/dynamicid')


button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
sleep(2)
button.click()


driver.quit()
