'''
Created on 07-Dec-2025

@author: vishw
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

import time

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com")
print("printing the elements in static web table in each line on the console:")

book_table =driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]")
print(book_table.text)#printing entire row in a single line
print()
'''
for i in range(1,5):
    i1= driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[2]/td{[i]}")
    print(i1.text)
 '''   
for j in range(2,8):#each row is accessed
    for i in range(1,5):#each item in current row is accessed
        row =driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr{[j]}/td{[i]}")#locating the elements in a table using xpath with string formating
        print(row.text)#printing the elements



    
    
driver.quit()    
    
    
    
