from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def GetBrowser(headless=False):
    options = Options()
    options.headless = headless
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(5)
    return browser