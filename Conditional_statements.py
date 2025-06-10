#=***********************************************************CONDITIONAL STATEMENTS *****************************************************************************
"""

a = int(input("enter the value of a : "))

if a > 5:
     print("hello")
else :
    print("by")

 """


"""
a= int(input("enter the value of a : "))
b= int(input("enter the value of b : "))
if a>b:
     print("greater")
else :
    print("smaller")
              
"""

age= int(input("enter the value of age: "))
#b= int(input("enter the value of b : "))
if age>=18  and age < 60:
     print("he can give the vote ")
elif  age<18  :
    print("he can not give the vote ")
elif age >= 60:
    print("retire")
else :
    print("ok")
