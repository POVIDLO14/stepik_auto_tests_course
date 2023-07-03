import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select



browser = None
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Михаил")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Зубенко")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("Мафиозник")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "bio.txt"
    file_path = os.path.join(current_dir, file_name)
    file_put = browser.find_element(By.ID, "file")
    file_put.send_keys(file_path)

    time.sleep(2)

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()

finally:
    time.sleep(9)
    browser.quit()
