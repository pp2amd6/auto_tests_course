import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
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
    