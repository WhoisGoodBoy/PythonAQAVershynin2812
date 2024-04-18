import pytest
from playwright.sync_api import sync_playwright
from lesson32.product_page import ProductPage




url = "https://petslike.ua/"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page
        page.close()

@pytest.fixture
def product_page(page):
    page.goto('https://petslike.ua/olenina-z-m-iasom-kurki-konservi-dlia-kotiv')
    yield ProductPage(page)