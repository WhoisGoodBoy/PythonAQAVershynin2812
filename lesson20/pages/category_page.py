from lesson20.pages.base_page import BasePage
from lesson20.pages.product_page import Product
from lesson20.core import CategoryLocators


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocators()

    def click_first_product(self):
        self.click_on_element(self.locators.locator_first_product_by_me, True)
        return Product(self.driver)

    def click_checkbox_purina(self):
        self.click_on_element(self.locators.locator_checkbox_purina, True)
