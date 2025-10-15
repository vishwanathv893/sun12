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

II.Classification of operators based on Operations:
    1. Arithmetic Operators: +, -, *, /(Quotient), %(Reminder), ** (Exponent), // (Floor division)
        i/p: numerical
        o/p: numerical
        
    2. Comparison/ Relational Operators: >, <, >=, <=, !=, ==
        i/p: numerical
        o/p: boolean
        
    3. Assignment Operator: =
    4. Logical Operators: AND, OR, NOT
        i/p: boolean (True/ False)
        o/p: boolean
        
        AND(both): If 'a' AND 'b' is True, o/p will be True. Takes 2 i/ps
        OR(anyone): If any of the i/p is True, o/p will be True. Takes 2 i/ps
        NOT (reverse): If i/p is True o/p will be False and vice-versa. Takes 1 i/p
        
    5. Membership Operators: To check  whether any element is part of a group
        -- in, not in
    6. Identity Operators: To check identity/ to check whether 2 variables are identical
        -- is , is not
    7. Unary Minus operator: To negate the numbers
'''

#Arithmetic Operators
print("========Arithmetic Operation========")
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
print("Floor Division operation ,op6:",op6)# returns quotient in flooor number
op7 = 8.0 //3 #Floor division operation also returns float value
print("op7", op7)

#Unary operation
print("=======Unary Nagate Opertion======")
ury1 = -(op1)
print("Unary Operation (negative sign) ,ury1:",ury1)

#Relational operators
print("========Relational Operation========")
re1 =(op2 == op6) #Equal operator
print ("re1 :",re1)
re2 =(op1>op3) #greater-than operator
print ("re2:",re2)
re3 =(op1 < op5) # Lesser-than operator
print("re3:" ,re3)
re4=(op3<=op6) # lesser than or equal-to
print("re4:",re4)
re5=(ury1>=op1) # greater than or equal-to
print("re5:",re5)

#Logical Operators
print("=========Logical AND Operation=======")
print("re1 and re2 :" ,re1 and re2)
print("re2 and re3 :" ,re2 and re3)
print("re1 and re5 :" ,re1 and re5)

print("========Logical OR Operation========")
print("re1 or re2 :" ,re1 or re2)
print("re2 or re3 :" ,re2 or re3)
print("re1 or re5 :" ,re1 or re5)
print("re4 or re5 :" ,re4 or re5)

print("========Logical NOT Operation========")
print("not re1 :", not re1)
print("not re2 :", not re2)

#Membership operators
print("========Membership Operation=======")
print("w in 'vishwa'" ,'w' in 'vishwa')
print("n in 'vishwa'" ,'n' in 'vishwa')
print("t not in 'vishwa'" ,'t' not in 'vishwa')
print("7 not in '7,14,21,28'" ,'7' not in '7,14,21,28')

#Identity Operators
print("========Identity Operation======")
name1 ="vishwanath"
name2 = "Vishwanath"
print(id(name1) ,id(name2)) #different ID
print("vishwanath is Vishwanath" ,name1 is name2)
print("vishwanath is not Vishwanath" ,name1 is not name2)




