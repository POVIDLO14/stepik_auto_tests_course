import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://ya.ru"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.ID, 'text')
input1.send_keys("Смешные преколы с котятами")
time.sleep(3)

pressFind = browser.find_element(By.CLASS_NAME, "search3__button.mini-suggest__button")
pressFind.click()

time.sleep(3)
browser.quit()