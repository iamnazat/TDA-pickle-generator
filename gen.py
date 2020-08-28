from urllib.request import urlopen

import atexit
import datetime
import dateutil
import sys
import tda

API_KEY = "
REDIRECT_URI = 'https://127.0.0.1'
TOKEN_PATH = 'token.pickle'

def make_webdriver():
    # Import selenium here because it's slow to import
    from selenium import webdriver

    driver = webdriver.Chrome()
    atexit.register(lambda: driver.quit())
    return driver

client = tda.auth.easy_client(
    API_KEY,
    REDIRECT_URI,
    TOKEN_PATH,
    make_webdriver)


