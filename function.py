#************************************************************  function of python ***********************************************************************************

"""
def name():
    print("hello")
    print("I am romeo Advin")
    print("ok by")

name()

for i in range (5):
    name()
"""

#*****************************************************************   NON_PARAMETRIZED   function************************************************************************
"""
def xyz():
    ????
"""

#*****************************************************************   PARAMETRIZED   function ************************************************************************

"""
def xyz(a,b,c):
    ????

"""

#*****************************************************************   formal arguments   function ************************************************************************

"""
def add(a,b):
    print(a+b)
"""
#*****************************************************************   formal arguments   function ************************************************************************
"""
def add(a= int(input("enter the value of a :")),b = int(input("enter the value  of b :"))):
    print(a+b)

add(a,b)
"""
"""
def add(a, b):
    print(a + b)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

add(a,b)
"""

"""
def add(a,b):
    return a+b,a-b,a*b,a/b


print(add(3,4))

"""


"""
def emp(name="hello",eid=112):
    print("name of the employee is : ",name)
    print("eid of the employee is : ",eid)

"""

#emp("qwerty",112)
#emp("xyz",890)
#emp("qwertyy")
#emp(223,"xyz")
#emp("apple",117)

#*****************************************************************   ANONYMOUS   function ************************************************************************

"""
t=lambda a,b:a+b
print(t(5,6))

x=lambda a,b,c:a*b*c
print(x(2,7,3))

"""
"""
n=lambda name:print("Mallika")
n(1)
"""


"""
a=9
b=20
c=30
def f1():
    #global a
    a=100
    print("local : ",a)
    g=globals()
    print("global var : ",g.get("a"))


f1()
print("outside : ",a)

"""


