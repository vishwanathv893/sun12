'''
Created on 24-Nov-2025

@author: vishw
'''
from selenium import webdriver #Imports Selenium’s webdriver module
from selenium.webdriver.common.by import By
#import time


options =webdriver.ChromeOptions()#the ChromeOptions() class provides add settings or custom behavior to Chrome before launching it.
options.add_experimental_option("detach", True)#"detach" True, tells Chrome NOT to close automatically when script finishes running.
options.add_argument("start-maximized")#"start-maximized" tells Chrome to open in maximized window mode
driver= webdriver.Chrome(options) #Launches the Chrome browser with the options set by above lines of code.driver becomes the object of Chrome() class to control the browser
driver.get("https://testautomationpractice.blogspot.com/")#driver object opens the url using get method.
driver.implicitly_wait(5)

pop_up_windows =driver.find_element(By.ID, "PopUp")#finding the "popup windows" button on the test automation site
pop_up_windows.click()#clicking on it

print("Two pop-up windows opened.")
windows= driver.window_handles#accessing the existing windows using method
driver.switch_to.window(windows[2])#selecting the 2nd pop up window by switching to it using 'window' method
print(windows)


playwrite =driver.find_element(By.CLASS_NAME, "getStarted_Sjon") #finding the 'get started' button in playwright website
playwrite.click()#clicking on it


