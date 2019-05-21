#!/usr/bin/python

import sys
sys.path.append('./')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = webdriver.ChromeOptions()
<<<<<<< HEAD
# Comment out the below line if you want to see the browser window!
=======
# Comment out the below line to view the browser window as the script is working. Notice which extension is being downloaded (that's the 3.41.0_0 folder)
>>>>>>> 43c40f93c948ce2ac87869e0d5bb480121ab2ed9
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
path_to_extension = './3.41.0_0'
chrome_options.add_argument('load-extension=' + path_to_extension)
# chrome_options.binary_location = './google-chrome'

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = './chromedriver')

print('')
print('')

<<<<<<< HEAD
# You can change this to 'hour', 'day', 'month', 'year'
=======
# timeframe can be 'hour', 'day', 'month', 'year'
>>>>>>> 43c40f93c948ce2ac87869e0d5bb480121ab2ed9
timeframe = 'month'

driver.get('https://www.reddit.com/top?t=' + timeframe)

time.sleep(1)

info = driver.find_element_by_class_name('scrollerItem')

getlinks = info.find_elements_by_css_selector('a') 

text_subreddit = getlinks[1].get_attribute('innerHTML')
text_user = getlinks[2].get_attribute('innerHTML')

print('User ' + text_user + ' posted the top post of the ' + timeframe + ' in subreddit ' + text_subreddit)

time.sleep(1)

driver.quit()
