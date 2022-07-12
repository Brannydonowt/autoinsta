from time import sleep

from browsers import browsers
from profile import ProfileManager

import instagram
import tiktok
import driver
import video
import utils
import mail
import profile

def Upload_Trending_TikTok(user, VIDEO_EDIT=False, HEADLESS=True):
    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        utils.error_log("No video path was returned")
        Upload_Trending_TikTok(user, VIDEO_EDIT, HEADLESS)
        return False

    if VIDEO_EDIT:
        utils.clean_log("Padding Video Content")
        video_path = video.add_video_pad(video_path)

    browser = driver.GetBrowser(HEADLESS=HEADLESS)

    sleep(3)

    if instagram.sign_in_to_account(browser, user):
        if instagram.upload_video(browser, video_path):
            if instagram.finalise_upload(browser, tik_tok, user):
                utils.clean_log("Video Uploaded Succesfully")
                browser.close()
                return True
    
    browser.close()
    return

def Like_Relevant_Posts(user, num, HEADLESS=False):

    browser = driver.GetBrowser(HEADLESS=HEADLESS)

    sleep(3)

    result, explore = instagram.navigate_to_explore(user, browser, user.topic)
    if not result:
        utils.error_log("Failed to navigate to explore page.")

    recent_posts = explore.get_recent_posts(num)
    print(recent_posts)

    sleep(3)

    for x in range(len(recent_posts)):
        p = instagram.load_post(browser, recent_posts[x])
        sleep(5)
        p.like_post()
        p.comment_post(user.get_random_comment())
        p.follow_poster()

    sleep(3)
    browser.close()
    utils.clean_log("Finished liking posts")   
    return True  

def Test_Email():
    browser = driver.GetBrowser(HEADLESS=False)
    mail.get_email_address(browser)


def Test_VideoEdit():
    tik_tok, video_path = tiktok.get_tiktok_video()
    if video_path == False:
        utils.error_log("No video path was returned")
        #return False

    video.add_video_pad('autoinsta/videos/tikTokTrending.mp4')

p_mgr = ProfileManager()
p_mgr.parse_json()
for p in p_mgr.profiles:
    Like_Relevant_Posts(p, 10, HEADLESS=False)
    Upload_Trending_TikTok(p, VIDEO_EDIT=False, HEADLESS=False)