import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    # options = Options()
    if browser == "chrome":
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("Launching Chrome browser.....")
        # return driver
    elif browser == "edge":
        # driver = webdriver.Edge()
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser.....")
    else:
        # driver = webdriver.Chrome()
        driver = webdriver.Firefox(service=ChromeService(ChromeDriverManager().install()))
        print("Launching Firefox browser.....")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")
