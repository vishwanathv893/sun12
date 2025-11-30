'''
Created on 23-Nov-2025

@author: vishw
'''
from selenium import webdriver #Imports Selenium’s webdriver module
from selenium.webdriver.common.by import By
import time

options =webdriver.ChromeOptions()#the ChromeOptions() class provides add settings or custom behavior to Chrome before launching it.
options.add_experimental_option("detach", True)#"detach" True, tells Chrome NOT to close automatically when script finishes running.
options.add_argument("start-maximized")#"start-maximized" tells Chrome to open in maximized window mode
driver= webdriver.Chrome(options) #Launches the Chrome browser with the options set by above lines of code.driver becomes the object of Chrome() class to control the browser
driver.get("https://testautomationpractice.blogspot.com/")#driver object opens the url using get method.
driver.implicitly_wait(5)

promt_alert_button=driver.find_element(By.ID,"promptBtn")#finding the promt button
promt_alert_button.click()#click on promt button
time.sleep(2)

driver.switch_to.alert.send_keys("vishwanath")#entering the name in the popup text bo
driver.switch_to.alert.accept()#click on "ok" on pop up button