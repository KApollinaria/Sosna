import pytest
from selenium import webdriver
from shop_page import ShopPage


@pytest.fixture()
def driver():
  driver = webdriver.Firefox()
  yield driver
  driver.quit()

def test_shop(driver):
  driver.maximize_window()
  driver.get("https://www.saucedemo.com/")
  shop = ShopPage(driver)
  shop.shop_for("standard_user")
  shop.shop_for("secret_sauce")
  shop.click_button("login")

  shop.first_name_field("Аполлинария")
  shop.last_name_field("Коровкина")
  shop.postal_code_field("12345")

  shop.click_button("continue")
  shop.total_cost(58.29)

  assert shop.get_shop_results() 
