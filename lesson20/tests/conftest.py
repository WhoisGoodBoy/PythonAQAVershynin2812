import pytest
from selenium.webdriver import Chrome
from lesson20.pages.dashboard_page import Dashboard
from lesson20.pages.category_page import CategoryPage
from lesson20.pages.product_page import Product


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

@pytest.fixture
def purina_pro_plan_chicken(driver):
    driver.get('https://petslike.ua/purina-pro-plan-sterilised-nutrisavour-cats-chicken-sauce')
    print(f"Cookies:{driver.get_cookies()}")
    print(f"Cookies:{driver.add_cookie({'name':'mysterious_cookie', 'value':'misterious_value'})}")
    print(f"Single cookie:{driver.get_cookie('mysterious_cookie')}")
    driver.execute_script('window.localStorage["es_webpush_inited"]=2')
    print(driver.execute_script('return window.localStorage["es_webpush_inited"];'))
    yield Product(driver)
