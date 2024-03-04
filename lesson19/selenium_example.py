from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_01():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    search_locator = '//textarea[@aria-label="Пошук"]'
    search_element = driver.find_element(by='xpath', value=search_locator)
    search_element.send_keys('повернись живим')
    search_element.send_keys(Keys.ENTER)
    first_non_ad_result_locator = '//div[@id="search"]/div[1]/div//h3[contains(text(), "- допомoга ЗСУ")]/..'
    first_element = driver.find_element('xpath', first_non_ad_result_locator)
    first_element.click()
    assert driver.title == 'Благодійний фонд "Повернись живим" - допомoга ЗСУ'
    driver.quit()
    time.sleep(3)

def test_actionchains():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    search_locator = '//textarea[@aria-label="Пошук"]'
    search_element = driver.find_element(by='xpath', value=search_locator)
    search_element.send_keys('повернись живим')
    actions = ActionChains(driver)
    time.sleep(2)
    actions.key_down(Keys.CONTROL).key_down('a').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    actions.key_down(Keys.CONTROL).key_down('x').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    search_element.click()
    actions.key_down(Keys.CONTROL).key_down('v').key_up(Keys.CONTROL).perform()
    time.sleep(2)

