from selenium.webdriver.common.by import By

class Register:
    def __init__(self, driver):
        self.driver = driver

    """....... Open the Register page ....... """
    def open_signup_page(self):
        # Open the signup page
        self.driver.get("https://practicesoftwaretesting.com/auth/register")

    """....... Fill the Register form ....... """
    def fill_signupForm(self):
        # Get the form elements
        firstName = self.driver.find_element(By.ID, "first_name")
        lastName = self.driver.find_element(By.ID, "last_name")
        dob = self.driver.find_element(By.ID, "dob")
        address = self.driver.find_element(By.ID, "street")
        postCode = self.driver.find_element(By.ID, "postal_code")
        city = self.driver.find_element(By.ID, "city")
        state = self.driver.find_element(By.ID, "state")
        country = self.driver.find_element(By.ID, "country")
        phone = self.driver.find_element(By.ID, "phone")
        email = self.driver.find_element(By.ID, "email")
        password = self.driver.find_element(By.ID, "password")

        # Fill the form elements
        firstName.send_keys("test")
        lastName.send_keys("user")
        dob.send_keys("1990-08-18")
        address.send_keys("First floor DHA")
        postCode.send_keys("42321")
        city.send_keys("Lahore")
        state.send_keys("Punjab")
        country.send_keys("Pakistan")
        phone.send_keys("0314509876")
        email.send_keys("test1344@gmail.com")
        password.send_keys("Test@!9876")

    """....... Submit the signup form ....... """
    def submit_form(self):
        # Click the register button
        register_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()

