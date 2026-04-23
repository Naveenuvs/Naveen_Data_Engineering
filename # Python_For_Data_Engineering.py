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

# file_handling.py

# Writing to a file
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python file handling is easy.\n")

# Reading from a file
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
import csv

# Data to write
rows = [
    ["id", "name", "department"],
    [1, "Venkat", "Data Engineering"],
    [2, "Naveen", "Backend"],
    [3, "Arjun", "Analytics"]
]

# Write CSV
with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Read CSV
with open("employees.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# csv_dict_example.py

import csv

data = [
    {"id": 1, "name": "Venkat", "skill": "Python"},
    {"id": 2, "name": "Naveen", "skill": "SQL"}
]

# Write
with open("users.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["id", "name", "skill"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Read
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["skill"])

# json_handling.py

import json

employee = {
    "id": 101,
    "name": "Venkat",
    "role": "Data Engineer",
    "skills": ["Python", "SQL", "AWS"]
}

# Write JSON
with open("employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)

# Read JSON
with open("employee.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)
    print(data["name"])
    print(data["skills"])

    # exception_handling.py

def divide_numbers(a: float, b: float) -> float:
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return 0
    except TypeError:
        print("Error: Invalid input type.")
        return 0
    finally:
        print("Execution completed.")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
class InvalidAgeError(Exception):
    pass

def check_age(age: int) -> None:
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    print("Eligible")

try:
    check_age(16)
except InvalidAgeError as error:
    print("Caught custom exception:", error)
# logging_basics.py

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is a debug message")
logging.info("Script started")
logging.warning("This is a warning")
logging.error("This is an error message")
logging.critical("Critical issue occurred")

# logging_basics.py

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is a debug message")
logging.info("Script started")
logging.warning("This is a warning")
logging.error("This is an error message")
logging.critical("Critical issue occurred")
# Logging in functions
# Python


# Run
# logging_example.py

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_file(filename: str) -> None:
    logging.info("Processing file: %s", filename)
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            logging.info("File content length: %d", len(content))
    except FileNotFoundError:
        logging.error("File not found: %s", filename)

process_file("sample.txt")
process_file("missing.txt")

