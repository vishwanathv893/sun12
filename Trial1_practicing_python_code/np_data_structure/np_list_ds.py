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
2. Accessing the elements:
    - Using Index:  List supports indexing
        Index is a number which represents a position in a DS
        - Positive Index: 
            > Numbering the positions from left-to-right ( --> )
            > Index starts with 0, 1, 2....
            
        - Negative Index:
            > Numbering the positions from right-to-left ( <-- )
            > Index starts with -1, -2, -3....
            
        - Syntax: ds_name[index] --> this will return the value present in that index
        
        - We get IndexError in following cases
            > Using index greater than or equal to length of the list. Ex: list4[7]
            > Using index lesser than the negative value of length of the list. Ex: list4[-8]
            
    - Using loops
    - Using slicing operator        
@author: vishw
'''
a =7
b=5
list1 = [a+b,a-b,a*b,a/b]
print("list1:",list1)
print(type(list1))
print(id(list1))
print()

print()

c = [9,2.5,3j+9,"vishwa",True,7]
print(c)
print(id(c))
#new element can be assigned  to existing  list
c[0]=99
print("c afer modifiying :",c)
print(id(c))

d=[range(9)] # output :-- d: [range(0, 9)]
print("d:",d)

e =[4]
f=[4]
print(id(e),id(f)) #in list same objects are stored in different memory location


#Accessing elements from the list 
print("list1[1]:",list1[1])    

print("Accessing using for loop:")
for i in list1:
    print(i)

print("Accessing using while loop:")
i=0    
while i<len(c):
    print(c[i])
    i+=1
    
print("Accessing using slicing operator:")
print(c[:6:2])

print("======Functions specific to Lists==========")
c.append(d)
print("c list appended with d list:",c)
#c.clear()
#print("c variable after clear function:",c)
g =c.copy()
print("g variable:",g)
h=c.count(1)
print("h:",h)
c.extend(d)
print("c",c)
c.remove('vishwa')
print("c",c)

'''
x = 9380084062 #TypeError: 'int' object is not subscriptable
print(x[:4])
print(type(x))
'''
y = "9380084062"
print(y[:4])
print(type(y))
print(type(c))
print(c.index(7))
print(c.pop(1)) #remove the value pointed by index and returns to console.
print(c)
print(c.remove(True))#True (boolean value) is same as 1 (integer value) 
print(c)
c.reverse()
print(c)
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

print("Printing the even numbers from a list having only integers:")
l1 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
l1_even=list()
for i in l1:
    if i%2 == 0 :
        l1_even.append(i)
print(l1_even)

print("Printing the odd numbers from a list having only integers:")
l1_odd=list()
for i in l1:
    if i%2 == 1 :
        l1_odd.append(i)
print(l1_odd)

#List Comprehension 
L_cprhsn =[j for j in l1 if j%2 == 0]
print(L_cprhsn)


print()      
print("Finding the elements in the list of duplicate and unique elements chosen by user and printing the number of times the element appears with their indices ")
print()        
l_ds=[1,3,5,22,6,7,4,7,4,8,3,9,2,5,7,99,100,103,99]
print(len(l_ds)) 
print("l_ds = ",l_ds)
print()

element=input("Enter the elements you wish to know which index does it belongs to and how many times does it appears in the list :")
elements=int(element)
if elements in l_ds:
    for i in l_ds:
        count = l_ds.count(elements)
    print("The number of times the element repeated is:",count)
    
    ie =list() #creating the separate list
    for k in range(len(l_ds)): 
        if l_ds[k] == elements:
            ie.append(k) #appending the  index of elements 
    print("index of the chosen element is:",ie)
else:  
    print("Please enter the elements which are only present in given list:")

    



