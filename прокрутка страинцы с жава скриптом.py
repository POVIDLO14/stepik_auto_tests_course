import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = None
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    inputX = browser.find_element(By.ID, "answer")
    inputX.send_keys(y)

    robot1 = browser.find_element(By.ID, "robotCheckbox")
    robot1.click()

    robot2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot2)
    robot2.click()

    time.sleep(2)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(9)
    browser.quit()
