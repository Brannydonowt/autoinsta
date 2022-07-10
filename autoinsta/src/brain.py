import schedule
import time

import bot

def job():
    print("--- Posting to Instagram ---")
    #bot.Upload_Trending_TikTok(VIDEO_EDIT=True, HEADLESS=False)
    time.sleep(3)
    bot.Like_Relevant_Posts("memes", 15)
    print("bot finished running!")

print("--- STARTING BOT ---")
job()
schedule.every(5).minutes.do(job)
schedule.every().hour.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
