import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    """....... Navigate to homepage and select a specific product....... """
    def select_product(self):
        # Open the website
        self.driver.get("https://practicesoftwaretesting.com/")
        time.sleep(2)
        # Click on the product
        self.driver.find_element(By.XPATH, '//img[@alt="Combination Pliers"]').click()
        time.sleep(5)  # Static wait for page load

    """....... Add the selected product to the cart....... """
    def add_to_cart(self):

        # Wait until the 'Add to Cart' button is clickable
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-add-to-cart"))
        )
        cart_button.click()