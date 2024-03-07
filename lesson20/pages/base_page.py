from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, wait_time=3):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locator_discount = ('xpath', '//nav[@class="header__menu"]/a[@href="/page/diskontna-programa"]')

    def wait_until_element_presence(self, locator:tuple):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator, scroll=False):
        if scroll:
            self.scroll_a_bit()
        element = self.wait_until_element_presence(locator)
        element.click()

    def click_header_discount(self):
        self.click_on_element(self.locator_discount)

    def scroll_a_bit(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(200, 200).perform()

