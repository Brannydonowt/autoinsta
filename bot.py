from cProfile import run
from codecs import escape_encode
from msilib.schema import File
from selenium import webdriver

from time import sleep

import instagram
import tiktok

def Main():
    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        print("No video path was returned")
        Main()
        return False

    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    sleep(3)

    if instagram.navigate_to_homepage(browser):
        if instagram.upload_video(browser, video_path):
            if instagram.finalise_upload(browser, tik_tok):
                browser.close()
                return True
    
    browser.close()

Main()