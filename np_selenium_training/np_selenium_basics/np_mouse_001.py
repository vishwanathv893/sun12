'''
Created on 03-Dec-2025

@author: vishw
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By # "By" class defines locator strategies to find elements on a web page
from selenium.webdriver.common.action_chains import ActionChains #importing 'ActionChains' class to automate mouse related actions
import time

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://demo.automationtesting.in/Frames.html")

actions = ActionChains(driver)

webtable_menu_item = driver.find_element(By.LINK_TEXT, "WebTable") # Locate the element
actions.move_to_element(webtable_menu_item).perform()

time.sleep(5)#wait for 5 seconds before exit
driver.quit()#exiting the automated Chrome browser






