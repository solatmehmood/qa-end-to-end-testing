import time
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def unique_email():
    # sirf email unique hoga
    timestamp = str(int(time.time()))
    return f"test{timestamp[-5]}@gmail.com"