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

print("Taking process name from user input and display the feature of a process by choosing pre-defined options.")

process_name =input("Please enter the process name:")
process_name.casefold()

memory_space =driver.find_element(By.XPATH, "//table[@id='taskTable']/tbody[@id='rows']/tr/td[contains(text() ,'MB') and not( contains(text(),'/s'))]")