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

# You can change this to 'hour', 'day', 'month', 'year'

driver.get('http://flip2.engr.oregonstate.edu:3007')

time.sleep(1)

info = driver.find_elements_by_class_name('row')



for i in range(len(info)):

    getlinks = info[i].find_elements_by_css_selector('a') 

    thing =  info[i].find_elements_by_css_selector('small')

    text_link = getlinks[0].get_attribute('innerHTML')
    text_up   = getlinks[2].get_attribute('text')
    text_down = getlinks[3].get_attribute('text')
    text_up = text_up.split('\n')[2]
    text_down = text_down.split('\n')[2]

    text_details = thing[0].get_attribute('innerHTML')

    print("TITLE: " +  text_link)
    print("DETAILS: " + text_details)
    print("UPVOTES: " + text_up)
    print("DOWNVOTES: " + text_down)

    print('')
    print('')

driver.quit()
