'''
Created on 09-Nov-2025

@author: vishw

naming convention for defining a class name :a naming convention in programming where every word in a compound identifier begins with a capital letter, 
and the words are joined together without spaces or underscores


# self :a reference (a pointer) to the object that’s calling the method
'''
class DogClass:
     
    def __init__(self,name,color,gender,breed):#initialised ,constructor(method):used to construct a special(magic) method  to define properties or features
        self.name=name # self :a reference (a pointer) to the object that’s calling the method
        self.color =color#attributes,  "self" is used to store the given color in the object's own variable
        self.gender =gender
        self.breed=breed
        print(f"A dog having name :{name},color:{color},gender:{gender},breed:{breed} is  created.")#string formatting
     
    def bark(self):#defining a function which is called as 'method'
        print(f"{self.name} is barking.")     
        

d=DogClass('bug','blue','putt',"v")
f=DogClass('a',"b","c","d")
f.bark()

    
'''
puppy=DogClass("puppy","white","Male","Husky") #Creating an instance of  class i.e. an object
puppy.bark()#calling a function from DogClass  
print(type(puppy)) #<class '__main__.DogClass'>
 
kariya=DogClass("kariya","black","male","native")   
kariya.bark() 


print(puppy.name)   #self is replaced by puppy while calling a  constructor method
print(dir(puppy)) #python creates magic methods for backend activity

class Cryons:
    def __init__(self,color):
        self.color=color
        print(f"This is {color} Cryon.")
    def fill(self):
        print(f"The {self.color} cryon fills {self.color}.") 


a1=Cryons("blue")
a1.fill()  
'''
        
    
    
