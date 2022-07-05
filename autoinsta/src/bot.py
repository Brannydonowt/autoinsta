from time import sleep

import instagram
import tiktok
import driver

def Main():
    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        print("No video path was returned")
        Main()
        return False

    browser = driver.GetBrowser(headless=False)

    sleep(3)

    if instagram.navigate_to_homepage(browser):
        if instagram.upload_video(browser, video_path):
            if instagram.finalise_upload(browser, tik_tok):
                print("**** Video Uploaded Succesfully ****")
                browser.close()
                return True
    
    browser.close()

Main()