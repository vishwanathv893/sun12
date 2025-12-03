'''
Created on 03-Dec-2025

@author: vishw
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com")

print("Demonstrating the 'double click' action.")
print()

f1= driver.find_element(By.ID, "field1")#locating the element 
f1.clear()#clearing the default text
f1.send_keys("Vishwanath")#entering the new text
time.sleep(2)

actions = ActionChains(driver)#defining the object to perform mouse actions
copy_txt =driver.find_element(By.XPATH, "//button[@ondblclick = 'myFunction1()']")#locating the button
actions.double_click(copy_txt).perform()#performing the double click action
print("Text in field1 is copied to field2.")

time.sleep(3)
driver.quit()
