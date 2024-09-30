# -*- coding: utf-8 -*-
"""Copy of Classes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13BJ-8bXMlKJy-RQN3hsSmaa9t4QzE-JO
"""

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  #dunder = double underscore
  def __repr__(self):
    return f"this person's name is {self.name} and his age is {self.age}"
  # def __add__(self, other): # self+other
  #   return self.age + other.age


john = Person("John", 36)
peter = Person("Peter", 30)
print(john + peter)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)

class Dog():
    def __init__(self,name_1,age):
      #self.name is the attribute of name within the dog class
      #name is the parameter that i got in the init function
        self.name = name_1
        self.age = age
    def whats_your_name(self):
        print(self.name)

sally = Dog("Sally",1)
sally.whats_your_name()

spot = Dog("Spot",2)
spot.whats_your_name()

class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

shelter_dog = Dog("Rex")
shelter_dog.walk(10)

class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

    def rename(self, new_name):
        self.name = new_name

shelter_dog = Dog("Rex")
shelter_dog.name = "Paul"

print(shelter_dog.name)

shelter_dog.walk(10)

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)
    def __repr__(self):
        return "This is a computer: {}".format(self.brand)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

windows = Computer()
windows.brand = "Microsoft"
print(windows.brand)

dell_computer = Computer()
dell_computer.brand = "Windows"
Computer.description(dell_computer, "Mark")

# IS THE SAME AS:
dell_computer.description("Mark")

class Dog():

    # Initializer / Instance Attributes
    def __init__(self):
        print("A new dog has been initialized !")

shelter_dog = Dog()

sally = Dog()

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # Attribute: Owner of the account
        self.balance = balance    # Attribute: Current balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"

# Usage
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
account.check_balance()
print(account)

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


sally = BankAccount("123456789")
sally.deposit(100)
sally.deposit(200)
sally.withdraw(50)
sally.view_balance()
sally.view_transactions()

#Inventory management System

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity +=amount

    def calculate_total_value(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

class Inventory:#bananas, peaches, pineapple
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to inventory")

    def remove_item(self,item_name):
        self.items = [item for item in self.items if item.name!=item_name]
        print(f"Removed {item_name} from inventory")

    def get_inventory_value(self):
        values = [item.calculate_total_value() for item in self.items]
        print(f"Inventory Value: {sum(values)}")
        return sum(values)
    def __repr__(self):
        return "\n".join(str(item) for item in self.items)#str(item) is another way to call the repr function within the class

item1 = Item("Bananas", 1, 10)
item2 = Item("Peaches", 2, 5)

inventory = Inventory()
inventory.add_item(item1)
inventory.add_item(item2)
inventory.get_inventory_value()
print(inventory)
inventory.remove_item("Bananas")
inventory.get_inventory_value()
print(inventory)

"""#Hello"""

".".join(["a","b","c"])

class Student:
    def __init__(self, name):
        # Initialize the name and an empty dictionary for grades
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        # Add or update the grade for the given subject
        self.grades[subject] = grade

    def calculate_average(self):
        # Calculate and return the average grade
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        # Return a string representation of the student with their grades
        grades_str = ', '.join(f'{subject}: {grade}' for subject, grade in self.grades.items())
        return f'{self.name} - Grades: {grades_str}'

class Gradebook:
    def __init__(self):
        # Initialize an empty list to hold students
        self.students = []

    def add_student(self, student):
        # Add the student to the gradebook
        self.students.append(student)

    def find_student(self, name):
        # Find and return the student with the given name
        for student in self.students:
            if student.name == name:
                return student
        return f'Student {name} not found in the gradebook.'

    def display_all_students(self):
        # Display the information of all students
        for student in self.students:
            print(student)

# Usage Example
student1 = Student("Alice")
student2 = Student("Bob")

gradebook = Gradebook()
gradebook.add_student(student1)
gradebook.add_student(student2)

student1.add_grade("Math", 90)
student1.add_grade("English", 85)
student2.add_grade("Math", 78)
student2.add_grade("Science", 88)

print(f"{student1.name}'s average grade: {student1.calculate_average()}")
print(f"{student2.name}'s average grade: {student2.calculate_average()}")

gradebook.display_all_students()

def is_empty(lst):
  return not lst

my_list = []
if is_empty(my_list):
  print("The list is empty")
else:
  print("The list is not empty")