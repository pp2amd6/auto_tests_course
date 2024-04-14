import os
import time
import uuid

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    uuid_str = str(uuid.uuid1())
    
    field_first_name = browser.find_element(By.NAME, "firstname")
    field_first_name.send_keys(uuid_str)
    
    field_last_name = browser.find_element(By.NAME, "lastname")
    field_last_name.send_keys(uuid_str)
    
    field_email = browser.find_element(By.NAME, "email")
    field_email.send_keys(uuid_str)
    
    field_file = browser.find_element(By.NAME, "file")
    field_file.send_keys(os.path.abspath(os.path.dirname(__file__)) + "\\file.txt")
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
