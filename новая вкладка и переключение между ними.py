import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = None
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)

    troll = browser.find_element(By.CLASS_NAME, "trollface")
    troll.click()

    time.sleep(2)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
