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

driver.get("https://testautomationpractice.blogspot.com")#loading url on the chrome browser

print("Taking the device name entered by the user and display its price if the device name is present.")
print()

entered_device_name =input("Please enter the device name:")#taking user input
entered_device_name.casefold()#converting it into lower case
print()
'''
page_no =driver.find_element(By.XPATH,"//ul/li/a[text()=3]") 
page_no.click()

divices_on_current_page_in_table =[]

for i in range(1,6):
        device_name =driver.find_element(By.XPATH, f"//table[@id ='productTable']/tbody/tr{[i]}/td[2]")
        divices_on_current_page_in_table.append(device_name.text.casefold())
         
i=0
device_not_present = True
while i<5:
    if entered_device_name == divices_on_current_page_in_table[i] :
        price_of_device = driver.find_element(By.XPATH,f"//table[@id ='productTable']/tbody/tr{[i+1]}/td[3]")
        print(f"The entered device name '{divices_on_current_page_in_table[i]}' is present and its price is '{price_of_device.text}'")
        device_not_present =False
    i+=1    
            
    if device_not_present:
        
        page_no =driver.find_element(By.XPATH,"//ul[@class = 'pagination']/li/a[text()=2]") 
        page_no.click()

'''

device_name_list =[]#creating names list
device_price_list=[]#creating price list



for j in range(1,5):#iterating the page clicking action
    pagination_button = driver.find_element(By.XPATH, f"//ul/li/a[text() = {j}]")#finding the pagination number
    pagination_button.click()#clicking on it
    
    for i in range(1,6):#iterating name and price fetching action
        device_name =driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[i]}/td[2]")#locating the device name in each row
        device_name_list.append(device_name.text.casefold())#adding the names into the list 

        device_price =driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[i]}/td[3]")#locating the device price in each row
        device_price_list.append(device_price.text.casefold())#adding the prices into the list
        

    
device_not_found = True#creating the flag
for l in range(len(device_name_list)):#iterating upto length of either of the lists   
    if entered_device_name == device_name_list[l]:
        print(f"The device '{device_name_list[l]}' is present and its price is '{device_price_list[l]}'. ")
        device_not_found =False
        
if device_not_found: 
    print("The entered device name is not present.")
    
s=driver.save_screenshot(r"\Screenshots\pageination.png")
print(s)

    
  
      
        

