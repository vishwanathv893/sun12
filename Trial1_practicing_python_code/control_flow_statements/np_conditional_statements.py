'''
Created on 16-Oct-2025

@author: vishw

Indentation: It is the leading space to define a block of code
1 Indentation = 1 tab space = 4 normal spaces

Conditional statements: Flow of program execution will be decided based on a condition.
(Decision-making statements)

1. if statement
2. if-else statement
3. Series if-else statements
4. Nested if-else statements
'''
'''Here I am using conditional statments to explain 'KSRTC bus ticketing scenario'  from  mysore to nanjangud ,where conductor give bus tickets according to some guidelines
    -female/women have special allowance where they don't charged (nil)
    -male/men have to pay the prescribed  bus charge (Rs:46)
    -childrens(male) below age 7 are waived of charge(nil)
    -childrens(male) above age 7 and below 18 are charged with half price of the bus ticket(Rs:23)
    -Scenior citizen have concession on bus ticket(Rs :32)
    -Any person having 'bus pass' won't charged as they previously paid for certain duration(nil)
these points are only approximation not to take accuratly .
'''  
print("Kindly ensure to give input in lower case & without any space. ")
gender = input("Please enter your gender ,type 'male' or 'female':")


if gender == 'female' :
    print("Bus Charge not applicable ,special allowance.")
elif gender == "male":
    age_below_7 =input("Kindly confirm whether age is below 7 , type 'yes' or 'no' :")
    if age_below_7 == 'yes':
        print("Bus Charge not applicable , age is below 7. ")
    elif age_below_7 == 'no':
        answer =input("Please confirm having bus pass ,type 'yes' or 'no' :")
        if answer == 'yes':
            print("Bus Charge not applicable,possess bus pass")
        elif answer == 'no':
            half_charge =input("If age is between 7 & 18 then type 'yes' if not then 'no' : ") 
            if half_charge == 'yes':
                print("Half Chargeble,pay Rs:23")  
            elif half_charge == 'no':   
                age_group =input("Kindly Confirm which  other age group you belong to ,adult or scenior citizen :")
                if age_group =="adult":
                    print("Full Chargeble ,pay Rs:46")
                elif age_group == "scenior citizen":
                    print("Charge concession,pay Rs:32")    
 
print("Programm terminated :)")       
            
        
        
    
    
    




