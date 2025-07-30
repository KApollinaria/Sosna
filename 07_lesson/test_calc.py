import pytest
from selenium import webdriver
from calc_page import Calc


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    calc.calc_delay(45)
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")
    result = calc.get_result()
    assert result == "15"
