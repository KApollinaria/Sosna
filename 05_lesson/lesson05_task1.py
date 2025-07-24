from selenium import webdriver
from selenium.webdriver.common.service import Service as ChromeService
from webdriver_manager.common import ChromeDriverManager
from seleniun.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get('http://uitestingplayground.com/classattr')


button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
button.click()
alert = driver.switch_to.alert


driver.quit()
