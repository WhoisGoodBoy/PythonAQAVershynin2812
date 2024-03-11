from lesson20.pages.category_page import CategoryPage

def test_go_to_sale(dashboard):
    dashboard.click_sale()
    assert dashboard.driver.title == 'Харчування - Акційні пропозиції З подарунком | інтернет-магазин petslike.ua'

def test_go_to_discount(dashboard):
    dashboard.click_header_discount()
    assert dashboard.driver.title == 'Дисконтна програма | зоомагазин, Україна'

def test_go_to_discount_and_check_product(dashboard):
    category = dashboard.click_header_discount()
    category.click_checkbox_purina()
    product = category.click_first_product()