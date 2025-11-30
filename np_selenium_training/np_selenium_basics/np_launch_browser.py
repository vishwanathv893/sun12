'''
Created on 08-Nov-2025

@author: vishw


SELENIUM :-
- Selenium is an umbrella project(a large, overarching project that coordinates or encompasses multiple smaller, independent projects) for a range of tools and libraries that enable and support the automation of web browsers.
- It provides extensions to emulate user interaction with browsers.
- At the core of Selenium is WebDriver, an interface to write instruction sets that can be run interchangeably in many browsers.

WEBDRIVER :- 
- WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server. It marks a leap forward in terms of browser automation.
- Selenium WebDriver refers to both the language bindings(libraries or APIs that allow you to interact with Selenium WebDriver using a specific programming language) and the implementations of the individual browser controlling code. This is commonly referred to as just WebDriver.
- Selenium WebDriver is designed as a simple and more concise programming interface.It is a compact object-oriented API.It drives the browser effectively.

Selenium as an API: 
- Selenium itself, particularly Selenium WebDriver, provides an API. This API is a set of classes, interfaces, and methods that allow you to programmatically interact with web browsers.
- When you write Selenium code in a language like Java, Python, C#, or JavaScript,you are using the Selenium API to send commands to the browser.
  (e.g., "find this element," "click this button," "enter text here," "navigate to this URL").

Reason why selenium webdriver:
- If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs.
- WebDriver uses browser automation APIs provided by browser vendors to control the browser and run tests.This is as if a real user is operating the browser.
- Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live. 
- Selenium WebDriverallows users to simulate common activities performed by end-users; entering text into fields, selecting drop-down values and checking boxes, and clicking links in documents.
- It also provides many other controls such as mouse movement, arbitrary JavaScript execution, and much more.
'''
from selenium import webdriver #Imports Selenium’s webdriver module
from selenium.webdriver.common.by import By
#import time


options =webdriver.ChromeOptions()#the ChromeOptions() class provides add settings or custom behavior to Chrome before launching it.
options.add_experimental_option("detach", True)#"detach" True, tells Chrome NOT to close automatically when script finishes running.
options.add_argument("start-maximized")#"start-maximized" tells Chrome to open in maximized window mode
driver= webdriver.Chrome(options) #Launches the Chrome browser with the options set by above lines of code.driver becomes the object of Chrome() class to control the browser
driver.get("https://testautomationpractice.blogspot.com/")#driver object opens the url using get method.
driver.implicitly_wait(5)
print("Navigated to practice site.")
'''
name_txt_bx = driver.find_element(By.ID, "name")
name_txt_bx.send_keys("VISHWANATH")

email_text_box =driver.find_element(By.ID,"email")
email_text_box.send_keys("vishwanathv89@gmail.com")#entering the email

phone_txt_bx =driver.find_element(By.ID,"phone")
phone_txt_bx.send_keys("5236148952")#entering the phone number

address_txt_bx =driver.find_element(By.ID,"textarea")
address_txt_bx.send_keys("sagara,shivamogga,House No:256,vinoba nagara")

gender_button=driver.find_element(By.ID,"male")
gender_button.click()#clicking the button

day_check_box=driver.find_element(By.ID,"sunday")
day_check_box.click()#checking the box
'''



print("title name after entry name in automation page")
print(driver.title)

wiki_txt_bx = driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input")
wiki_txt_bx.send_keys("python")

wiki_search_clk =driver.find_element(By.CLASS_NAME,"wikipedia-search-button")
wiki_search_clk.click()
#time.sleep(20)

wiki_search_suggestion =driver.find_element(By.LINK_TEXT,"Python (missile)")#finding the link element in search suggestions which is in anchor tags
wiki_search_suggestion.click()#clicking on the link 
print("a new tab opens with wiki link title")

current_title_page = driver.title
print("current_title_page after clicking on wiki page :",current_title_page)

windows= driver.window_handles#this method collects the id of different windows and stores it in list
print(windows)


driver.switch_to.window(windows[1])#this method transfers the driver objects capability to another url
current_title_page_1 = driver.title
print("current_title_page_1",current_title_page_1)

wiki_link_name_click =driver.find_element(By.ID,"toc-External_links")
wiki_link_name_click.click()









