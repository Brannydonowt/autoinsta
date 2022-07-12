import schedule
import time

import bot
import utils
from profile import ProfileManager

def job():
    p_mgr = ProfileManager()
    p_mgr.parse_json()
    for p in p_mgr.profiles:
        utils.clean_log(f"Running Bot for Profile: {p.username}")
        utils.clean_log(f"Liking relevant posts with Profile: {p.username}")
        bot.Like_Relevant_Posts(p, 10, HEADLESS=False)
        utils.clean_log(f"Posting Trending Tiktok with Profile: {p.username}")
        bot.Upload_Trending_TikTok(p, VIDEO_EDIT=False, HEADLESS=False)
        utils.clean_log(f"Finished Running Bot for Profile: {p.username}")
    print("bot finished running!")

print("--- STARTING BOT ---")
job()
schedule.every(5).minutes.do(job)
schedule.every().hour.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
