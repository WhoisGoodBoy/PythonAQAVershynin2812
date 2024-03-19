class BaseLocators:
    locator_for_dogs = (
    'xpath', '//div[@class="menu__item js-menu-item"]/a[@href="https://petslike.ua/category/sobaki"]')
    locator_for_cats = (
    'xpath', '//div[@class="menu__item js-menu-item"]/a[@href="https://petslike.ua/category/koti"]')
    def __init__(self):
        self.locator_discount = ('xpath', '//nav[@class="header__menu"]/a[@href="/page/diskontna-programa"]')
        self.locator_cart_items_counter = ('xpath', '//a[@class="header__action header__action_cart js-header-cart"]/div/div')

        self.locator_dry_feed = ('xpath', '//div[@class="menu__links js-menu-links"]/a[@href="https://petslike.ua/category/sobaki/goduvannia/sukhi-kormi"]')