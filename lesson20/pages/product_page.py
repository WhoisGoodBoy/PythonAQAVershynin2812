from lesson20.pages.base_page import BasePage
from lesson20.core import ProductLocators


class Product(BasePage):
    def __init__(self, driver, start_page=False):
        super().__init__(driver)
        if start_page:
            self.driver.get(start_page)
        self.locators = ProductLocators

    def click_buy_one(self):
        self.click_on_element(self.locators.change_to_tuple())

    def click_buy_multiple(self):
        self.click_on_element(self.locators.locator_button_buy_multiple)

    def click_add_to_favourite(self):
        self.click_on_element(self.locators.locator_add_to_favourite)

    def return_favourite_button(self):
        button = self.wait_until_element_presence(self.locators.locator_add_to_favourite_is_active)
        return button.get_attribute('class')
