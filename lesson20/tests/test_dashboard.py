from lesson20.pages.category_page import CategoryPage
from lesson20.core.locators.base_locators import BaseLocators
from lesson20.core.datasample import dogs_list,cats_list
import time
import pytest

def test_go_to_sale(dashboard):
    dashboard.click_sale()
    sale = CategoryPage(dashboard.driver)
    sale.click_first_product()
    assert dashboard.driver.title == 'Харчування - Акційні пропозиції З подарунком | інтернет-магазин petslike.ua'

def test_go_to_discount(dashboard):
    dashboard.click_header_discount()
    assert dashboard.driver.title == 'Дисконтна програма | зоомагазин, Україна'

def test_go_to_discount_and_check_product(dashboard,sale,purina_pro_plan_chicken):
    dashboard.click_header_discount()
    sale.click_checkbox_purina()
    sale.click_first_product()
    purina_pro_plan_chicken.click_add_to_favourite()

@pytest.mark.parametrize('category,list_of_subcategories',[(BaseLocators.locator_for_dogs,dogs_list),(BaseLocators.locator_for_cats,cats_list)])
def test_navigate_to_dogs(dashboard,category,list_of_subcategories):
    dashboard.navigate_to_category(category, list_of_subcategories)
    time.sleep(5)
