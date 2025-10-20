'''
Created on 20-Oct-2025

@author: vishw

Accept marks from a student and display the grade based on the following:

   * 90 and above → A+
   * 80–89 → A
   * 70–79 → B
   * Below 70 → C

'''
print("Displaying the grade of the student :-")
grade=input("Enter the marks :")
g1 = int(grade)
if g1>=90 :
    print("Your grade is 'A+'.")
elif 80<=g1<=89:
    print("Your grade is 'A'.")
elif 70<=g1<=79:
    print("Your grade is 'B'.")
else:
    print("Your grade is 'C'.")

