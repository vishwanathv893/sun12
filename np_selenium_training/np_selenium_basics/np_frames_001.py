'''
Created on 01-Dec-2025

@author: vishw
'''
from selenium import webdriver #Imports Selenium’s webdriver module
from selenium.webdriver.common.by import By
import time

options =webdriver.ChromeOptions()#the ChromeOptions() class provides add settings or custom behavior to Chrome before launching it.
options.add_experimental_option("detach", True)#"detach" True, tells Chrome NOT to close automatically when script finishes running.
options.add_argument("start-maximized")#"start-maximized" tells Chrome to open in maximized window mode
driver= webdriver.Chrome(options)


driver.get("https://demo.automationtesting.in/Frames.html")

driver.switch_to.frame("SingleFrame")


input_txt_bx = driver.find_element(By.TAG_NAME,"input")
input_txt_bx.send_keys("vishwa")