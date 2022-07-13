# autoinsta
## An Automated Instagram Page Manager
### Post Trending Tiktoks, Interact with relevant hashtags, Follow relevant pages and grow your instagram automatically.

This is an in-development automated social media tool, built on Selenium, that I am developing for fun.

I am currently also using the TikTokAPI for video retrieval. 

For an example of an instagram account that uses the bot, check out [@trendmeisters](https://www.instagram.com/trendmeisters/?hl=en)

## Recently Added Features
- [X] Account Creation Process

    *You can define any profile that you'd like in "autoinsta/profiles/map.json" and an account will be generated if one doesn't already exist.*
- [X] Better Profile Management

    *Profiles can now be defined in "autoinsta/profiles/map.json" and the bot will behave according to the details provided in there.*
    *Bot will like, comment and follow posts/users with the correct topic (Food, Memes, Funny, etc...)*
    *Bot will place relevant hashtags on posts based on profile information*
- [X] Multiple Profile Support

    *Bot will now cycle through all profiles defined in map.json file*
- [X] ffmpeg auto-padded videos
    
    *Automatically pads any TikTok content to fit the 4:3 Instagram Aspect Ratio* 
- [X] Docker Support
   
   *Added a basic Dockerfile that runs the bot via docker*

## Getting Started

Clone the repo
```
git clone https://github.com/Brannydonowt/autoinsta.git
```
### Running Via Docker
I have dockerized the project so that you can simply create a deployable docker image to run.
```
docker build -t autoinsta .
```
You **MUST** be running in headless mode for Docker to run succesfully.

I'm new to using Docker, so if there are any problems please raise an issue and I'll jump on it!

### Running Locally
install the required pip packages (requirements.txt file included)
```
pip install virtualenv (if you don't already have virtualenv installed)
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

TikTokApi uses the Playwright library. Therefore with a fresh install, you need to ensure that you run
*(due to this, you may have some problems running this bot on linux. I recommend using Docker if running locally doesn't work for you.)*
```
playwright install
```

Make sure you have a valid web driver installed and placed into your PATH for Selenium.
[Follow this link for more information on how to do that](https://pypi.org/project/selenium/)

Look at the `autoinsta/profiles` folder. Inside is a `example.json` file. Duplicate this file and rename it to `map.json`
Open `map.json` and fill out the relevant information for your account profile.

### Using an existing account
Create a folder in `autoinsta/profiles` named after your account username. For example: `autoinsta/profiles/example/`

In this folder create a file called `login.pass`, and write your login details inside as like so:
```
exampleaccount@example.com
examplepassword123
```
path should look like: `autoinsta/profiles/username/login.pass`

*.pass files are in the .gitignore, so will not be picked up when commiting, you can also remove the requirement for this file by manually entering your login details in the instagram.py.*
*To do this, go to instagram.py. Delete line 107 and enter your details in the place of usr and pwd on line 109*

### Creating new accounts
To run the bot and create new accounts automatically, simply define the profile you would like to be created in the `map.json` file. Ensure your username is unique beforehand, as you could run into issues otherwise.

**Important** - The account will be created using a temporary email address. If you intend to use the account for a long period of time - migrate the account to a new email address manually. Login details are stored in a login.pass file.

### Next Steps

`brain.py` contains example code that shows how to carry out the most basic tasks that the bot is capable of.

Use the schedule class to set intervals for how often tasks should be carried out.

You can also adjust and run `brain.py` to schedule posts every x minutes or at certain times throughout the day.
[Follow this link for more information on how to do that](https://pypi.org/project/schedule/)

Feel free to read through the project code and offer up any suggestions, tweaks or improvements. 

This is my first public, intermediate python project, and so any feedback is always appreciated.

### Cookies

[There are some issues that can occur related to the TikTokAPI](https://github.com/davidteather/TikTok-Api/issues/891). Most of these issues can be circumvented by logging into tik tok manually, scrolling through for a short time and then saving all of your cookies to a json file (at cookies/cookies.json)

This can be done using a browser extension [like this one.](https://add0n.com/cookie-editor.html)

#### This is a hobby project, and so further development is not guaranteed, however below are some of the features I'd like to add.







