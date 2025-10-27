'''
Created on 25-Oct-2025
loop Control statements:
1.break - stop in-between within in the loop execution.Used after print() statement.
2.continue - skips the execution of statements in a loop available after continue statement. used before 'print()statment.


@author: vishw
'''
'''  

for i in range(1,100):
    if i == 50:
        continue  
    print(i)
    
    '''
    
#infinite loop is created thats why program is not terminated and its not showing in the console 
num =1    
while num <100:
    if num==50:
        num+=1
        continue
    print(num)
    num+=1

    