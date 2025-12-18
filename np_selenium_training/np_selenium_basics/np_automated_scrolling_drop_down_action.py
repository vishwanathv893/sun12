'''
Created on 15-Dec-2025

@author: vishw
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin 




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5) 

driver.get("https://testautomationpractice.blogspot.com/")

print("Automating the scrolling-drop-down and option-selecting action ")

scroll_drop_down = driver.find_element(By.ID, "comboBox")
scroll_drop_down.click()

actions = ActionChains(driver) #creating a actionschains object

drop_down = driver.find_element(By.XPATH,"//div[text()='Item 95']")
drop_down.click()
#actions.drag_and_drop_by_offset(drop_down, 0, 500).perform()




