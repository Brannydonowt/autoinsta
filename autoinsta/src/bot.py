from time import sleep

import instagram
import tiktok
import driver
import video
import utils

def Main():
    VIDEO_EDIT = True

    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        utils.error_log("No video path was returned")
        Main()
        return False

    if VIDEO_EDIT:
        utils.clean_log("Padding Video Content")
        video_path = video.add_video_pad(video_path, 100, 100)

    browser = driver.GetBrowser(headless=True)

    sleep(3)

    if instagram.navigate_to_homepage(browser):
        if instagram.upload_video(browser, video_path):
            if instagram.finalise_upload(browser, tik_tok):
                utils.clean_log("Video Uploaded Succesfully")
                browser.close()
                return True
    
    browser.close()

def Test_VideoEdit():
    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        utils.error_log("No video path was returned")
        #return False

    video.add_video_pad('autoinsta/videos/tikTokTrending.mp4', 100, 100)

Main()