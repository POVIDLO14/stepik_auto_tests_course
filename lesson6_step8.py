from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
input1.send_keys("Ivan")
input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
input2.send_keys("Petrov")
input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
input3.send_keys("Petrov@mail.ru")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
welcome_text = browser.find_element(By.TAG_NAME, "h1").text
welcome_text = welcome_text
assert "Congratulations! You have successfully registered!" == welcome_text
time.sleep(10)
browser.quit()

