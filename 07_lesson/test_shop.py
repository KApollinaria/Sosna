import pytest
from selenium import webdriver
from shop_page import Shop


@pytest.fixture()
def driver():
  driver = webdriver.Firefox()
  yield driver
  driver.quit()

def test_shop(driver):
  driver.maximize_window()
  driver.get("https://www.saucedemo.com/")
  shop.enter_username("standard_user")
  shop.enter_password("secret_sauce")
  shop.click_button("login")

  shop.add_item_to_cart("sauce-labs-backpack")
  shop.add_item_to_cart("sauce-labs-bolt-t-shirt")
  shop.add_item_to_cart("sauce-labs-onesie")
  shop.navigate_to_cart()
  
  shop.click_button("checkout")
 
  shop.first_name_field("Аполлинария")
  shop.last_name_field("Коровкина")
  shop.postal_code_field("12345")

  shop.click_button("continue")
  shop.total_cost(58.29)

  assert shop.get_shop_results() 
