'''
Created on 14-Oct-2025

@author: vishw

Operator: Is a symbol which performs operation on one or more operands(variables)

I. Classification of operators based on No. of operands:
    1. Unary operator: acts on single operand
        Ex: =, -
    2. Binary Operator: acts on two operands
        Ex: +, - etc.,
    3. Ternary Operator: acts on three operands
        Ex: list comprehension

II. Classification of operators based on Operations:
    1. Arithmetic Operators: +, -, *, /(Quotient), %(Reminder), ** (Exponent), // (Floor division)
    2. Comparison/ Relational Operators: >, <, >=, <=, !=, ==
    3. Assignment Operator: =
    4. Logical Operators 
'''

#Arithmetic Operations
x,y,z = 2,3,4
op1 = x + y
print("Addition operation ,op1 :" ,op1)
op2 = x - y
print("Subtraction operation ,op2 :",op2)
op3 = z%y
print("Modulus operation ,op3:" ,op3) #returns remainder
op4 = z/y 
print("Division operation ,op4:",op4) #returns quotient
op5 =y**z
print("Exponential operation ,op5:" ,op5)
op6 = z//y 
print("Floor Division operation ,op6:",op6)# returns quotient in whole number

#Unary operation
ury1 = -(op1)
print("Unary Operation (negative sign) ,ury1:",ury1)

#Relational operators
re1 =(op2 == op6) #Equal operator
print ("re1 :",re1)
re2 =(op1>op3) #greater-than operator
print ("re2:",re2)
re3 =(op1 < op5) # Lesser-than operator
print("re3:" ,re3)
re4=(op3>=op6) # greater than or equal-to
print("re4:",re4)
re5=(ury1<=op1) # Lesser than or equal-to
print("re5:",re5)

