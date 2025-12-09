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

driver.get("https://demo.automationtesting.in/Frames.html")

print("Demonstrating resizable ation")

actions = ActionChains(driver)#defining the 'actions' object from ActionChains class 

interactions_dp_tab = driver.find_element(By.LINK_TEXT,"Interactions")#locating the 'Interactions' tab using link_text 
actions.move_to_element(interactions_dp_tab).perform()#hovering over the tab

resizable_button= driver.find_element(By.LINK_TEXT, "Resizable")#Locating the Resizable option
actions.move_to_element(resizable_button).perform()#hovering over it
resizable_button.click()#clicking on resizable option

re_item =driver.find_element(By.ID,"resizable")
actions.drag_and_drop_by_offset(re_item, 500, 40).perform()





