

def test_01(driver_to_pass):
    search_locator = '//textarea[@aria-label="Пошук"]'
    search_element = driver_to_pass.find_element(by='xpath', value=search_locator)
    search_element.send_keys('повернись живим')
