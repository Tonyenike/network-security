#!/usr/bin/python

import sys
sys.path.append('./')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = webdriver.ChromeOptions()
# Comment out the below line if you want to see the browser window!
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
path_to_extension = './3.41.0_0'
chrome_options.add_argument('load-extension=' + path_to_extension)
# chrome_options.binary_location = './google-chrome'

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = './chromedriver')

print('')
print('')

driver.get('http://localhost:3007/users/sign_in')

time.sleep(1)

email_input = driver.find_element_by_id('user_email')
email_input.send_keys("bot@gmail.com")

password_input = driver.find_element_by_id('user_password')
password_input.send_keys("password")

login_button = driver.find_element_by_name('commit')

time.sleep(1)

driver.get('http://localhost:3007/links/new')


driver.quit()
