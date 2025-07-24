from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form(driver):
    # Открытие страницы
    driver = webdriver.Firefox()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажатие кнопки
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки поля Zip code
    zip_code_input = driver.find_element(By.NAME, "zip")
    assert "red" in zip_code_input.get_attribute(
        'style'), "Поле Zip code не подсвечено красным"

    # Проверка подсветки остальных полей
    fields = ["firstName", "lastName", "address", "email", "phone", "city", "country", "job", "company"]
    for field in fields:
        element = driver.find_element(By.NAME, field)
        assert "green" in element.get_attribute(
            'style'), f"Поле {field} не подсвечено зелёным"


driver.quit()
