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

driver.get('https://week1-raddit.herokuapp.com/')

time.sleep(1)

info = driver.find_elements_by_class_name('row')

for i in range(3):

    getlinks = info[i].find_elements_by_css_selector('a') 

    text_link = getlinks[0].get_attribute('innerHTML')

    print(text_link)

driver.quit()
