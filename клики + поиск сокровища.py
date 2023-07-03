import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    treasure_checked = x_element.get_attribute("valuex")
    x = treasure_checked
    y = calc(x)
    print(treasure_checked)
    print(y)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    robotCheckbox1 = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox1.click()

    robotRadiobutton1 = browser.find_element(By.ID, "robotsRule")
    robotRadiobutton1.click()

    pressSubmit1 = browser.find_element(By.CLASS_NAME, "btn")
    pressSubmit1.click()
finally:
    time.sleep(9)
    browser.quit()