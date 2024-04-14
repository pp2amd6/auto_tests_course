import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)
    
    field_result = browser.find_element(By.ID, "answer")
    field_result.send_keys(result)
    
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()
    
    radiobutton_robot = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_robot)
    radiobutton_robot.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()