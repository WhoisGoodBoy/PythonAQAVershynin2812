from lesson20.pages.base_page import BasePage


class Dashboard(BasePage):
    def __init__(self, driver, header=None):
        super().__init__(driver)
        self.locator_sale = ('xpath', '//a[@class="categories__item"][@href="category/koti/goduvannia-petslike/sale-gift"]')
        self.header = header
    def click_sale(self):
        self.click_on_element(self.locator_sale)
