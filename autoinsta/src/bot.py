from time import sleep

from browsers import browsers

import instagram
import tiktok
import driver
import video
import utils

def Upload_Trending_TikTok():
    VIDEO_EDIT = False

    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        utils.error_log("No video path was returned")
        Upload_Trending_TikTok()
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

def Test_LoadPost():
    browser = driver.GetBrowser(headless=False)

    if instagram.navigate_to_homepage(browser):
        post = instagram.load_post(browser, 'Cfy_C70LIM6')
        post.like_post()
        post.comment_post('What great content!')

def Like_Relevant_Posts(hashtag, num):

    browser = driver.GetBrowser(headless=False)

    sleep(3)

    result, explore = instagram.navigate_to_explore(browser, hashtag)
    if not result:
        utils.error_log("Failed to navigate to explore page.")

    recent_posts = explore.get_recent_posts(10)
    print(recent_posts)

    sleep(3)

    for x in range(len(recent_posts)):
        p = instagram.load_post(browser, recent_posts[x])
        sleep(5)
        p.like_post()
        p.comment_post('Love this!!')       

def Test_VideoEdit():
    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        utils.error_log("No video path was returned")
        #return False

    video.add_video_pad('autoinsta/videos/tikTokTrending.mp4')

Like_Relevant_Posts('food', 10)