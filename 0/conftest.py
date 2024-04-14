import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

def pytest_addoption(parser):    
    parser.addoption('--language', 
                     action='store', 
                     default=None, 
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = str(request.config.getoption("language")).lower()
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    
    print(f"\nStart browser for test")
    
    yield browser
    
    print("\nQuit browser")
    
    browser.quit()
    