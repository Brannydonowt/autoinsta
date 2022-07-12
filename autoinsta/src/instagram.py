from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from mail import Email
import utils
import driver

class LandingPage:
    def __init__(self, browser):
        self.browser = browser

    def save_login_information(self):
        # TODO - Update to By.CSS_SELECTOR
        return utils.try_click_element(self.browser, By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")

    def turn_on_notifications(self):
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, "button._a9--:nth-child(2)")

    def upload_page(self):
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, '._acub > button:nth-child(1)')

    def upload_from_computer(self):
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, '._ab9x > button:nth-child(1)')

    def upload_from_computer_cp(self, video_path): 
        utils.clean_log("Trying to send keys")
        # This is still temperamental, sometimes visibile - sometimes not.
        # xpath is - "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/form/input"
        # css selector is - ._ac2t > form:nth-child(2) > input:nth-child(1)
        # css path is - html._9dls.js-focus-visible._aa4c body._a3wf.system-fonts--body.segoe div#mount_0_0_TM div div div.rq0escxv.l9j0dhe7.du4w35lb div div div.hwddc3l5 div.rq0escxv.l9j0dhe7.du4w35lb div.j83agx80.cbu4d94t.h3gjbzrl.l9j0dhe7.dza99gun div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p div.gs1a9yip.rq0escxv.j83agx80.cbu4d94t.buofh1pr.taijpn5t div.ll8tlv6m.rq0escxv.j83agx80.taijpn5t.tgvbjcpo.hpfvmrgz.hzruof5a div.du4w35lb.cjfnh4rs.lzcic4wl.ni8dbmo4.stjgntxs.oqq733wu.futnfnd5.mudwbb97.fg7vo5n6.q0p5rdf8.li38xygf div.ryzhgsaw.q0p5rdf8.nxkddm9p.d6zs4f6z.dopw56fx.lcf4bpt0.kbli7zfr.fg7vo5n6.mpyj2j6a.d2uofw50.h1gfnr7q.mgim66vq div.qg4pu3sx.flebnqrf.kzt5xp73.h98he7qt.e793r6ar.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav div._a3gq._ab-1 div div._ab8w._ab94._ab99._ab9f._ab9m._ab9o._ab9s div._ac2r div._ac2t form input._ac69
        if self.select_upload_file():
            print("Clicked upload button")

        result, element = utils.try_find_element(self.browser, By.CSS_SELECTOR, "._ac2t > form:nth-child(2) > input:nth-child(1)")
        if result == True:
            element.send_keys(os.path.abspath(video_path))
            sleep(3)
        
        return result

    def select_upload_file(self):
        sleep(3)

        if utils.try_click_element(self.browser, By.CSS_SELECTOR, '._ab9x > button:nth-child(1)'):
            return True
        else:
            return False
        sleep(3)

        autoit.control_send("File Upload","Edit1", os.path.abspath(video_path))
        autoit.control_send("File Upload","Edit1","{ENTER}")
        sleep(2)
        if autoit.win_exists("File Upload"):
            return False
        else:
            return True
        

class UploadPage:
    def __init__(self, browser):
        self.browser = browser

    def nextpage(self):
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, "._abaa > button:nth-child(1)")

    def write_caption(self, caption):
        return utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, 'textarea._ablz:nth-child(1)', caption)

    def verify_upload(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "h2._aacl")
            return True
        except:
            return False
        
class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        usr = utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, "input[name='username']", username)
        if not usr:
            utils.error_log("Failed to send text to username field")
            return False
        
        pwd = utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, "input[name='password']", password)

        if not pwd:
            utils.error_log("Failed to send text to password field")
            return False

        return utils.try_click_element(self.browser, By.XPATH, "//button[@type='submit']")

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def accept_cookies(self):
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)')

    def go_to_login_page(self):
        sleep(2)
        return LoginPage(self.browser)

    def go_to_new_account_page(self):
        utils.clean_log("Trying to move to sign up page.")
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, '.izU2O > a:nth-child(1)')

class CreateAccountPage:
    def __init__(self, browser, p):
        self.browser = browser

        ebrowser = driver.GetBrowser(HEADLESS=True)
        self.mail = Email(ebrowser)

        email = self.mail.get_email()
        
        self.set_email_address(email)
        self.set_fullname("Micheal Watts")
        self.set_username(p.username)
        self.set_password(p.create_account_password())

        self.submit_user_details()
        
    def set_email_address(self, email):
        utils.clean_log("Setting Email Address")
        utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, "div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)", email)
    
    def set_fullname(self, fullname):
        utils.clean_log("Setting Fullname")
        utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, "div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)", fullname)

    def set_username(self, username):
        utils.clean_log("Setting Username")
        utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, "div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)", username)

    def set_password(self, password):
        utils.clean_log("Setting Password")
        utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, "div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)", password)

    def set_birth_date(self):
        res1, month = utils.try_find_element(self.browser, By.CSS_SELECTOR, 'span.O15Fw:nth-child(1) > select:nth-child(2)')
        if not res1:
            utils.error_log("Failed to find month select element")
            return False
        
        res2, day = utils.try_find_element(self.browser, By.CSS_SELECTOR, 'span.O15Fw:nth-child(2) > select:nth-child(2)')
        if not res2:
            utils.error_log("Failed to find day select element")
            return False

        res3, year = utils.try_find_element(self.browser, By.CSS_SELECTOR, 'span.O15Fw:nth-child(3) > select:nth-child(2)')
        if not res3:
            utils.error_log("Failed to find year select element")
            return False

        # select by value
        Month = Select(month)
        Month.select_by_value('8')
        Day = Select(day)
        Day.select_by_value('12')
        Year = Select(year)
        Year.select_by_value('1986')

        sleep(3)

        self.submit_birth_details()

    def submit_user_details(self):
        utils.clean_log("Submitting account details")
        if utils.try_click_element(self.browser, By.CSS_SELECTOR, 'div.bkEs3:nth-child(1) > button:nth-child(1)'):
            utils.clean_log("Details submitted succesfully")
            sleep(5)
            self.set_birth_date()

    def submit_birth_details(self):
        utils.clean_log("Submitting Birthdate Details")
        if utils.try_click_element(self.browser, By.CSS_SELECTOR, '.L3NKy'):
            utils.clean_log("Birthdate submitted succesfully")
            verif = self.mail.get_verification_code()
            self.enter_verification_code(verif)
            # Do something about verifying email

    def enter_verification_code(self, code):
        utils.clean_log("Entering email verification")
        if utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, '.j_2Hd', code):
            utils.clean_log("Email Submitted Succesfully")
            if utils.try_click_element(self.browser, By.CSS_SELECTOR, '.L3NKy'):
                utils.clean_log("Clicked next step succesfully")
                sleep(100)
                

