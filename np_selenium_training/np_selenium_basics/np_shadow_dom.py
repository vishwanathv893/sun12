'''
Created on 09-Dec-2025

@author: vishw
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com")

shadow_dom_txt_box =driver.find_element(By., value)