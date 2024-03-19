import pytest
from argparse import ArgumentParser
from selenium.webdriver import Chrome, Firefox

def pytest_addoption(parser):
    parser.addoption('--driver_to_pass', action='store')

@pytest.fixture(scope='session')
def driver_to_pass(request):
    driver_name = request.config.option.driver_to_pass
    driver = None
    if driver_name == 'chrome':
        driver = Chrome()
    elif driver_name == 'firefox':
        driver = Firefox()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    driver.implicitly_wait(7)
    yield driver
    driver.close()
