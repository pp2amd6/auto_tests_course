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
    
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    
    print("value of people radio: ", people_checked)
    
    assert people_checked is not None, "People radio is not selected by default"
finally:
    time.sleep(10)
    
    browser.quit()