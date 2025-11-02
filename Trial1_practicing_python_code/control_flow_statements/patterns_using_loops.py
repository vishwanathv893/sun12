'''
Created on 31-Oct-2025

@author: vishw
'''

print("Squre fill pattern:-")

for j in range(6):
    for i in range(6):
        print("*",end=" ")
    print()
    
    
print("Square Hollow Pattern:")
print("* "*5) # used string multiplication instead of for-loop 
for l in range(3):    
    for j in range(0,5,4):
        print("*",end="       ")#step value 4 and 7 spaces(4 blank space and 3 space of *)   
    print() 
print("* "*5)

print("Right-half pyramid:")  
r =list(range(6))
i=0
while i<=5:
    print(r[i]*"* ")
    i+=1
    
print("Reverse right-half pyramid:") 
r =list(range(6))
i=5
while i<=5:
    print(r[i]*"* ")
    i-=1
    
    
    
    
  

        