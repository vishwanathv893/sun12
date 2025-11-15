'''
Created on 15-Nov-2025

@author: vishw
'''

print("Finding the largest and smallest number in the list:")
x=[55,26,-9,0,85,6,115,4,-2,100]
print(x)

small =x[0]
large=x[0]
for i in x:
    if i < small:
        small=i
    if i>large:
        large =i      
print("Smallest number is :",small) 
print("Larger number is :",large)   
    

