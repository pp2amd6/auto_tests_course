import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "form div.form-group span#input_value")
    x = x_element.text
    result = calc(x)
    
    field_result = browser.find_element(By.ID, "answer")
    field_result.send_keys(result)
    
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()
    
    radiobutton_robot = browser.find_element(By.ID, "robotsRule")
    radiobutton_robot.click()
    
    button_submit = browser.find_element(By.TAG_NAME, "button")
    button_submit.click()
    
finally:
    time.sleep(10)
    
    browser.quit()