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

applications_list=[]

for i in range(1,5):
    applications_name =driver.find_element(By.XPATH,f"//tbody[@id='rows']/tr{[i]}/td[1]")
    applications_list.append(applications_name.text.casefold())
     
process_not_found =True
for j in range(0,len(applications_list)):
    if process_name == applications_list[j]:
        while True:
            number =int(input("1.memory_space \n2.percentage_cpu_used \n3.disk_speed \n4.network_speed. \nEnter the number associated with feature name to get the details :"))
            match number:
                case 1:
                    memory_space =driver.find_element(By.XPATH, f"//table[@id='taskTable']/tbody[@id='rows']/tr{[j+1]}/td[contains(text() ,'MB') and not( contains(text(),'/s'))]")
                    print(f"Memory Size of {applications_list[j]} process is {memory_space.text}.")
                    break
                    
                case 2:
                    percentage_cpu_used=driver.find_element(By.XPATH,f"//table[@id='taskTable']/tbody/tr{[j+1]}/td[contains(text(),'%')]")
                    print(f"CPU load of {applications_list[j]} process is {percentage_cpu_used.text}.")
                    break
                    
                case 3:
                    disk_speed=driver.find_element(By.XPATH,f"//table[@id='taskTable']/tbody/tr{[j+1]}/td[contains(text(),'MB/s')]")
                    print(f"Disk Speed of {applications_list[j]} process is {disk_speed.text}.")
                    break
                    
                case 4:
                    network_speed=driver.find_element(By.XPATH,f"//table[@id='taskTable']/tbody/tr{[j+1]}/td[contains(text(),'Mbps')]")
                    print(f"Network speed of {applications_list[j]} process is {network_speed.text}.")
                    break
                    print()
                case _ :
                    print("PLease enter 1 to 4:")
        process_not_found=False

if process_not_found:
    print("The process name is not present in the dynamic web table")


                    



                    



                    
                    

                    

