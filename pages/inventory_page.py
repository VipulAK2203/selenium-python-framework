from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.CLASS_NAME, "inventory_item")
    add_to_cart = (By.XPATH, "//button[contains(text(), 'Add To Cart')]")
    to_cart = (By.XPATH, "//a[@class = 'shopping_cart_link']")

    def get_products(self):
        return self.driver.find_elements(*self.products)

    def get_product(self, item_name):
        return self.driver.find_element(By.XPATH, f"//div[contains(text(), {item_name})]")

    def get_add_to_cart(self, item_name):
        item_name = item_name.lower()
        item_name = item_name.replace(" ", "-")
        self.driver.find_element(By.XPATH, f"//button[contains(@name, '{item_name}')]").click()

    def get_to_cart(self):
        self.driver.find_element(*self.to_cart).click()
