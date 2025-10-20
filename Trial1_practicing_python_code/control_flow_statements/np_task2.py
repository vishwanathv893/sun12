'''
Created on 20-Oct-2025

@author: vishw
'''
print("Finding the greatest of the three given numbers :-")
a =input("Enter the value for a :")
a1=int(a)
b=input("Enter the value for b :")
b1=int(b)
c =input("Enter the value for c :")
c1=int(c)
if a1>b1 and a1>c1 :
    print("The value assigned to 'a' is greater among them.")
elif b1>a1 and b1>c1 :   
    print("The value assigned to 'b' is greater among them.")
else:
    print("The value assigned to 'c' is greater among them.")

