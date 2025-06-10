"""

a =1
while a<=10 :
     print("aman",a)
     a += 1
"""


"""
i = 1
while i<=100 :
    print(i)
    i += 1
"""
"""
i= 5
while i>0 :
    print(i)
    i -= 1
"""

"""
i=1
while i<=10:
    print(i*2)
    i += 1
"""


"""
n=int(input("enter the number of the table :"))
i=1
while i<=10:
      print(f"{i} * {n} = {i * n}")
      i += 1

"""

#***************************************************** NESTED WHILE LOOP ************************************************************************************
"""
a =1
while a<=3:
    b=1
    while b < 5:
        print("*", end =" ")
        b = b+ 1
    print()
    a = a+1

"""

"""
row =1
while row<=4:
    col = 1
    while row >= col:
        print("*",end=" ")
        col += 1
    print()
    row +=1
"""

#***************************************************************** FOR LOOP ************************************************************************************
"""
for x in [2,7,1,"abc"]:
    print("xyz",x)
"""

"""
for i in {2,7,7,7,8,3,7}:
    print(i)
"""

"""
for i in (2,7,7,7,8,3,7):
    print(i)
"""


"""
for s in "abc":
    print(s)
"""

"""
emp ={
    1:"aaa",
    2:"bbb",
    3:"ccc"
    }
print(emp.items())
for i,j in emp.items():
    print(i,j)

"""
"""
a= range(1,6,2)
print(a[0],a[1],a[2])

for i in a:
    print(i)
    
"""
"""
for i in range (10):
    print(i)
"""

"""
for i in range(5):
    print("abc",i)

"""

# table generator
"""
n=int(input("enter the value of table :"))
for i in range(0,11):
    print(i*n)
"""

#***************************************************************** NESTED FOR  LOOP ************************************************************************************
"""

for i in range(4):
    print("*",end=" ")

"""

# same thing nested 
"""
for j in range(3):
    for i in range (4):
        print("*",end=" ")
    print()


for row in range(3):
    for col in range(4):
        print("*",end=" ")
    print()
"""


"""
for row in range(1,5):
    for col in range (row):
        print("*",end=" ")
    print()
"""


for row in range(4,0,-1):
    for col in range (row):
        print("*",end=" ")
    print()
