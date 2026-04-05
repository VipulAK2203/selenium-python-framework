from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    products = (By.CLASS_NAME, "inventory_item")
    add_to_cart = (By.XPATH, "//button[contains(text(), 'Add To Cart')]")
    to_cart = (By.XPATH, "//a[@class = 'shopping_cart_link']")
    options_btn = (By.ID, "react-burger-menu-btn")
    logout_btn = (By.ID, "logout_sidebar_link")

    def get_products(self):
        return self.driver.find_elements(*self.products)

    def get_product(self, item_name):
        return self.driver.find_element(By.XPATH, f"//div[contains(text(), '{item_name}')]")

    def get_add_to_cart(self, item_name):
        item_name = item_name.lower()
        item_name = item_name.replace(" ", "-")
        self.driver.find_element(By.XPATH, f"//button[contains(@name, '{item_name}')]").click()

    def get_to_cart(self):
        self.driver.find_element(*self.to_cart).click()

    def click_logout_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.options_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.logout_btn)).click()