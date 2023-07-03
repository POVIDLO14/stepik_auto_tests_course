import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = None
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)

    magic = browser.find_element(By.CLASS_NAME, "btn")
    magic.click()

    time.sleep(2)

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

    time.sleep(2)

    #submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    #submit.click()

finally:
    time.sleep(5)
    browser.quit()
