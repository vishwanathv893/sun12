'''
OOPS : Object Oriented programming systems
'''
print("Welcome to OOPs")

class algebra_formulas():
    def __init__(self):#constructor method
        greeting ="Hey try out these algebraic methods:"
        print(greeting)
    
    def a_plus_b_whole_square(self,a,b):#call using print function
        r1 = a*a 
        r2 = 2*a*b 
        r3 = b*b
        result = r1+r2+r3 
        return result #giving something

    def x_minus_y_whole_square(self,x,y):#just call it
        s1 = x*x
        s2 = 2*x*y
        s3 = y*y
        solution =s1-s2+s3
        print(solution)#function is itself is showing the result , so it returns 'None'
'''
a,b = input("Enter the value for a and b to perform (a+b)^2 :")
a =int(a)
b=int(b)
#print(a_plus_b_whole_square(a,b))#showing using print function


x =int(input("Enter the value for x :"))
y =int(input("Enter the value for y :"))



x_minus_y_whole_square(x,y) #just call the function with valid arguments to see the output
'''
        
g =algebra_formulas()
print(g.a_plus_b_whole_square(4, 6))
g.x_minus_y_whole_square(5, 2)










    