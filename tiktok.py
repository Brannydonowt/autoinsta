from TikTokApi import TikTokApi
import logging

import json

from random import randint

from time import sleep

# TikTok Section
class TikTokVideoGet:
    def __init__(self):
        self.api = TikTokApi()
        self.cookies = self.get_cookies_from_file()

        self.api._get_cookies = self.get_cookies
        print("initialized tiktok video helper")

    def get_cookies_from_file(self):
        with open('cookies/cookies.json') as f:
            self.cookies = json.load(f)

        cookies_kv = {}
        for cookie in self.cookies:
            cookies_kv[cookie['name']] = cookie['value']

        return cookies_kv

    def get_cookies(self, **kwargs):
        return self.cookies
    
    def get_hashtag_video(self, hashtag):
        desiredVideo = randint(0, 10)
        step = 0
        
        h = self.api.hashtag(name=hashtag)
        print("Made it")

        videos = h.videos(count=10)
        print("Made it to videos")

        for v in videos:
            step += 1

            if (step == desiredVideo):
                video_id = v.id
                self.download_video_by_id(video_id)

                return "videos/tikTokTrending.mp4"

    def get_trending_video(self):
        try: 
            desiredVideo = randint(0, 3)
            step = 0
            print("Desired ID: ", desiredVideo)

            for trending_video in self.api.trending.videos(count=10):
                step += 1
                # Prints the author's username of the trending video.
                if (step == desiredVideo):
                    print("Found a match for our desired video.")
                    video_id = trending_video.id
                    
                    self.video_author = ""
                    self.desc = ""

                    try:
                        video_data = trending_video.info()
                        self.desc = video_data['desc']
                        print (self.desc)

                        self.video_author = trending_video.author.username
                        print("video author: ", self.video_author)
                        self.video_hashtags = trending_video.hashtags
                        self.hashtag_string = ""
                        for h in self.video_hashtags:
                            self.hashtag_string += (" #" + h.name)
                        print("hashtag string:", self.hashtag_string)
                    except:
                        print("Failed to pull video data")

                    print (self.hashtag_string)

                    self.download_video_by_id(video_id)
                
                    return "videos/tikTokTrending.mp4"
            return False
        except:
            print ("Failed to pull from TikTok...")
            return False


    def download_video_by_id(self, video_id):
        with TikTokApi() as api:
            video_bytes = api.video(id=video_id).bytes()

        # Saving The Video
        with open('videos/tikTokTrending.mp4', 'wb') as output:
            output.write(video_bytes)

        sleep(10)

def get_tiktok_video():
    tik_tok = TikTokVideoGet()
    #video_path = tik_tok.get_hashtag_video("food")
    return tik_tok, tik_tok.get_trending_video()