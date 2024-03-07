


def test_first_product(sale):
    sale.click_first_product()
    assert sale.driver.title == 'Purina Pro Plan Sterilised Adult Chicken - вологий корм у соусі з куркою для стерилізованих котів купити в Україні - Зоомагазин Petslike.net'

def test_checkbox_and_first_product(sale):
    sale.click_checkbox_purina()
    sale.click_first_product()
    assert sale.driver.title == 'Purina Pro Plan Sterilised Adult Chicken - вологий корм у соусі з куркою для стерилізованих котів купити в Україні - Зоомагазин Petslike.net'
