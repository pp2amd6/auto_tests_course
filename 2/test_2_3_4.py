import time
import calc

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x = browser.find_element(By.ID, "input_value").text
    result = calc.calc(x)
    
    field_result = browser.find_element(By.ID, "answer")
    field_result.send_keys(result)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
