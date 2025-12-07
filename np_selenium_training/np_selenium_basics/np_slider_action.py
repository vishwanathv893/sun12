'''
Created on 06-Dec-2025

@author: vishw
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

import time

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com")
print("Demonstrating the Slider action.")
print()

actions = ActionChains(driver) #creating a actionschains object

slider_one = driver.find_element(By.XPATH,"//span[@style='left: 15%;']")#locating the 1st slider
actions.drag_and_drop_by_offset(slider_one, -50, 0).perform()#sliding towards left

slider_two = driver.find_element(By.XPATH,"//span[@style='left: 60%;']")#locating the 2st slider
actions.drag_and_drop_by_offset(slider_two, 100, 0).perform()#sliding towards right
