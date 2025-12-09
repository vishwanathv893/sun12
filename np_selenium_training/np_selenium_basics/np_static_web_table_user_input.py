'''
Created on 07-Dec-2025

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

print("Taking input from the user and checking if the 'book name' is present or not,if present then display its 'price' on the console. ")
print()
entered_book_name =input("Please enter the book name:")
entered_book_name.casefold()
print()
books_on_table =[]#defining list

for j in range(2,8):#each row is accessed
    book_name =driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr{[j]}/td[1]")#locating the 1st elements from each row in  static web table using xpath with string formating
    books_on_table.append(book_name.text.casefold())#storing the book names in the list DS using append functions    


i=0
book_not_found=True #defining a flag as true 
while i<=5:
    if entered_book_name == books_on_table[i] :
        price_of_book =driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr{[i+2]}/td[4]")#finding the price value on static web table
        print(f"The book '{books_on_table[i]}' is present and its price is '{price_of_book.text}'")#printing the price 
        book_not_found=False # indicates book is found and prints the price 
    i+=1

if book_not_found :#as flag is initially defined True,statement is executed
    print("The entered book name is not on the table. ")
        
driver.quit()
        
        

