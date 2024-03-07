from lesson20.pages.base_page import BasePage


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_first_product_by_google = ('xpath', '/html/body/div[1]/main/div[2]/div/div/div/div[3]/div/div[1]/div[1]/div[2]/a')
        self.locator_first_product_by_me = ('xpath', '//div[@class="catalog__item"]//div[@class="card"][1]//div[@class="card__preview"]/a/img')
        self.locator_checkbox_purina = ('xpath', '//a[@href="/category/koti/goduvannia-petslike/sale-gift-purina"]')

    def click_first_product(self):
        self.click_on_element(self.locator_first_product_by_me, True)

    def click_checkbox_purina(self):
        self.click_on_element(self.locator_checkbox_purina, True)
