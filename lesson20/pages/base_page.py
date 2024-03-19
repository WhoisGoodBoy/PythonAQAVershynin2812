from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lesson20.core import BaseLocators


class BasePage:
    def __init__(self, driver, wait_time=3):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locators = BaseLocators()



    def wait_until_element_presence(self, locator:tuple):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator, scroll=False):
        if scroll:
            self.scroll_a_bit()
        element = self.wait_until_element_presence(locator)
        element.click()

    def click_header_discount(self):
        self.click_on_element(self.locators.locator_discount)

    def scroll_a_bit(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(200, 200).perform()

    def return_cart_counter(self):
        cart_counter = self.wait_until_element_presence(self.locators.locator_cart_items_counter)
        return int(cart_counter.text)


    def navigate_to_dogs(self):
        dogs = self.wait_until_element_presence(self.locators.locator_for_dogs)
        actions = ActionChains(self.driver)
        actions.move_to_element(dogs).perform()
        dry_feed = self.wait_until_element_presence(self.locators.locator_dry_feed)
        return dry_feed.is_displayed()

    def navigate_to_category(self,category, items_list):
        category_object = self.wait_until_element_presence(category)
        actions = ActionChains(self.driver)
        actions.move_to_element(category_object).perform()
        for item in items_list:
            item_object = self.wait_until_element_presence(item)
            assert item_object.is_displayed()


