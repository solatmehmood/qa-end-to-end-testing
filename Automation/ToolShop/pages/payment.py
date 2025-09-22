from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class PaymentMethod:
    def __init__(self,driver):
        self.driver=driver

    def select_COD(self):
        """....... Select the payment method ....... """
        select_method = self.driver.find_element(By.XPATH, "//select[@id='payment-method']")
        dropdown = Select(select_method)
        # Select cash on delivery
        dropdown.select_by_visible_text("Cash on Delivery")

    def select_bank_transfer(self):
        """....... Select the payment method ....... """
        select_method = self.driver.find_element(By.XPATH, "//select[@id='payment-method']")
        dropdown = Select(select_method)
        # Select bank transfer
        dropdown.select_by_visible_text("Bank Transfer")
        bank_name=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"bank_name")))
        account_name=self.driver.find_element(By.ID,"account_name")
        account_num=self.driver.find_element(By.ID,"account_number")

        bank_name.send_keys("UBL")
        account_name.send_keys("Test User")
        account_num.send_keys("9876556788765430010")

    def select_credit_card(self):
        """....... Select the payment method ....... """
        select_method = self.driver.find_element(By.XPATH, "//select[@id='payment-method']")
        dropdown = Select(select_method)
        # Select bank transfer
        dropdown.select_by_visible_text("Credit Card")
        card_num = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "credit_card_number")))
        expiry_date = self.driver.find_element(By.ID, "expiration_date")
        cvv = self.driver.find_element(By.ID, "cvv")
        card_holder_name=self.driver.find_element(By.ID, "card_holder_name")

        card_num.send_keys("9876-5567-8876-0098")
        expiry_date.send_keys("10/2030")
        cvv.send_keys("980")
        card_holder_name.send_keys("Test User")
