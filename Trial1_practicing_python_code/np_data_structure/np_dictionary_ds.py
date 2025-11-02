'''
Created on 01-Nov-2025

@author: vishw
'''
dict1 ={1:'car',2:'bike',2:"baloon",3:"tree",4:"bag"}
print(dict1)
dict2 =dict(a="apple",b="ball",c="ball")
print(dict2)
print(dict1[1])# accessing using key inside the square brackets

for i in dict1:# only key is printing not the values associated with it.
    print(i)
    
for j in dict1:
    print(j,dict1[j])
    
dict2['d']="deer"
print(dict2)
    
dict3={5:"fire"}
print(dict2)

    
        




