from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [[driver.find_element_by_id("productName" + str(i)), driver.find_element_by_id("productPrice" + str(i))] for i in range(3, -1, -1)]

#print(items)

actions = ActionChains(driver)
actions.click(cookie)

for i in range(2000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item_name, item_value in items:
        value = int(item_value.text)
        if value <= count:
            building_actions = ActionChains(driver)
            building_actions.move_to_element(item_name)
            building_actions.click()
            building_actions.perform()
            print("Just bought {} for {} cookies...".format(item_name.text, value))
