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
print("Number increasing pyramid:")
for i in range(1,6):#
    print()#for line by line print
    for j in range(1,i):#starting from 1 for loop is iterating range function till ith as stop value 
        print(j,end=" ")
        
print()
print("Number increasing reverse pyramid:")  
for k in range(5,-1,-1):#logic is start value in k-loop is stop value in i-loop
    print()#for line by line print
    for i in range(1,k):
        print(i,end=" ")      
 
print()
print("Number Changing pyramid:")
num =1
for i in range(6): 
    print() 
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    

print()
print("Zero - One pattern:")
z=0
o=1
for i in range(6):
    
        
print()
print("Rhombus Pattern:")
space=" "
for j in range(6):#increments spaces 
    print()
    print(j*space,end=" ")
    for i in range(5):#prints string * * * * *
        print("*",end=" ")              
'''   
print()
print("Daimond Pattern:")
space =" "
j=4
for i in range(1,5):
    print((j-1)*space+i*("*"+space ))#used string formating,for j numbers ,the preceding spaces are (j-1) and i(number + space)
    j-=1
for k in range(1,4):
    print((k-1)*space+i*("*"+space ))#used string formating,for j numbers ,the preceding spaces are (j-1) and i(number + space)
    j-=1
'''    

         
    
    
  

        