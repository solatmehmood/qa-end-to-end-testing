import time
import pytest
from selenium import webdriver

# Add command line option for browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome, firefox, edge")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use chrome, firefox, or edge.")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def unique_email():
    timestamp = str(int(time.time()))
    return f"test{timestamp[-5:]}@gmail.com"
