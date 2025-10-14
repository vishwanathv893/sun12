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
#int -> float
num4 = float(num1)
print(num4)
print('int->float,num4 :' ,num4 ,type(num2))

# complex -> float
#num11 = float(num3)
#print('complex -> float ,num11 :',num11) #TypeError: float() argument must be a string or a real number, not 'complex'

#float ->int
num5 = int(num2)
print('float -> int ,num5 :' ,num5)

#num12 = int(num3)
#print('complex -> int ,num12 :',num12)

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

name = "vishwa"
print("Data type of 'name' :" ,type(name))

#string -> int
#myint = int(name)
#print(" myint :",myint) ValueError: invalid literal for int() with base 10: 'vishwa'

#string -> float
#myfloat = float(name)
#print(" myfloat :",myfloat) #ValueError: could not convert string to float: 'vishwa'

#string -> boolean
mybool = bool(name)
print("mybool :",mybool)
print("Data type of mybool :",type(mybool))

#string -> int -> boolean 
shape = "0"
shape1 = int(shape)
var4 = bool(shape1)
print("var4 :",var4)
print("Data type of var4 :",type(var4))






        