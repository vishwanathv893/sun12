'''
Created on 06-Dec-2025

@author: vishw
'''

print("Demonstrating the Automated file upload action")

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

multiple_file =driver.find_element(By.ID,"multipleFilesInput")
multiple_file.send_keys("C:/Users/vishw/OneDrive/Desktop/software Testing/5W1H.jpg")#replacing '\' with '/' in path
multiple_file.send_keys(r"C:\Users\vishw\OneDrive\Desktop\software Testing\5W2H.jpg")#by deafult escape character \U is interpreted so insert "r" before the the string of path
multiple_file.send_keys("C:\\Users\\vishw\\OneDrive\\Desktop\\software Testing\\Defect life cycle.jpg") #replacing '\' with '\\'


upload_mfile_btn =driver.find_element(By.XPATH,'//button[text()="Upload Multiple Files"]')
upload_mfile_btn.click()

confirmation_line =driver.find_element(By.ID, 'multipleFilesStatus')
print(confirmation_line.text)
