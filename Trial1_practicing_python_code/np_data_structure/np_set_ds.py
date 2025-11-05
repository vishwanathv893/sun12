'''
Created on 27-Oct-2025

@author: vishw
'''
set1 ={}
print("set1:",set1)
print(type(set1)) #Class 'dict'
print()

set2 ={1,2,3,4}
print("set2:",set2)
print(type(set2))#Class 'set',non empty set always belongs to class set
print()

set3 = {5,9,6,"f","g"}
#set3[0]="vishwa" #TypeError: 'set' object does not support item assignment
print("set3:",set3)
print()
'''
set4 ={1,2}
set4 ={1,2} +set3
#print("set4:",set4)#new element cannot be added or attached to existing  set
'''
print()
set5 ={range(6)}
print("set5:",set5) #set5: {range(0, 6)} ,elements are represented through set 

print()
set6 ={1}
set7 ={1}
print(id(set6),id(set7)) #in set same object is stored in different memory location

print()
print("Accessing the elements in the set:")

s1 ={25,5,"vishwa",56.9,-3,True,None,6j+8,"&"}
#print("s1[3]:",s1[3]) #TypeError: 'set' object is not subscriptable

print()
'''
print("Accessing using while loop:-")
i=0
while i<len(set3):
    print("set3:",set3[i])
    i+=1
#TypeError: 'set' object is not subscriptable
#set elements cannot be accessed using while loop  
'''
'''
print()
print("Accessing using for loop:-")
for j in range(len(set3)):
    print("set3:",set[j])
#TypeError: 'set' object is not subscriptable   
''' 
#set2=set2.append(8) AttributeError: 'set' object has no attribute 'append'