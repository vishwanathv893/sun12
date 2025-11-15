'''
Created on 25-Oct-2025

@author: vishw
'''
#taking input from the user for which day it is so that he/she can park vehicle according to  parking rules

while True :
    number = int(input("Please enter the number for desired day :"))
    match number:
        case 1:
            print("1 represents Monday")
            break
                
        case 2:
            print("2 represents Tuesday")
            break
                
        case 3:
            print("3 represents Wednesday")
            break
                
        case 4:
            print("4 represents Thursday")
            break
                
        case 5:
            print("5 represents Friday")
            break
                             
        case 6:
            print("6 represents Saturday")
            break
                
        case 7:
            print("7 represents Sunday")
            break
                   
        case _ :
            print("PLease enter 1 to 7:")
            
print() #adding newline in console
print("Demonstrating a simple calculator using basic arithmetic operations :-") 
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:")) 
print() 
while True :
    op=int(input("Enter which arithmetic operation you want perform by entering  number 1 for add, 2 for sub,3 for multi, 4 for div options: "))
    print()
    match op:
        case 1:
            res =a+b
            print("Result for addition:",res)
            
        case 2: 
            res=a-b
            print("Result for subtraction:",res)
            
        case 3:
            res=a*b
            print("Result for multiplication:",res)
            
        case 4:
            res=a/b
            print("Result for division:",res)
            
        case _ :
            print("Enter only mentioned numbers.")    
                       
            
               
             
            
                
              
            
             
                
            
        
                
           
                
                
           
                

        
