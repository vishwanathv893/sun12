'''
Created on 27-Oct-2025
tuple : 
- defined using parenthesis
- empty tuple can be created 
- iterable function can be used in order to define data elements
- elements with different data types can be defined and arithmetic operations can be done inside the tuple

@author: vishw
'''
tu =()#Empty tuple
print("tu:",tu)
print(type(tu))

tu1=(1,2,3,4,5)#tuple with listed elements
print("tu1",tu1)
print(type(tu1))

tu3=tuple(range(6))#tuple with an itereble function i.e. range()
print("tu3:",tu3)
print(type(tu3))

a=5
b=2
tu4 =(a+b,a-b,a*b,a/b)# using operations as elements inside the tuple
print("tu4 :",tu4)

c = (1,2,3)
print(id(c))
c= (1,2,3)  #new element cannot be added or attached to existing  tuple
c1 =(7) 
#c =c+c1
print("c:",c)

d=(4)
e =(4)
print(id(d),id(e))#in tuple same object is stored in one memory location

 


