'''
Created on 12-Oct-2025
comments : provides description about single line or block of a code , two types of comments 
single line comments : starts with # (hashtag) symbol
multi-line comments : starts with triple single quotes or double quotes  and ends with same notation 

variables : name given to memory location which stores input or output data and the data stored can be changed thats why the name is variable.
syntax : variable_name = value
naming conventions :
@author: vishw
'''
num1 =  2 #integers should not start with zero i.e only natural numbers
print('num1:',num1) # detailed output for reference
num2 = 1998
num3 = 5.25
name = 'vishwa' #string
print(name)
print(id(name))

#defining multiple variables in single line
num4,num5,num6 = 12,34,56
print(num4,num5)

num7 = num8 = 10
print(num7)
print(id(num7))
print(id(num8))
#variables names should always start with characters or letter ,it should not start with  numbers
#names should always be in left hand side and values should be in right hand side
#single type print function

''' How function calls or fetch data stored in the memory ?
-function calls the nametag ie variable name 
-value assigned to that nametag is fetched from memory
-if the value is same then multiple nametags are assigend to single memory ID.
'''



