#************************************************************************** CONCEPTS OF OOPS ************************************************************************
"""
class Student:
    # Parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student to database:")

# Creating student objects
s1 = Student("Aman", 97)
print(s1.name, s1.marks)

s2 = Student("Romeo", 96)
print(s2.name, s2.marks)

"""
#************************************************************************** CONCEPTS OF OOPS ************************************************************************

# create students class that takes name & marks of 3 subjects as arguments in constructor . Then, create a methods to print the average.
"""
class student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is:",sum/3)


s1 = student("Advin",[99,98,96])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()

"""
#************************************************************************** CONCEPTS OF OOPS ************************************************************************

#CREATE ACCOUNT CLASS WITH 2-ATTRIBUTES BALANCE & ACCOUNTS NUMBER
#CREATE METHODS FOR DEBIT , CREDIT, & PRINTING THE BALANCE

class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.acc = acc

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance =", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_balance())

    # Method to get current balance
    def get_balance(self):
        return self.balance

# Example usage:
a1 = Account(10000, "ACC123")
a1.debit(1000)
a1.credit(500)
a1.credit(40000)
a1.debit(1000)
