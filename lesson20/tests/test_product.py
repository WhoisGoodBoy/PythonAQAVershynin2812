

def test_bypass_to_purina_from_dashboard(dashboard):
    sale_category = dashboard.click_sale()
    sale_category.click_checkbox_purina()
    purina_product = sale_category.click_first_product()
    assert purina_product.driver.title == 'Purina Pro Plan Sterilised Adult Chicken - вологий корм у соусі з куркою для стерилізованих котів купити в Україні - Зоомагазин Petslike.net'

def test_single_product_added_to_cart(purina_pro_plan_chicken):
    purina_pro_plan_chicken.click_buy_one()
    assert purina_pro_plan_chicken.return_cart_counter() == 1

def test_multiple_product_added_to_cart(purina_pro_plan_chicken):
    purina_pro_plan_chicken.click_buy_multiple()
    assert purina_pro_plan_chicken.return_cart_counter() == 26


def test_check_button_add_to_favourite_works(purina_pro_plan_chicken):
    purina_pro_plan_chicken.click_add_to_favourite()
    assert purina_pro_plan_chicken.return_favourite_button() == 'actions__button js-favorite-product active'