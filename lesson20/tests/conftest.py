import pytest
from selenium.webdriver import Chrome
from lesson20.pages.dashboard_page import Dashboard
from lesson20.pages.category_page import CategoryPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def dashboard(driver):
    driver.get('https://petslike.ua/')
    yield Dashboard(driver)


@pytest.fixture
def sale(driver):
    driver.get('https://petslike.ua/category/koti/goduvannia-petslike/sale-gift')
    yield CategoryPage(driver)
