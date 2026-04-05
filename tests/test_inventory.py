from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login=LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    inventory=InventoryPage(driver)

    products = inventory.get_products()
    assert len(products) > 0
    inventory.get_add_to_cart('Sauce Labs Bike Light')
    inventory.get_add_to_cart('Sauce Labs Fleece Jacket')