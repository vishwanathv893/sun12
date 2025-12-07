'''
Created on 06-Dec-2025

@author: vishw
'''
from selenium.webdriver.common.keys import Keys


print("Demonstrating the keyboard actions")

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com")#loading the url
actions = ActionChains(driver)#defining the 'actions' object from ActionChains class

field1 =driver.find_element(By.ID, "field1") #finding the element
actions.key_down(Keys.CONTROL,field1).send_keys("a").key_up(Keys.CONTROL).perform() #selecting the content from filed1 i.e "Ctrl A"
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()#selecting the content from filed1 i.e "Ctrl C"

field2 =driver.find_element(By.ID, "field2")#finding the element
actions.key_down(Keys.CONTROL,field2).send_keys("v").key_up(Keys.CONTROL).perform() #selecting the content from filed1 i.e "Ctrl V"






