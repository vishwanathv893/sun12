'''
Created on 15-Nov-2025

@author: vishw
'''
print("Finding the index of an element in a tuple:")
x=(34,2,67,-9,67,22,97,45)
print(x)
i=(int(input("Entry the element you wish to know its index: ")))
j=x.index(i)
print(f"Index of the element {i} is:",j)
