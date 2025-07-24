from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get('http://uitestingplayground.com/ajax')


driver.find_element(By.CSS_SELECTOR, '#ajaxBotton').click()
content = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
)

text = content.text


print(text)


driver.quit()
