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

    def get_verification_code(self):
        utils.clean_log("Getting verification code.")
        utils.clean_log("Sleeping 30 seconds before trying to retrieve")
        sleep(30)

        res, element = utils.try_find_element(self.browser, By.CSS_SELECTOR, '.inbox-dataList > ul:nth-child(1) > li:nth-child(2) > div:nth-child(2) > span:nth-child(1) > a:nth-child(1)')
        if not res:
            utils.error_log("Failed to retrieve verification email")
            return False

        return self.parse_verification_code(element)

    def parse_verification_code(self, elem):
        utils.clean_log("Parsing verification code")
        str = elem.text.split(' ')
        utils.clean_log(f'Parsed Verification code is: {str[0]}')
        return str[0]

def get_email_address(browser):
    e = Email(browser)
    return e.get_email()




