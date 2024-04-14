from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    field_first_name = browser.find_element(By.CSS_SELECTOR,"div.first_block div.first_class input")
    field_first_name.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))
    
    field_last_name = browser.find_element(By.CSS_SELECTOR,"div.first_block div.second_class input")
    field_last_name.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))
    
    field_email = browser.find_element(By.CSS_SELECTOR,"div.first_block div.third_class input")
    field_email.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()