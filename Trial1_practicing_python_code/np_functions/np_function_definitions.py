'''
Created on 07-Nov-2025

@author: vishw
'''
def call():
    print("The following functions used are called from 'np_function_definitions' including this one.")
 
def factorial(a):
    if a == 0:
        result = 1
    else:
        result = a*factorial(a-1)
    return result

def add(a, b): # Function with parameters
    c=a+b
    return c # returns value when function is called. return statement is optional

def sub(a, b):
    d=a-b
    return d

    
def add_sub(a, b):
    c = add(a, b) # calling a function inside another function
    d = sub(a, b)
    return c, d # returning multiple values

def fibonacci(i,a=0,b=1):
    for i in range(i):
        res=a+b
        print(res,end=" ") # 0 and first 1 are default values
        a=b
        b=res
    return res    
        
         
    
    
    