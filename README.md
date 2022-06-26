# autoinsta
## A small Python project that automatically takes trending tik toks and uploads them to instagram.

This is an in-development automated social media tool, built on Selenium that I am developing for fun.

I am currently also using the TikTokAPI for video retrieval. 

For an example of an instagram account that uses the bot, check out [@trendmeisters](https://www.instagram.com/trendmeisters/?hl=en)

## Getting Started
Clone the repo and install the required pip packages (requirements.txt file included)

```
git clone <https://github.com/Brannydonowt/autoinsta.git>
cd <repo>
pip install virtualenv (if you don't already have virtualenv installed)
virtualenv venv to create your new environment (called 'venv' here)
source venv/bin/activate
pip install -r requirements.txt
```

Make sure you have a valid web driver installed and placed into your PATH for Selenium.
[Follow this link for more information on how to do that](https://pypi.org/project/selenium/)

Create a folder at the root called "profiles".
In this folder create a file called "instagram.pass", and write your login details inside as like so:
```
exampleaccount@example.com
examplepassword123
```
path should look like: *autoinsta/profiles/instagram.pass*

*.pass files are in the .gitignore, so will not be picked up when commiting, you can also remove the requirement for this file by manually entering your login details in the instagram.py*
*to do this, go to instagram.py. Delete line 107 and enter your details in the place of usr and pwd on line 109*

You can now compile run bot.py to upload a single trending tiktok video to your instagram page.

You can also adjust and run scheduler.py to schedule posts every x minutes or at certain times throughout the day.
[Follow this link for more information on how to do that](https://pypi.org/project/schedule/)




