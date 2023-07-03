import time
# import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = None
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1element = browser.find_element(By.ID, "num1")
    num1 = int(num1element.text)

    num2element = browser.find_element(By.ID, "num2")
    num2 = int(num2element.text)
    result = num1 + num2

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))
    # print(treasure_checked)
    print(num1)
    print(num2)
    print(result)

    time.sleep(2)

    pressSubmit1 = browser.find_element(By.CLASS_NAME, "btn")
    pressSubmit1.click()
finally:
    time.sleep(2)
    browser.quit()
