from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


def GetBrowser(headless=False):
    options = Options()
    options.headless = headless
    
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    browser.implicitly_wait(5)
    return browser