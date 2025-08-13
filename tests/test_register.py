import pytest
from pages.register import Register

@pytest.mark.order(1)
def test_signup(driver):
    # Create Register page object
    register = Register(driver)
    # Open signup page
    register.open_signup_page()
    # Fill signup form
    register.fill_signupForm()
    # Submit the form
    register.submit_form()
