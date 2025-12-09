'''
Created on 08-Dec-2025

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

network_speed_chrome =driver.find_element(By.XPATH, "//table[@id='taskTable']/tbody[@id='rows']/tr/td[contains(text() ,'Mbps')]")
print(network_speed_chrome.text)


