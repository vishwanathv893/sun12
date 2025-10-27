'''
Created on 27-Oct-2025

@author: vishw
'''
set1 ={}
print("set1:",set1)
print(type(set1)) #Class 'dict', so empty set belongs to class dictionary

set2 ={1,2,3,4}
print("set2:",set2)
print(type(set2))#Class 'set',non empty set always belongs to class set

set3 = {1+2,2+3,3-9,4.5-2 ,"g"}
print("set3:",set3)
#set3: {2.5, -6, 3, 5,'g'}  irrespective of  type of operations while assigning to set variable, its output is in order of {float,int,string}

set4 ={1,2}
#set4 ={1,2} + {3}
#print("set4:",set4)#new element cannot be added or attached to existing  set
set5 ={range(6)}
print("set5:",set5) #set5: {range(0, 6)} ,elements are represented through set 

set6 ={1}
set7 ={1}
print(id(set6),id(set7)) #in set same object is stored in different memory location