class ExplorePage:
    def __init__(self, browser, hashtag):
        self.browser = browser
        self.browser.get('https://www.instagram.com/explore/tags/' + hashtag)

    def get_recent_post_id(self):
        utils.clean_log("Getting recent post")

    def get_recent_posts(self, num):
        #    ._aao7 > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)
        #    ._aao7 > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)
        #    ._aao7 > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)
        #   ._aao7 > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)
        recent = self.browser.find_element(By.CSS_SELECTOR, 'h2._aanc:nth-child(2)')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", recent)
        sleep(5)

        ids = list()
        row = 0
        for x in range(num):
            column = x % 3
            if column == 0:
                row += 1

            print("x =", x, " row =", row, "column = ", column)
            elem = self.browser.find_element(By.CSS_SELECTOR, f'._aao7 > div:nth-child(3) > div:nth-child(1) > div:nth-child({row}) > div:nth-child({column + 1})')
            a = elem.find_elements(By.TAG_NAME, 'a')       
            for l in a:
                url = l.get_attribute("href")
                id = utils.get_part_from_url(url, 2)
                print("1", utils.get_part_from_url(url, 1))
                print("2", utils.get_part_from_url(url, 2))
                utils.clean_log("id: " + id)
                ids.append(id)
        
        return ids

class Post:
    def __init__(self, browser, id):
        self.browser = browser
        self.id = id
        utils.clean_log("Loading Post: " + id)
        self.browser.get('https://www.instagram.com/p/' + id + '/')

    def like_post(self):
        utils.clean_log("Liking current post")
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, '._aamw > button:nth-child(1)')

    def comment_post(self, comment):
        utils.clean_log("Commenting on post")
        result = utils.try_sendtext_element(self.browser, By.CSS_SELECTOR, '._ablz', comment)
        if not result:
            return False

        sleep(3)
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, 'button._acan:nth-child(3)')

    def follow_poster(self):
        utils.clean_log("Following Poster")
        return utils.try_click_element(self.browser, By.CSS_SELECTOR, 'button._acan:nth-child(2)')

def sign_in_to_account(browser, profile):
    home_page = HomePage(browser)
    login_page = LoginPage(home_page.browser)

    if profile.get_login_details() == 'MAKE_ACCOUNT':
        utils.clean_log("New account is being created.")
        if home_page.accept_cookies():
            utils.clean_log("STEP - Accept Cookies, complete")
            if home_page.go_to_new_account_page():
                acc = CreateAccountPage(browser, profile)
                browser.close()
                sign_in_to_account(browser, profile)
                return True
    else:
        usr, pwd = profile.get_login_details()
        if home_page.accept_cookies():
            utils.clean_log("STEP - Accept Cookies, complete")
            if login_page.login(usr, pwd):
                utils.clean_log("STEP - Login, Complete")
                landing_page = LandingPage(login_page.browser)
                if landing_page.save_login_information():
                    utils.clean_log("STEP - Save Login Information, complete")
                    if landing_page.turn_on_notifications():
                        utils.clean_log("STEP - Notification Settings, complete")
                        return True
    
    print("Failed to navigate to home page.")
    return False

def navigate_to_explore(profile, browser, hashtag):
    if sign_in_to_account(browser, profile):
        sleep(3)
        
        explore = ExplorePage(browser, hashtag)
        sleep(5)
        return True, explore
    else:
        return False

def load_post(browser, post_id):
    post = Post(browser, post_id)
    utils.clean_log("Loaded Post")
    return post

def upload_video(browser, video_path):
    landing_page = LandingPage(browser)
    if landing_page.upload_page():
        utils.clean_log("STEP - Upload Page, complete")
        if landing_page.upload_from_computer_cp(video_path):
            utils.clean_log("STEP - Select Upload, complete")
            return True
    
    return False

def finalise_upload(browser, tik_tok, profile):
    result = True

    my_hashtags = profile.get_hashtag_string()
    
    upload_page = UploadPage(browser)
    if upload_page.nextpage():
        utils.clean_log("UPLOAD 1/4, Complete")
        if upload_page.nextpage():
            utils.clean_log("UPLOAD 2/4, Complete")
            if upload_page.write_caption(tik_tok.desc + "\nCredit: " + tik_tok.video_author + "\n\n\n\n " + tik_tok.hashtag_string + "\n" + my_hashtags):
                utils.clean_log("UPLOAD 3/4, Complete")
                if upload_page.nextpage():
                    utils.clean_log("UPLOAD 4/4, Complete")
                    upload_complete = False
                    while not upload_complete:
                        utils.clean_log("UPLOADING...")
                        sleep(30)
                        upload_complete = upload_page.verify_upload()
                    utils.clean_log("UPLOAD COMPLETE")
                    return True
    
    return False
