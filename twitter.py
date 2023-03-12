from selenium import webdriver
import pickle
import os.path
import time

# create a new Chrome browser instance
browser = webdriver.Chrome()
print(f'SESSION ID: {browser.session_id}')


def load_twitter(url, browser):
    # navigate to the website
    browser.get(url)
    # check if the cookies file exists
    if os.path.isfile('cookies.pkl'):
        print("COOKIES EXist")
        # if the cookies file exists, load the cookies
        with open('cookies.pkl', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
        time.sleep(3)
        for cookie in cookies:
            browser.add_cookie(cookie)
        # print(cookies)
        browser.refresh()
    else:
        print("COOKIES DO NOT EXist")
        # log in manually
        input("press enter after loggin in")
        # get the cookies from the browser
        cookies = browser.get_cookies()
        # save the cookies to a file
        with open('cookies.pkl', 'wb') as cookiesfile:
            pickle.dump(cookies, cookiesfile)
        # print(f"cookies after login: {cookies}")
    print('waiting 3 seconds...')
    time.sleep(3)
        


# function to load another user's profile 
def load_profile(username, browser):
    print("LOAD PROFILE")
    # navigate to the profile
    profile_url = f"https://www.twitter.com/{username}"
    print(profile_url)
    browser.get(profile_url)
    time.sleep(3)


# function to select 1st tweet
def select_tweet(browser):
    # navigate to the first tweet
    # xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[1]/div/div/article[0]'
    # # first_tweet = browser.find_element('xpath', xpath)
    # # print(first_tweet)
    # browser.find_element('xpath', xpath).click()
    time.sleep(3)



# variables
url = "https://www.twitter.com"
username = "elonmusk"


# STEPS
# 1. load twitter and login
# 2. go to another users profile
# 3. select 1st tweet
# 4. click on 1st tweet
# 5. select 1st comment
# 6. "like" 1st comment


load_twitter(url, browser)
load_profile(username, browser)
select_tweet(browser)


# pause the script and keep the window open
input("Press any key to close the window...")

# close the browser
browser.quit()