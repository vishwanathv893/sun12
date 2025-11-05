'''
Created on 27-Oct-2025
tuple : 
- defined using parenthesis
- empty tuple can be created 
- iterable function can be used in order to define data elements
- elements with different data types can be defined and arithmetic operations can be done inside the tuple

@author: vishw
'''
tu =()#Empty tuple can be created
print("tu:",tu)
print(type(tu))

tu1=(1,2,3,4,5)#tuple with listed elements
print("tu1:",tu1)
print(type(tu1))

tu3=tuple(range(6))# using tuple function with an iterable function i.e. range()
print("tu3:",tu3)
print(type(tu3))

a=5
b=2
tu4 =(a+b,a-b,a*b,a/b)# using simple arithmetic operations as elements inside the tuple
print("tu4 :",tu4)
print()
c = (1,2,3)
print("c:",id(c))
d= (1,2,3)  
print("d:",id(d)) #in tuple the memory location is one and only for same objects assigned to different variables 

#new element cannot be added or attached to existing  tuple
#tuple is immutable
c =(1,2,3)+tu1 #in tuple concatination of tuple into other can be done
print("c:",c)
'''after concatination old tuple is
    replaced by new tuple having 
    different memory location,no modification of existing tuple
    it indicates that tuple data structure is immutable
                '''
print("c:",id(c))
print("d:",id(d))
'''
c[0]=99
print("c:",c)#TypeError: 'tuple' object does not support item assignment
'''
print()
print("-------------Accessing elements from tuple-----------")
t1 =tuple(range(91,100))
print("t1:",t1)
print("Using indexing:")
print("t1[2]:",t1[2])

print()
print("using while loop:")
i=0
while i<len(t1):
    t1_w=t1[i]
    i+=1
    print(t1_w)
    
print()
print("using for loop:") 
t1_f=[j for j in t1 ] 
print(t1_f)
print(type(t1_f))


print()
print("--------tuple specific in-built function------" )
count=t1.count(91)#returns value idicating how many times the element is repeated
print("count:",count)

print()
t2 =(1,2,3,1,2,3,3,4,5,2,1,5,2,6,7)
print("t2:",t2)
idx=t2.index(2,6,10)#returns index position of a value within 6th to 10th index
print("index position of 2 starting from 6th and stop @ 10th:",idx)
print()






 


