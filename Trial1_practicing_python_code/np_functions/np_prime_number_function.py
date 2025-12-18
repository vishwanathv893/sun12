'''
Created on 18-Dec-2025

@author: vishw
'''
#A Prime number is number which is divisible by itself and one only.Since 1 is not prime number , these numbers are always greater than one.

def prime_number_checker(a) :
    if a==0 or a==1:
        print("Enter any number except zero and one.")
    else:
        count=0
        for i in range(2,a+1):
            if a%i == 0:
                count=count+1
        if count>1:
            print("The given number is not prime number.")
            
        else:
            print("The given number is prime number.")
        
number = int(input("Enter only the natural positive integer number:"))
prime_number_checker(number)

        
                
                
             
    
    
