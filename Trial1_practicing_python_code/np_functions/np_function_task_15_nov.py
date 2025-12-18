'''
Created on 17-Nov-2025

@author: vishw
'''
print("Defining a function that returns the maximum of three numbers:")
def max_3(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    if a>b and a>c:
        return a
    elif a<b and b<c:   
        return c
    else:
        return b
    
m=max_3(-9.5,-8.85,0)  
print("The maximum of 3 numbers is",m)     
