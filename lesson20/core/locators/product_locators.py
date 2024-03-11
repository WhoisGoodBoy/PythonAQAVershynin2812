from.base_locators import BaseLocators
class ProductLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.locator_button_buy_one = ('xpath', '//div[@class="product__control"]/div[1]//a')
        self.locator_button_buy_multiple = ('xpath', '//div[@class="product__control"]/div[2]//a')
        self.locator_add_to_favourite = ('xpath', '//div[@class="product__line"]/div[@class="actions"]/button[@class="actions__button js-favorite-product "]')
        self.locator_add_to_favourite_is_active = ('xpath','//div[@class="product__line"]/div[@class="actions"]/button[@class="actions__button js-favorite-product active"]')
