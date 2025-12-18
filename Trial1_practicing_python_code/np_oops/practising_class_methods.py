'''
Created on 14-Dec-2025

@author: vishw
'''
types_of_footwares =["slippers","sandals", "casual shoes","running Shoes", "trekking shoes"]

class Footware:
    
    def __init__(self,size_of_feet_in_inch,type,color,price):#constructer method
        self.size_of_feet_in_inch=size_of_feet_in_inch
        self.type=type
        self.color=color
        self.price=price
        print(f"The footware is {type},its size is {size_of_feet_in_inch} Inch , its color is {color} and its price is {price}.")

        
    def purpose(self):#method
        if self.type == "slippers":
            print(f"{self.type} are used for normal use.")
            
        elif self.type=="sandals":
            print(f"{self.type} are used for special use.")
        
        elif self.type=="casual shoes":
            print(f"{self.type} are used for office or professional use.")
        
        elif self.type=="running shoes":
            print(f"{self.type} are used for sports use.")
        
        elif self.type=="trekking shoes":
            print(f"{self.type} are used for adventure use.")
    
f1=Footware(7.5,"slippers","black","Rs.100")
f1.purpose()
print()

f3=Footware(type="casual shoes",size_of_feet_in_inch=8,price="Rs.200",color="white")
f3.purpose() 

print(f3.price)





        
    