# Variables
name = "Naveen"
age = 28
salary = 75000.50
is_active = True

# Data types
print(type(name))      
print(type(age))       
print(type(salary))    
print(type(is_active)) 

# Operators
a = 10
b = 3

print(a + b)   
print(a - b)   
print(a * b)   
print(a / b)   
print(a // b)  
print(a % b)   
print(a ** b)  

# Comparison operators
print(a > b)
print(a == b)
print(a != b)

# Logical operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)

# Conditionals
score = 85

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")

# Loops
for i in range(5):
    print("For loop:", i)

count = 0
while count < 3:
    print("While loop:", count)
    count += 1

# Functions
def greet(user_name: str) -> str:
    return f"Hello, {user_name}!"

def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

print(greet("Venkat"))
print(add_numbers(10, 20))

# List
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)
print(fruits[0])

# Dictionary
student = {
    "name": "Venkat",
    "age": 28,
    "skill": "Python"
}
print(student["name"])
student["age"] = 29
print(student)

# Tuple
coordinates = (10.5, 20.8)
print(coordinates[0])

# Set
numbers = {1, 2, 2, 3, 4, 4}
print(set(numbers))  # duplicates removed

# List comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# oop_basics.py

class Employee:
    def __init__(self, name: str, role: str, salary: float) -> None:
        self.name = name
        self.role = role
        self.salary = salary

    def display_info(self) -> None:
        print(f"Name: {self.name}, Role: {self.role}, Salary: {self.salary}")

    def give_bonus(self, amount: float) -> None:
        self.salary += amount

# Create object
emp1 = Employee("Venkat", "Data Engineer", 90000)
emp1.display_info()

emp1.give_bonus(5000)
emp1.display_info()

