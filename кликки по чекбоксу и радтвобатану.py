import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    robotCheckbox1 = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox1.click()

    robotradiobutton1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robotradiobutton1.click()

    pressSubmit1 = browser.find_element(By.CLASS_NAME, "btn")
    pressSubmit1.click()
finally:
    time.sleep(9)
    browser.quit()