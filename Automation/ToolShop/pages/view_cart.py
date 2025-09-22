import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ViewCart:
    def __init__(self, driver):
        self.driver = driver

    """....... View the cart page ....... """
    def view_cart(self):
        cart_page=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"lblCartCount")))
        cart_page.click()
        time.sleep(4)