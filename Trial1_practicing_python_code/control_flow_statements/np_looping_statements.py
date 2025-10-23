'''
Created on 23-Oct-2025

"Reduce repetation - increase reuse" --> Easy maintenence

Looping statements: 
- Looping statements are used to execute any statement/s repeatedly.
- Any statement/s will be executed repeatedly until a condition is fulfilled

Types of Looping Statements:
1. While loop:
    - initial variable -- used to set initial value
    - define the condition
    - increment/ decrement
    
2. For loop

@author: vishw
'''
#while loop : incremental
statement =input("Enter any statement you wish to repeat multiple times :")
no_of_times =int(input("Enter how many times you want to repeat the given statement :"))
count = 1               
while count <= no_of_times :
    print(f"{count}.",statement) # Using formatted string literal(f-string) to include numeric values along with statement
    count+=1 