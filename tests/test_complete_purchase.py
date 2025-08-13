import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.product_page import ProductPage

""" ....... Complete purchase flow starting from product selection ....... """
def test_complete_purchase(driver):
    # Create ProductPage object
    product_page = ProductPage(driver)

    """ ....... Open the product and add it to cart ....... """
    # Open the product detail page
    product_page.select_product()
    # Add the product to cart
    product_page.add_to_cart()
    # Wait for the product added toaster
    cart_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "toast-container"))
    )
    # Verify product added or not
    assert cart_msg.is_displayed(),"Product not added"
    print(cart_msg.text)

    """ ....... View the cart page ....... """