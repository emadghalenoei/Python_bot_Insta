# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:38:07 2021

@author: emadg
"""

import numpy as np
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
import time
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
############################################################
# you can not close the firefox during the run
# you must follow the page of photo first
############################################################
# username = "username"
# password = "password"
# photolink = 'insert link'
# Number_Follow = 200 # Please do not exceed than 300, otherwise IG blocks you!
############################################################
username = "username"
password = "password"
photolink = 'inser link here'
Number_Follow = 150 # Please do not exceed than 300, otherwise IG blocks you!
############################################################

browser = webdriver.Firefox(executable_path=r"C:\...\InstaPy\assets\geckodriver.exe")
             
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(10)


username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
sleep(10)
login_button.click()

wait = WebDriverWait(browser, 20)
sleep(10)
notNowButton = wait.until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')).click()
sleep(10)
browser.get(photolink)
sleep(10)

try:
    FollowButton = wait.until(lambda d: d.find_element_by_xpath('//button[text()="Follow"]'))
    FollowButton.click()

except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as exception:
    pass


shortlink = urlparse(photolink)
url = shortlink[2] + "liked_by/"
sleep(10)
like_link = browser.find_element_by_xpath('//a[@href="'+url+'"]').click()
sleep(20)


t_start = time.time()
for iuser in np.arange(1,Number_Follow+1):
    #FollowButton = wait.until(lambda d: d.find_element_by_xpath('//button[text()="Follow"]'))
    #FollowButton.click()
    try:
        FollowButton = wait.until(lambda d: d.find_element_by_xpath('//button[text()="Follow"]'))
        FollowButton.click()

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as exception:
        try:
            CancelButton = wait.until(lambda d: d.find_element_by_xpath('//button[text()="Cancel"]'))
            CancelButton.click()
        except:     
            pass


    sleep(55+np.random.randint(5, 20))
    t_stop = time.time()
    print("Following: ", iuser, " of ", Number_Follow, ". Time: ", (t_stop-t_start)/60, " min")
   
    
print("The End")
