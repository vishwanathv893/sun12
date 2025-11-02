'''
Created on 28-Oct-2025

@author: vishw
'''
for m in range(4):
    print(m)

print("range function with start & stop arguments:")    
for b in range(-9,9):
    print(b)
    
print("range function with start,stop and step arguments:")    
for i in range(1,20,2):
    print(i)
    
print("range function with negative step value: ")
for j in range(20,0,-2):
    print(j)
    
print("range function with negative start value:")
for k in range(-45,0,5):
    print(k) 
    
print("range function with +start,-stop,-step:")
for l in range(50,-50,-7):
    print(l)  
    
print("range function with -start,-stop and + step:")
for n in range(-25,-15,3):
    print(n)    
    
print("range function with -start,-stop and -step:")  
for s in range(-1,-40,-2):
    print(s)  #reverse /negative step cannot be given for -start and -stop arguments
    
#step value should be negative if start value is greater than stop value
#step value should be positive if start value is lesser than stop value
#if only two arguments are given then stop value should always greater than start value
#if single argument is used then it should be only positive number
