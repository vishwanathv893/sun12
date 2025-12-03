'''
Created on 02-Dec-2025

@author: vishw
'''
print("Demonstrating 'text entering action' in nested frames:")

from selenium import webdriver 
from selenium.webdriver.common.by import By # "By" class defines locator strategies to find elements on a web page
import time

options =webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver= webdriver.Chrome(options)

driver.get("https://demo.automationtesting.in/Frames.html")

iframe_tab_two = driver.find_element(By.XPATH, "//a[@href='#Multiple']")#finding the 2nd type of frame (nested frames) with relative XPATH using "a" tag
iframe_tab_two.click()#clicking on it
time.sleep(2)#wait for 2 seconds after clicking on the frames tab

outer_nested_iframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")#finding the outer frame with relative xpath using "iframe" tag
driver.switch_to.frame(outer_nested_iframe)#switching to it 


inner_iframe_demo = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")#finding the inner frame with the relative xpath using "iframe" tag
driver.switch_to.frame(inner_iframe_demo)#switching to it 


input_txt_box = driver.find_element(By.TAG_NAME, "input")#finding the text box inside the inner frame
input_txt_box.send_keys("ALL IS WELL")#doing action inside the box i.e. entering the text


time.sleep(5)#wait for 5 seconds before exit
driver.quit()#exiting the automated Chrome browser


