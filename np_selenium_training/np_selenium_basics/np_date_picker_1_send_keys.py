'''
Created on 11-Dec-2025

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

print("Enter the text in date picker 1 using send keys.")

dp1=driver.find_element(By.ID,"datepicker")
dp1.send_keys("12/10/2025")

dp2=driver.find_element(By.NAME,"SelectedDate")
dp2.send_keys("10/12/2025")