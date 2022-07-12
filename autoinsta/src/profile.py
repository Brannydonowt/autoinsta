# Responsible for creating/managing profiles and what they can post/target

import json
from random import randint
import utils
import os

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
        f = f'autoinsta/profiles/{self.username}/login.pass'
        if os.path.isdir(f'autoinsta/profiles/{self.username}'):
            utils.clean_log("user already has information stored.")
            if utils.get_account_details(f) == False:
                utils.clean_log("User exists, but account has not been created.")
                return 'MAKE_ACCOUNT'
            else:
                return utils.get_account_details(f)
        else:
            utils.clean_log("no user information stored for this user")
            return 'MAKE_ACCOUNT'

    def get_account_password(self):
        path = f'autoinsta/profiles/{self.username}/login.pass'
        try:
            return utils.get_account_details(path)
        except:
            return False

    def create_account_password(self):
        password = utils.generate_password(12)
        self.save_login_details(password)
        return password

    def save_login_details(self, password):
        root = f'autoinsta/profiles/{self.username}/'
        if not os.path.exists(root):
            os.makedirs(root)

        f = open(root + 'login.pass', "w+")
        f.write(f'{self.username}\n')
        f.write(f'{password}')
        f.close()

    def get_hashtag_string(self):
        res = ""
        for h in self.tags:
            res += '#' + h + ' '
        return res

    def get_random_comment(self):
        i = randint(0, len(self.comments))
        return self.comments[i]


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

    

    

    