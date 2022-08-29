from selenium import webdriver
import pytest
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=".\\Driverdetails\\chromedriver.exe")
        print("Lunching Chrome Driver")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=".\\Driverdetails\\firefoxdriver.exe")
        print("Lunching Firefox Driver")
    else:
        driver = webdriver.Edge(executable_path=".\\Driverdetails\\msedgedriver.exe")
        print("Lunching edge Driver")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# --- Pytest HTML Report --- #
def pytest_configure(config):
    config._metadata['Project Name'] = 'Axelerant Project'
    config._metadata['Moudule Name'] = 'E-Commerce Website'
    config._metadata['Tester Name'] = 'Debasish'
    config._metadata['Date & Time'] = datetime.now()

@pytest.mark.optionalhook
def pytest_metatdata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)