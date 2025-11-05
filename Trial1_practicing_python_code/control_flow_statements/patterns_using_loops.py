'''
Created on 31-Oct-2025

@author: vishw
'''

print("Squre fill pattern:-")

for j in range(6):
    for i in range(6):
        print("*",end=" ")
    print()
    
print()     
print("Square Hollow Pattern:")
print("* "*5) # used string multiplication instead of for-loop 
for l in range(3):    
    for j in range(0,5,4):
        print("*",end="       ")#step value 4 and 7 spaces(4 blank space and 3 space of *)   
    print() 
print("* "*5)

print() 
print("Right-half pyramid:")  
r =list(range(6))
i=0
while i<=5:
    print(r[i]*"* ")
    i+=1
    
print()     
print("Reverse right-half pyramid:") 
r =list(range(6))
i=5
while 0<i<=5:
    print(r[i]*"* ")
    i-=1
    
print()
print("Number triangular:")
space =" "
j=4
for i in range(1,5):
    print((j-1)*space+i*(f"{i}"+space ))#used string formating,for j numbers ,the preceding spaces are (j-1) and i(number + space)
    j-=1
print()

'''
print("Number increasing pyramid:")
for j in range(1,5): 
    print(f"{j} ") 
    '''  
            
    
    
  

        