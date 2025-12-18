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

memory_space =driver.find_element(By.XPATH, "//table[@id='taskTable']/tbody[@id='rows']/tr/td[contains(text() ,'MB') and not( contains(text(),'/s'))]")
percentage_cpu_used=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr/td[contains(text(),'%')]")
disk_speed=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr/td[contains(text(),'MB/s')]")
network_speed=driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr/td[contains(text(),'Mbps')]")


