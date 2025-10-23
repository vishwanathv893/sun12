'''
Created on 20-Oct-2025

@author: vishw
'''
print("Checking whether the given number is negative or zero or positive :-")
x = input("Enter the number :")
x1 = int(x)
if x1<0 :
    print(f"The entered number {x1} is negative.") #unsing 'f-string' to include  user input
elif x1>0 :
    print(f"The entered number {x1} is positive.")
else:
    print(f"The entered number {x1} is zero.")   

   
    
     
    
