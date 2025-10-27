'''
Created on 27-Oct-2025

List: 

- List is a DS where elements stored within square braces separated by commas
1. Creation:
    - Empty list can be created
    - List with elements:
        > Manual entry
        > Using built-in function - list()
        > 
@author: vishw
'''
a =7
b=5
list1 = [a+b,a-b,a*b,a/b]
print("list1:",list1)
print(type(list1))
print(id(list1))

c = [1,2,3]
print(id(c))
c = [1,2,3] + [4] #new element can be added or attached to existing  list
print("c :",c)
print(id(c))

d=[range(9)] # output :-- d: [range(0, 9)]
print("d:",d)

e =[4]
f=[4]
print(id(e),id(f)) #in list same objects are stored in different memory location