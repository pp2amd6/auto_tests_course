from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

try: 
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    field_first_name = browser.find_element(By.CSS_SELECTOR,"div.first_block div.first_class input")
    field_first_name.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))
    
    field_last_name = browser.find_element(By.CSS_SELECTOR,"div.first_block div.second_class input")
    field_last_name.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))
    
    field_email = browser.find_element(By.CSS_SELECTOR,"div.first_block div.third_class input")
    field_email.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
