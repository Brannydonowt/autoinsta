from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import utils
import pyperclip

#https://temp-mail.org/en/

class Email:
    def __init__(self, browser):
        utils.clean_log('Initializing Email Retriever')
        self.browser = browser
        self.browser.get('https://temp-mail.org/en/')
        # sleep for a while, as the site has a fake delay for displaying emails
        sleep(10)

    def get_email(self):
        utils.clean_log('Getting Email Address')

        if utils.try_click_element(self.browser, By.CSS_SELECTOR, 'button.btn-rds:nth-child(1)'):
            utils.clean_log("copied email to clipboard")
            sleep(3)
            return pyperclip.paste()

def get_email_address(browser):
    e = Email(browser)
    return e.get_email()




