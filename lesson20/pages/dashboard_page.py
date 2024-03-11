from lesson20.pages.base_page import BasePage
from lesson20.pages.category_page import CategoryPage
from lesson20.core import DasboardLocators


class Dashboard(BasePage):
    def __init__(self, driver, header=None):
        super().__init__(driver)
        self.header = header
        self.locators = DasboardLocators()

    def click_sale(self):
        self.click_on_element(self.locators.locator_sale)
        return CategoryPage(self.driver)
