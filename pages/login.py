import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver

    def open_loginPage(self):
        # Launch the website
        self.driver.get("https://practicesoftwaretesting.com/")
        # Click the 'Sign in' link and wait until it is clickable
        sign_in_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign in']"))
        )
        sign_in_link.click()
        time.sleep(3)

    def fill_loginForm(self, email, password):
        # Locate email and password input fields
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        # Fill inputs
        email_input.send_keys(email)
        password_input.send_keys(password)

    def click_login(self):
        # Click the login button
        login_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()
        time.sleep(3)
