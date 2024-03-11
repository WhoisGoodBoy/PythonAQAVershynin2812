from.base_locators import BaseLocators
class CategoryLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_first_product_by_google = ('xpath', '/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/div[1]/div[1]/div[2]/a')
        self.locator_first_product_by_me = ('xpath', '//div[@class="catalog__item"]//div[@class="card"][1]//div[@class="card__preview"]/a/img')
        self.locator_checkbox_purina = ('xpath', '//a[@href="/category/koti/goduvannia-petslike/sale-gift-purina"]')
