from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    remove_from_cart = (By.XPATH, "//button[text() = 'Remove']")

    def get_remove_from_cart(self):
        return self.driver.find_elements(*self.remove_from_cart)
