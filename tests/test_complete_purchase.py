import pytest
from pages.product_page import ProductPage
from pages.view_cart import ViewCart
from pages.checkout import Checkout

""" ....... Complete purchase flow starting from product selection ....... """
@pytest.mark.order(4)
def test_complete_purchase(driver):
    # Create ProductPage object
    product_page = ProductPage(driver)

    """ ....... Open the product and add it to cart ....... """
    # Open the product detail page
    product_page.select_product()
    # Add the product to cart
    product_page.add_to_cart()

    """ ....... View the cart page ....... """
    cart_page=ViewCart(driver)
    # View the cart page
    cart_page.view_cart()

    """ ...... Proceed to checkout page ....... """
    checkout_page=Checkout(driver)
    # Go to checkout page
    checkout_page.proceed_to_checkout()

    """ ...... Proceed to billing page and confirm the order ....... """
    # Go to billing page and fill the details
    checkout_page.billing_page()
    # Select payment method
    checkout_page.payment_selection()
    # Place the order
    checkout_page.order_placed()
     # Order confirmation
    checkout_page.order_confirmation()
