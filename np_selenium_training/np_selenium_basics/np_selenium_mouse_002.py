'''
Created on 03-Dec-2025

@author: vishw

'''

print("Demonstrating the automation of mouse hover on interactions tab upto 'static' button. ")

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://demo.automationtesting.in/Frames.html")#loading the url
actions = ActionChains(driver)#defining the 'actions' object from ActionChains class 

interactions_dp_tab = driver.find_element(By.LINK_TEXT,"Interactions")#locating the 'Interactions' tab using link_text 
actions.move_to_element(interactions_dp_tab).perform()#hovering over the tab

drag_drop=driver.find_element(By.LINK_TEXT,"Drag and Drop")#locating the  next element to move the mouse point
actions.move_to_element(drag_drop).perform() #hovering over it

static_button= driver.find_element(By.LINK_TEXT, "Static")#Locating the static button
actions.move_to_element(static_button).perform()#hovering over it

time.sleep(5)
driver.quit()



