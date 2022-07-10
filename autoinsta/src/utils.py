import os
import json
import random
import string
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath

def generate_password(length):
    # get random password pf length 8 with letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_part_from_url(url, part):
    return PurePosixPath(
        unquote(
            urlparse(
                url
            ).path
        )
    ).parts[part]


def abs_path(local_path):
    return os.path.abspath(local_path)

def get_account_details():
    f = open('autoinsta/profiles/instagram.pass')
    details = f.readlines()
    return details[0], details[1]

def clean_log(message):
    print("*****", message, "*****")

def error_log(message):
    print("***** ERROR", message, "*****")

def get_json_value(j, key):
    valid = json.dumps(j)
    data = json.loads(valid)
    return data[key]

def try_find_element(browser, bySelector, path):
    sleep(5)
    try:
        target_element = browser.find_element(bySelector, path)
        return True, target_element
    except:
        error_log(f"Failed to find element: {path}")
        return False, None

def try_click_element(browser, bySelector, path):
    result, element = try_find_element(browser, bySelector, path)
    if result == True:
        element.click()
    
    return result

def try_sendtext_element(browser, bySelector, path, text):
    result, target = try_find_element(browser, By.CSS_SELECTOR, "textarea._ablz:nth-child(1)")
    if result:
        target.send_keys(text)
    return result