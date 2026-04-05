from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

def test_remove_from_cart(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login=LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    cart=CartPage(driver)

    inventory = InventoryPage(driver)

    inventory.get_add_to_cart('Sauce Labs Bike Light')
    inventory.get_add_to_cart('Sauce Labs Fleece Jacket')
    inventory.get_to_cart()

    remove_btn = cart.get_remove_from_cart()
    assert len(remove_btn) > 0
    for btn in remove_btn:
        btn.click()
