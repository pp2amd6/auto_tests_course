import time
import calc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    book = browser.find_element(By.ID, "book")
    book.click()
    
    x = browser.find_element(By.ID, "input_value").text
    result = calc.calc(x)
    
    field_result = browser.find_element(By.ID, "answer")
    field_result.send_keys(result)
    
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
