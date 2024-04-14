import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

class TestAbs(unittest.TestCase):
    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        
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
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text incorrect")
        
    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        
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
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text incorrect")
        
if __name__ == "__main__":
    unittest.main()