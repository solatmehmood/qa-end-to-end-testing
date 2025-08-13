import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver

    """....... Navigate to homepage and open the login page ....... """
    def open_loginPage(self):
        # Launch the website
        self.driver.get("https://practicesoftwaretesting.com/")
        # Click the 'Sign in' link and wait until it is clickable
        sign_in_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign in']"))
        )
        sign_in_link.click()
        time.sleep(2)

    """....... Fill the login form ....... """
    def fill_loginForm(self, email, password):
        # Locate email and password input fields
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        # Fill inputs
        email_input.send_keys(email)
        password_input.send_keys(password)

    """....... Click the login button ....... """

    def click_login(self):
        # Click the login button
        login_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()

        # Verify if the user logged in successfully or not
        try:
            # Wait until URL contains 'account' (successful login indicator)
            WebDriverWait(self.driver, 10).until(EC.url_contains("account"))
            assert "account" in self.driver.current_url, "Login Failed"
        except:
            try:
                # Wait for the error message element to appear (invalid login case)
                error_msg = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger']"))
                )
                print(f"Login Failed: {error_msg.text}")
            except:
                # No redirect and no error message found within the wait time
                print("Login Failed: Timeout waiting for success or error message.")
        else:
            # Runs only if the try block completes successfully without exceptions
            print("Login Successfully")
