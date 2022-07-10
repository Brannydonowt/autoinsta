# Responsible for creating/managing profiles and what they can post/target

import json
from autoinsta.src.utils import get_account_details
import utils
from os import path

class Profile():
    def __init__(self, j):
        self.j = j
        self.parse_profile()
        
    def parse_profile(self):
        self.username = self.j['username']
        self.bio = self.j['bio']
        self.topic = self.j['topic']
        self.tags = self.j['tags']
        self.comments = self.j['comments']
        print("Profile:", self.username, "parsed succesfully")

    def get_login_details(self):
        utils.clean_log(f"Retrieving login information for account: {self.username}")
        if path.isdir(f'autoinsta/profiles/{self.username}'):
            utils.clean_log("user already has information stored.")
            if get_account_details() == False:
                utils.clean_log("User exists, but account has not been created.")
                self.create_account_password()
                return 'MAKE_ACCOUNT'
                # Make account()
            else:
                return get_account_details()

    def get_account_password(self):
        path = f'autoinsta/profiles/{self.username}/login.pass'
        try:
            return utils.get_account_details(path)
        except:
            return False

    def create_account_password(self):
        password = utils.generate_password(12)
        self.save_login_details(password)

    def save_login_details(self, password):
        f = open(f'autoinsta/profiles/{self.username}/login.pass', "w")
        f.write(f'{self.username}\n')
        f.write(f'{password}')
        f.close()


class ProfileManager():
    def __init__(self):
         self.profiles = list()

    def parse_json(self):
        filepath = 'autoinsta/profiles/map.json'
        with open(filepath) as f:
                data = json.load(f)

        for profile in data:
            prof = Profile(profile)
            self.profiles.append(prof)

mgr = ProfileManager()

mgr.parse_json()

    

    

    