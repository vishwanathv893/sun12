'''
Created on 13-Oct-2025

@author: vishw

Data types :
type() : a predefined function to check the type of the value 
key words : starts with cap letter
Derived data types :
type casting :

'''
num1 = 6
num2 = 3.2
num3 = 6+8j
print(type(num1), type(num2),type(num3))

var1 = True
var2 = False
var3 = None #none type keyword is used if the value assigned to variable is yet to be decided
print( 'var3 data type ,var3 :',type(var3))

#Type casting : converting one data type into other data type
num4 = float(num1)
print(num4)
print('After type casting :' ,type(num2))

num5 = int(num2)
print('After type casting' ,num5)

'''num10 =int(num3)
print('num10 :',num10) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
'''
#boolean function
num6 = -6
num7 = bool(num6)
print('num7 :',num7)
print(type(num7))
num8 = 0
num9 =bool(num8)
print('num9:', num9)




        