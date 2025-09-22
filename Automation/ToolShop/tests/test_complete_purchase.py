import pytest
from Automation.ToolShop.pages.product_page import ProductPage
from Automation.ToolShop.pages.view_cart import ViewCart
from Automation.ToolShop.pages.checkout import Checkout
from Automation.ToolShop.pages.payment import PaymentMethod
from Automation.ToolShop.tests.conftest import unique_email

""" ....... Complete purchase with Cash on Delivery ....... """

@pytest.mark.order(4)
def test_purchase_with_COD(driver,unique_email):
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
    checkout_page.proceed_to_checkout(unique_email,"Test@!987")

    """ ...... Proceed to billing page and confirm the order ....... """
    # Go to billing page and fill the details
    checkout_page.billing_page()
    # Select payment method
    payment_selection=PaymentMethod(driver)

    payment_selection.select_COD()
    # Place the order
    checkout_page.order_placed()
     # Order confirmation
    checkout_page.order_confirmation()

""" ....... Complete purchase with Bank Transfer ....... """
@pytest.mark.order(5)
def test_purchase_with_bank_transfer(driver,unique_email):
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
    checkout_page.proceed_to_checkout(unique_email,"Test@!987")

    """ ...... Proceed to billing page and confirm the order ....... """
    # Go to billing page and fill the details
    checkout_page.billing_page()
    # Select payment method
    payment_selection=PaymentMethod(driver)

    payment_selection.select_bank_transfer()
    # Place the order
    checkout_page.order_placed()
     # Order confirmation
    checkout_page.order_confirmation()

""" ....... Complete purchase with Credit Card ....... """

@pytest.mark.order(6)
def test_purchase_with_credit_card(driver,unique_email):
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
    checkout_page.proceed_to_checkout(unique_email,"Test@!987")

    """ ...... Proceed to billing page and confirm the order ....... """
    # Go to billing page and fill the details
    checkout_page.billing_page()
    # Select payment method
    payment_selection=PaymentMethod(driver)

    payment_selection.select_credit_card()
    # Place the order
    checkout_page.order_placed()
     # Order confirmation
    checkout_page.order_confirmation()
