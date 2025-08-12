from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.register import Register

def test_signup(driver):
    # Create Register page object
    register = Register(driver)
    # Open signup page
    register.open_signup_page()
    # Fill signup form
    register.fill_signupForm()
    # Submit the form
    register.submit_form()
    # Wait until URL contains 'login'
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    # Assert signup success
    assert "login" in driver.current_url, "Signup Failed"
