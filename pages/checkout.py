import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from tests.conftest import unique_email


class Checkout:
    def __init__(self,driver):
        self.driver=driver

    """....... Proceed to checkout page ....... """
    def proceed_to_checkout(self,email,password):
        proceed_toCheckout_button = self.driver.find_element(By.XPATH, "//button[text()='Proceed to checkout']")
        assert proceed_toCheckout_button.is_displayed(),"Cart page is not opened"
        proceed_toCheckout_button.click()

        # Wait for the element to visible
        email_field=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"email")))

        # Check if email field is displayed (means user is not logged in)
        if email_field.is_displayed():
            # Locate the password input field
            password_field = self.driver.find_element(By.ID, "password")

            # Enter email and password
            email_field.send_keys(email)
            password_field.send_keys(password)

            # Click the login button
            login_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
            login_button.click()

            # After login, click the Proceed to checkout button
            proceed_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='proceed-2']"))
            )
            proceed_btn.click()

        # If already logged in, directly click the Proceed to checkout button
        else:
            proceed_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='proceed-2']"))
            )
            proceed_btn.click()

    """....... Proceed to billing page and fill the details ....... """
    def billing_page(self):
        # Getting the billing form elements
        address = self.driver.find_element(By.ID, "street")
        city = self.driver.find_element(By.ID, "city")
        state = self.driver.find_element(By.ID, "state")
        country = self.driver.find_element(By.ID, "country")
        postCode = self.driver.find_element(By.ID, "postal_code")

        # Clear the fields
        address.clear()
        city.clear()
        state.clear()
        country.clear()
        postCode.clear()

        # Fill the billing details
        address.send_keys("First")
        city.send_keys("Lahore")
        state.send_keys("Punjab")
        country.send_keys("UK")
        postCode.send_keys("42321")

        # Click the proceed button
        proceed_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='float-end']//button[@type='button'][normalize-space()='Proceed to checkout']"))
        )
        proceed_btn.click()
        time.sleep(3)

    """....... Placed the order ....... """
    def order_placed(self):
        order_confirm_button=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Confirm']")))
        order_confirm_button.click()

    """....... Confirm order is placed or not ....... """
    def order_confirmation(self):
        confirmation_msg=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='help-block']")))
        assert confirmation_msg.is_displayed(),"Order is not placed"
        print(f"Order is placed, {confirmation_msg.text}")



