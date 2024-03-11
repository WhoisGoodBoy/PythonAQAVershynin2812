class BaseLocators:
    def __init__(self):
        self.locator_discount = ('xpath', '//nav[@class="header__menu"]/a[@href="/page/diskontna-programa"]')
        self.locator_cart_items_counter = ('xpath', '//a[@class="header__action header__action_cart js-header-cart"]/div/div')
