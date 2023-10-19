import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching Chrome browser.....")
        # return driver
    elif browser == "edge":
        # driver = webdriver.Edge()
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser.....")
    else:
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching Chrome browser.....")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):          # This will return the browser value to setup method
    return request.config.getoption("--browser")

