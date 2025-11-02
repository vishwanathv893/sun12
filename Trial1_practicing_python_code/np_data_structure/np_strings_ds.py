'''
Created on 02-Nov-2025
string:

@author: vishw
'''
empty_string =""
print(type(empty_string))
name="vishwa"
name1="MANU"
action ="reading"
#can define multiple lines of string using triple-single quotes or triple-double qotes
adress ='''sagara
           Shivamogga
           karnataka
           '''
print(type(adress))  
message =("Welcome to 'iquest'")  
print(message)     

#Accessing the characters 
'''
1.indexing
2.slicing
3.loops
'''
#use the above methods (assignment)

print("Accessing using the index:")
s1 ="All is well"
print(s1)
print(s1[0])
print(s1[3])
print(s1[8])
print()
print("Accessing using slicing:")
s2 =("I have 2 pens & 1 eraser")
print(s2)
print(s2[:3])#starts with 0th index
print(s2[:])#access whole string
print(s2[3:])#starts with 3rd index
print(s2[4:7])#slices string according to mentioned indesis
print()

print("Accessing using loops:")
print()

print("Accessing using while loop:")
s3 =("'Always watch your 6!'")
l_s3 =len(s3)
i=0
while i<l_s3:
    print(s3[i],end=" ")
    i+=1
print()
print()

print("Accessing using for loop:")
s4="I have dictator who always obeys me."
axes = [j for j in s4]
print(axes,end=" ")
print()

#string is immutable
print()
print("<--------------pre_defined functions------------->")
print()

c_name=name.capitalize() #first letter will be in capital 
print(c_name)

cs_name1=name1.casefold()
print(cs_name1)

cen_name =name.center(10, '-')
print(cen_name)

edswth_action =action.endswith('ing')
print(edswth_action)

sentence =' '.join(["my","name","is","vishwa"])
print(sentence)

rmve =cen_name.strip("-")
print(rmve)

