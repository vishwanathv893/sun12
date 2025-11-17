'''
Created on 05-Nov-2025

@author: vishw
'''
print("Keyword variable Length argument :-")

def keyword_len_add(**a):                    
    return a
    
g_num=keyword_len_add(a=1,b=2,c=3) 
print("g_num:",g_num)  

def var_len(*a): # variable length arguments
    print(a)
var_len(4,7,9,12)
#print("sum_of:",sum_of)

