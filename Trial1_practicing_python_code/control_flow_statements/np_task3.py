'''
Created on 20-Oct-2025

@author: vishw
'''
print("Checking whether the given year is 'Leap year' or not :-")
lp =input("Enter the year :") 
# A leap year should be divisible by 4 and not by 100, if the given year is century year  it should be divisible by 400.
lp1 = int(lp)
if lp1%4==0  and (lp1%100 or lp1%400 ==0):
    print("The given year is a Leap year.")
else:
    print("The given year is  not a Leap year.")
    
    