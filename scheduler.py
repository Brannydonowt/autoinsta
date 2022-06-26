from turtle import pos
import schedule
import time

import bot

def job():
    print("--- Posting to Instagram ---")
    bot.Main()

print("--- STARTING BOT ---")
schedule.every(15).minutes.do(job)
schedule.every().hour.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
