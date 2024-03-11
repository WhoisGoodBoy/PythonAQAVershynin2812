from.base_locators import BaseLocators
class DasboardLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_sale = ('xpath', '//a[@class="categories__item"][@href="category/koti/goduvannia-petslike/sale-gift"]')
