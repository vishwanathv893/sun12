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

tu3=tuple(range(6))#tuple with an iterable function i.e. range()
print("tu3:",tu3)
print(type(tu3))

a=5
b=2
tu4 =(a+b,a-b,a*b,a/b)# using operations as elements inside the tuple
print("tu4",tu4)

