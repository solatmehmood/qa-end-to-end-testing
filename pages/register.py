import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Register:
    def __init__(self,driver):
        self.driver=driver

    def open_signup_page(self):
        #........ Opening the signup Page .........
        self.driver.get("https://practicesoftwaretesting.com/auth/register")

    def fill_signupForm(self):
        #........ Getting the form elements .......
        firstName=self.driver.find_element(By.ID,"first_name")
        lastName=self.driver.find_element(By.ID,"last_name")
        dob=self.driver.find_element(By.ID,"dob")
        address=self.driver.find_element(By.ID,"street")
        postCode=self.driver.find_element(By.ID,"postal_code")
        city=self.driver.find_element(By.ID,"city")
        state=self.driver.find_element(By.ID,"state")
        country=self.driver.find_element(By.ID,"country")
        phone=self.driver.find_element(By.ID,"phone")
        email=self.driver.find_element(By.ID,"email")
        password=self.driver.find_element(By.ID,"password")
        #........ Filling the form elements ..........
        firstName.send_keys("test")
        lastName.send_keys("user")
        dob.send_keys("1990-08-18")
        address.send_keys("First floor DHA")
        postCode.send_keys("42321")
        city.send_keys("Lahore")
        state.send_keys("Punjab")
        country.send_keys("Pakistan")
        phone.send_keys("0314509876")
        email.send_keys(f"user{str(int(time.time()))}@gmail.com")
        password.send_keys("Test@!9876")

    def submit_form(self):
        #...... Click the register button .......
        register_button=self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        register_button.click()
        time.sleep(5)







