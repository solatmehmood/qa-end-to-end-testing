import pytest
from Automation.ToolShop.pages.login import Login

"""....... Login with valid credentials ....... """
@pytest.mark.order(2)
def test_login_with_valid_credentials(driver,unique_email):
    # Create Login page object
    login = Login(driver)
    # Open login page
    login.open_loginPage()
    # Fill login form
    login.fill_loginForm(unique_email, "Test@!987")
    # Click login button
    login.click_login()

"""....... Login with invalid credentials ....... """
@pytest.mark.order(3)
def test_login_with_invalid_credentials(driver):
    # Create Login page object
    login=Login(driver)
    # Open login page
    login.open_loginPage()
    # Fill login form with invalid credentials
    login.fill_loginForm("test13434@gmail.com","Test@!98")
    # Click login button
    login.click_login()


