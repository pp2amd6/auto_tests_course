from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_appeared(browser):
    browser.get(link)
    
    assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) != 0, f"Button doesn`t exist"
    