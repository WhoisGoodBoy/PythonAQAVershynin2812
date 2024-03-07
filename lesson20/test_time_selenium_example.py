from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_with_explicit_wait(driver, locator, time_in_seconds):
    web_driver_wait = WebDriverWait(driver, time_in_seconds)
    element = web_driver_wait.until(EC.presence_of_element_located(locator))
    return element


def test_01():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    driver.implicitly_wait(7)
    search_locator = '//textarea[@aria-label="Пошук"]'
    search_element = driver.find_element(by='xpath', value=search_locator)
    search_element.send_keys('повернись живим')


def test_02():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    search_locator = ('xpath', '//textarea[@aria-label="Пошук"]')
    search_element = find_with_explicit_wait(driver, search_locator, 7)
    search_element.send_keys('повернись живим')