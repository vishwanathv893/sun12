'''
Created on 09-Dec-2025

class By:
    """Set of supported locator strategies.
    
    ID:
    --
    Select the element by its ID.
    
    >>> element = driver.find_element(By.ID, "myElement")
    
    XPATH:
    ------
    Select the element via XPATH.
    - absolute path
    - relative path
    
    >>> element = driver.find_element(By.XPATH, "//html/body/div")
    
    LINK_TEXT:
    ----------
    Select the link element having the exact text.
    
    >>> element = driver.find_element(By.LINK_TEXT, "myLink")
    
    PARTIAL_LINK_TEXT:
    ------------------
    Select the link element having the partial text.
    
    >>> element = driver.find_element(By.PARTIAL_LINK_TEXT, "my")
    
    NAME:
    ----
    Select the element by its name attribute.
    
    >>> element = driver.find_element(By.NAME, "myElement")
    
    TAG_NAME:
    --------
    Select the element by its tag name.
    
    >>> element = driver.find_element(By.TAG_NAME, "div")
    
    CLASS_NAME:
    -----------
    Select the element by its class name.
    
    >>> element = driver.find_element(By.CLASS_NAME, "myElement")
    
    CSS_SELECTOR:
    -------------
    Select the element by its CSS selector.
    
    >>> element = driver.find_element(By.CSS_SELECTOR, "div.myElement")
    

@author: vishw
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

options =  webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com")

print("Displaying all text contents in pagination table:")
print()
'''
for i in range(1,6):
    row =driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[i]}")
    print(row.text)
    
pagination_button = driver.find_element(By.XPATH, "//ul/li/a[text() = 2]")
pagination_button.click()

for i in range(1,6):
    row =driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[i]}")
    print(row.text)
    
pagination_button = driver.find_element(By.XPATH, "//ul/li/a[text() = 3]")
pagination_button.click()

for i in range(1,6):
    row =driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[i]}")
    print(row.text)
    
pagination_button = driver.find_element(By.XPATH, "//ul/li/a[text() = 4]")
pagination_button.click()

for i in range(1,6):
    row =driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[i]}")
    print(row.text)
'''    
for j in range(1,5):
    pagination_button = driver.find_element(By.XPATH, f"//ul/li/a[text() = {j}]")
    pagination_button.click()
    
    for i in range(1,6):
        row =driver.find_element(By.XPATH,f"//table[@id='productTable']/tbody/tr{[i]}")
        print(row.text.casefold())
    
    
    
    
driver.quit()
  


