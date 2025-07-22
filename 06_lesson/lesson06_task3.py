from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from seleniun.webdriver.chrome.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')


element = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), 'Donel')
)

src = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')

print(src)

driver.quit()
