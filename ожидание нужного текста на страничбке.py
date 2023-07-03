import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

url = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 12)

try:

    browser.get(url)
    book = browser.find_element(By.ID, "book")
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.ID, "solve")
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    time.sleep(5)
    alert.accept()
    print(alert_text)

finally:
    time.sleep(5)
    browser.quit()
