from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import Login

def test_login(driver):
    # Create Login page object
    login = Login(driver)
    # Open login page
    login.open_loginPage()
    # Fill login form
    login.fill_loginForm("test134@gmail.com", "Test@!9876")
    # Click login button
    login.click_login()
    # Wait until URL contains 'account'
    WebDriverWait(driver, 10).until(EC.url_contains("account"))
    # Assert login success
    assert "account" in driver.current_url, "Login Failed"
    print(f"Login Success: {driver.current_url}")
