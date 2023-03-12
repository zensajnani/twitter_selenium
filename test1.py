from selenium import webdriver
import pickle
import os.path
import time

# create a new Chrome browser instance
# browser = webdriver.Chrome()
url = "https://www.twitter.com"


# navigate to the website
# browser.get(url)
browser = webdriver.Chrome()
browser.get(url)

# check if the cookies file exists
if os.path.isfile('cookies.pkl'):
    print("COOKIES EXist")
    # if the cookies file exists, load the cookies
    with open('cookies.pkl', 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
    # create a new Chrome browser instance and add the cookies to it
    # browser = webdriver.Chrome()
    # browser.get(url)
    time.sleep(5)
    for cookie in cookies:
        browser.add_cookie(cookie)
    print(cookies)
    browser.get(url)


else:
    print("COOKIES DO NOT EXist")

    # if the cookies file doesn't exist, create a new Chrome browser instance and navigate to the website
    
    # do some stuff to generate cookies...
    # ...
    # get the cookies from the browser
    input("press enter after loggin in")
    cookies = browser.get_cookies()
    # save the cookies to a file
    with open('cookies.pkl', 'wb') as cookiesfile:
        pickle.dump(cookies, cookiesfile)
    print(f"cookies after login: {cookies}")
    

# pause the script and keep the window open
input("Press any key to close the window...")

# close the browser
browser.quit()
