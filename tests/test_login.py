from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import Login

"""....... Login with valid credentials ....... """
def test_login_with_valid_credentials(driver):
    # Create Login page object
    login = Login(driver)
    # Open login page
    login.open_loginPage()
    # Fill login form
    login.fill_loginForm("test1344@gmail.com", "Test@!9876")
    # Click login button
    login.click_login()
    # Wait until URL contains 'account'
    WebDriverWait(driver, 20).until(EC.url_contains("account"))
    # Assert login success
    assert "account" in driver.current_url, "Login Failed"
    print(f"Login Success: {driver.current_url}")

"""....... Login with invalid credentials ....... """
def test_login_with_invalid_credentials(driver):
    # Create Login page object
    login=Login(driver)
    # Open login page
    login.open_loginPage()
    # Fill login form with invalid credentials
    login.fill_loginForm("test1344@gmail.com","Test@!98")
    # Click login button
    login.click_login()
    # Wait until error message appears on page
    error_msg=WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger']"))
    )
    # Assert error message is visible
    assert error_msg.is_displayed(),"Error Message not appeared"
    print(f"Login Failed:{error_msg.text}")


