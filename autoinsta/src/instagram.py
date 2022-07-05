from time import sleep
from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import utils

def try_find_element(browser, bySelector, path):
    sleep(5)
    try:
        target_element = browser.find_element(bySelector, path)
        return True, target_element
    except:
        print("Failed to find element: ", path)
        return False, None

def try_click_element(browser, bySelector, path):
    result, element = try_find_element(browser, bySelector, path)
    if result == True:
        element.click()
    
    return result

class LandingPage:
    def __init__(self, browser):
        self.browser = browser

    def save_login_information(self):
        return try_click_element(self.browser, By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")

    def turn_on_notifications(self):
        return try_click_element(self.browser, By.CSS_SELECTOR, "button._a9--:nth-child(2)")

    def upload_page(self):
        return try_click_element(self.browser, By.CSS_SELECTOR, '._acub > button:nth-child(1)')

    def upload_from_computer(self):
        return try_click_element(self.browser, By.CSS_SELECTOR, '._ab9x > button:nth-child(1)')

    def upload_from_computer_cp(self, video_path): 
        utils.clean_log("Trying to send keys")
        result, element = try_find_element(self.browser, By.CSS_SELECTOR, "._ac2t > form:nth-child(2) > input:nth-child(1)")
        if result == True:
            element.send_keys(os.path.abspath(video_path))
            sleep(3)
            element.click()
        
        return result

    def select_upload_file(self, video_path):
        sleep(3)
        return True

        sleep(3)

        autoit.control_send("File Upload","Edit1", os.path.abspath(video_path))
        autoit.control_send("File Upload","Edit1","{ENTER}")
        sleep(2)
        if autoit.win_exists("File Upload"):
            return False
        else:
            return True
        

class UploadPage:
    def __init__(self, browser):
        self.browser = browser

    def nextpage(self):
        return try_click_element(self.browser, By.CSS_SELECTOR, "._abaa > button:nth-child(1)")

    def write_caption(self, caption):
        result, target = try_find_element(self.browser, By.CSS_SELECTOR, "textarea._ablz:nth-child(1)")
        if result:
            target.send_keys(caption)
        return result

    def verify_upload(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "h2._aacl")
            return True
        except:
            return False
        

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        result1, username_input = try_find_element(self.browser, By.CSS_SELECTOR, "input[name='username']")
        if not result1:
            return False

        result2, password_input = try_find_element(self.browser, By.CSS_SELECTOR, "input[name='password']")
        if not result2:
            return False

        username_input.send_keys(username)
        password_input.send_keys(password)
        return try_click_element(self.browser, By.XPATH, "//button[@type='submit']")

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def accept_cookies(self):
        return try_click_element(self.browser, By.CLASS_NAME, 'HoLwm')

    def go_to_login_page(self):
        sleep(2)
        return LoginPage(self.browser)

def navigate_to_homepage(browser):
    home_page = HomePage(browser)
    login_page = LoginPage(home_page.browser)
    usr, pwd = utils.get_account_details()
    if home_page.accept_cookies():
        utils.clean_log("STEP - Accept Cookies, complete")
        if login_page.login(usr, pwd):
            utils.clean_log("STEP - Login, Complete")
            landing_page = LandingPage(login_page.browser)
            if landing_page.save_login_information():
                utils.clean_log("STEP - Save Login Information, complete")
                if landing_page.turn_on_notifications():
                    utils.clean_log("STEP - Notification Settings, complete")
                    return True
    
    print("Failed to navigate to home page.")
    return False

def upload_video(browser, video_path):

    landing_page = LandingPage(browser)
    if landing_page.upload_page():
        utils.clean_log("STEP - Upload Page, complete")
        if landing_page.upload_from_computer_cp(video_path):
            utils.clean_log("STEP - Select Upload, complete")
            if landing_page.select_upload_file(video_path):
                utils.clean_log("STEP - Upload File, complete")
                return True
    
    return False

def finalise_upload(browser, tik_tok):
    result = True

    my_hashtags = "#funny #meme #follow #f4f #like #l4l #tiktok #trend #trendy #food #hungry #followers #follow4follow #trending #laugh #wholesome #cute #doggo #morning"
    
    upload_page = UploadPage(browser)
    if upload_page.nextpage():
        utils.clean_log("UPLOAD 1/4, Complete")
        if upload_page.nextpage():
            utils.clean_log("UPLOAD 2/4, Complete")
            if upload_page.write_caption(tik_tok.desc + "\nCredit: " + tik_tok.video_author + "\n\n\n\n " + tik_tok.hashtag_string + "\n" + my_hashtags):
                utils.clean_log("UPLOAD 3/4, Complete")
                if upload_page.nextpage():
                    utils.clean_log("UPLOAD 4/4, Complete")
                    upload_complete = False
                    while not upload_complete:
                        utils.clean_log("UPLOADING...")
                        sleep(30)
                        upload_complete = upload_page.verify_upload()
                    utils.clean_log("UPLOAD COMPLETE")
                    return True
    
    return False