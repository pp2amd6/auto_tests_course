import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CRED_LOGIN = "@gmail.com"
CRED_PASSWORD = ""

@pytest.mark.parametrize('lesson_number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# @pytest.mark.parametrize('lesson_number', ["236895"])
def test_login_to_stepik(browser, lesson_number):
    link = f"https://stepik.org/lesson/{lesson_number}/step/1"
    
    browser.implicitly_wait(10)
    browser.get(link)
    
    login_button = browser.find_element(By.CSS_SELECTOR, f"a[href='/lesson/{lesson_number}/step/1?auth=login']")
    login_button.click()
    
    field_login = browser.find_element(By.ID, "id_login_email")
    field_login.send_keys(CRED_LOGIN)
    
    field_email = browser.find_element(By.ID, "id_login_password")
    field_email.send_keys(CRED_PASSWORD)
    
    button_login = browser.find_element(By.CSS_SELECTOR, "form#login_form > button[type='submit']")
    button_login.click()
    
    field_answer = browser.find_element(By.CSS_SELECTOR, "div.quiz-component > textarea.string-quiz__textarea")
    calc_value = str(math.log(int(time.time()))) 
    field_answer.send_keys(calc_value)
    
    # button_send_selector = "div.attempt__actions > button.submit-submission[type='button']"    
    # button_send = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_send_selector)))
    # button_send.click()
    
    field_correct = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.lesson__hint > p.smart-hints__hint")))
    field_correct = browser.find_element(By.CSS_SELECTOR, "div.lesson__hint > p.smart-hints__hint").text
    assert field_correct == "Correct!", f"Field return next value: {field_correct}"
    
    # time.sleep(20)