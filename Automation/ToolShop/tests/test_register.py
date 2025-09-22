import pytest
from Automation.ToolShop.pages.register import Register

""" ....... Register a new user ....... """
@pytest.mark.order(1)
def test_signup(driver,unique_email):
    # Create Register page object
    register = Register(driver)
    # Open signup page
    register.open_signup_page()
    # Fill signup form
    register.fill_signupForm(unique_email,"Test@!987")
    # Submit the form
    register.submit_form()
