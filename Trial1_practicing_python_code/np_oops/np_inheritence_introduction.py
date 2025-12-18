'''
Created on 16-Dec-2025

@author: vishw
'''
#Inheritance is a concept where a class's attributes(variables and methods) are passed to another class. 
class Footwear:#Parent/Super class
    def __init__(self):#constructer  method
        print("The footwear constitutes mainly two parts 'sole' and 'upper' ")
        #return None
        
    def its_purpuse(self):
        print("Footware is used to protect the foot when moving from one point to another.")
    
    def order(self):
        print("Footwear class's method")
        
    
    
#Single-Level inheritance
class Slippers(Footwear):#Child/Sub class,in order to allow inheritance sub class name must have super class's name as its parameter
    def slippers_general_use(self):
        print("Slippers are used mainly for any casual routines")
        
    def order(self):
        print("Slippers class's method")
        
#Single-Level inheritance        
class Shoes(Footwear):#Child/Sub class
    def shoes_general_use(self):
        print("Shoes are used mainly for 'more physically demanding activities' ")
        
    def order(self):
        print("Shoes class's method")
        
#Multi-Level inheritance        
class Spike_shoes(Shoes):#sub-class for 'Shoes' super class
    def s_specific_use(self):
        print("Spike shoes are the special type of shoes which are specifically used in Athletic tracks ")
    
    def order(self):
        print("Spike_shoes class's method")
        
#Multi-Level inheritance       
class Football_shoes(Shoes):#sub-class for 'Shoes' super class
    def f_specific_use(self):
        print("Football shoes are used in football sports")
        
    def order(self):
        print("Footbal_shoes class's method")
                
#Multiple inheritance
class Sports_shoes(Spike_shoes,Football_shoes):#sub-class has two super-class
    def specific_use(self):
        print("Sports shoes are used in sports activities")
    
    def order(self):
        print("Sports_shoes class's method")
'''    
sports = Sports_shoes()
sports.specific_use()
sports.s_specific_use()
sports.f_specific_use()
sports.order()

s=Shoes()
s.order()

print(Sports_shoes.mro())#mro(): method resolution order, this function tells the order of class so that we can know which method is called first when object is created in case of same method's name.
'''

f =Football_shoes()#2nd level sub-class's object
#an instance is created that is an object of 'Football_shoes' class(sub-class),this sub-class has super-class and this super-class is again a sub-class of another super-class i.e. "Footwear" class.
#So,super-class's attributes are inherited at multi-level and therefore when object of sub class is created,it inherits the 'constructor method' from "Footwear" super class.

s=Shoes() #1st level sub-class's object 

o =Footwear() #super class's object

