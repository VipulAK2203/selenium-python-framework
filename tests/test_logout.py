from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login=LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    inventory=InventoryPage(driver)

    inventory.click_logout_btn()
    assert login.check_logout_success() is True
