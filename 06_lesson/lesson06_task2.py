from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from seleniun.webdriver.chrome.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get('http://uitestingplayground.com/textinput')


input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
input.send_kyes('SkyPro')
click = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print()

driver.quit
