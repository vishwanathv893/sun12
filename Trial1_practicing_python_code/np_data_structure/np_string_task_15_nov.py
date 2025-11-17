'''
Created on 17-Nov-2025

@author: vishw
'''
print("Reversing a string:")
s=("India")
print(type(s))
i=len(s)-1
reverse_s=" "
while 0<=i<len(s):
    reverse_s=reverse_s+s[i]
    i-=1
print(f"reverse of string is '{s}' is",reverse_s)    
    
   
    
    
    
    
