import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def pytest_addoption(parser):
    parser.addoption('--browser_name', 
                     action='store', 
                     default=None, 
                     help="Choose browser: chrome or firefox")
    
    parser.addoption('--user_language', 
                     action='store', 
                     default=None, 
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):    
    browser_name = str(request.config.getoption("browser_name")).lower()
    user_language = str(request.config.getoption("user_language")).lower()
    
    browser = None
    
    if browser_name == "chrome":
        options = Options()
        # options.add_argument("--headless=new")
        options.add_argument("--ignore-certificate-errors")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=firefox_profile)
    else:
        raise pytest.UsageError("--browser_name should be defined")
    
    print(f"\nStart {browser_name} browser for test")
    
    yield browser
    
    print("\nQuit browser")
    
    browser.quit()
    