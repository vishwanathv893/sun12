'''
Created on 05-Nov-2025

@author: vishw
'''

print("A function which takes 'double astric variable' as a parameter returns the output in dictionary data structure")
def double_astric_argument(**a):                    
    return a #while calling a function "keyword argument" shoud be given as parameter
    
g_num=double_astric_argument(apple=1,ball=2,cap=3) 
print("g_num:",g_num)  
print(type(g_num))



print()
print("A function which has 'single astric variable' as argument returns the output in tuple data structure")
def single_astric_argument(*a): # variable length arguments
    #print(a)
    return a #while calling this function "positional argument" should be given as parameter
s=single_astric_argument("apple","ball")
print(s)
print(type(s))
print(s[0])
#print("sum_of:",sum_of)
