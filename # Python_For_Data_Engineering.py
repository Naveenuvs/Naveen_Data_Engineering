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

import csv
import json

def csv_to_json(input_csv, output_json):
    with open(input_csv, "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        # Standardize headers
        reader.fieldnames = [
            header.strip().lower().replace(" ", "_")
            for header in reader.fieldnames
        ]

        records = []

        for row in reader:
            clean_row = {}

            for key, value in row.items():
                if value is None or value.strip() == "":
                    clean_row[key] = ""
                else:
                    clean_row[key] = value.strip()

            records.append(clean_row)

    with open(output_json, "w") as json_file:
        json.dump(records, json_file, indent=4)

    print("CSV converted to JSON successfully")


csv_to_json("input.csv", "output.json")

def validate_schema_and_count(records, expected_columns, min_rows=1):
    if len(records) < min_rows:
        raise ValueError("Row count validation failed")

    actual_columns = list(records[0].keys())

    if actual_columns != expected_columns:
        raise ValueError("Schema validation failed")

    return True

import csv
import json
import logging

logging.basicConfig(
    filename="bad_records.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def process_csv(input_csv, output_json, bad_json):
    valid_records = []
    bad_records = []

    with open(input_csv, "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        reader.fieldnames = [
            header.strip().lower().replace(" ", "_")
            for header in reader.fieldnames
        ]

        for row_number, row in enumerate(reader, start=2):
            try:
                clean_row = {}

                for key, value in row.items():
                    clean_row[key] = value.strip() if value else ""

                if clean_row["id"] == "" or clean_row["email"] == "":
                    raise ValueError("Missing required id or email")

                valid_records.append(clean_row)

            except Exception as error:
                row["error"] = str(error)
                bad_records.append(row)
                logging.info(f"Bad row {row_number}: {row}")

    with open(output_json, "w") as file:
        json.dump(valid_records, file, indent=4)

    with open(bad_json, "w") as file:
        json.dump(bad_records, file, indent=4)

    print("Processing completed")


process_csv("input.csv", "output.json", "bad_records.json")

import csv
import json
import logging

# ---------------- Logging Setup ----------------
logging.basicConfig(
    filename="bad_rows.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Vendor Column Mapping ----------------
COLUMN_MAPPING = {
    "product id": "product_id",
    "product_id": "product_id",
    "sku": "product_id",
    "item_id": "product_id",

    "product name": "product_name",
    "name": "product_name",
    "item_name": "product_name",

    "price": "price",
    "cost": "price",
    "amount": "price",

    "category": "category",
    "product_category": "category",

    "description": "description",
    "details": "description",

    "brand": "brand",
    "manufacturer": "brand"
}

REQUIRED_COLUMNS = ["product_id", "product_name", "price"]

DEFAULT_VALUES = {
    "category": "Unknown",
    "description": "",
    "brand": "Generic"
}

FINAL_COLUMNS = [
    "product_id",
    "product_name",
    "price",
    "category",
    "description",
    "brand"
]


# ---------------- Standardize Header ----------------
def standardize_header(header):
    header = header.strip().lower().replace("-", " ").replace("_", " ")
    return COLUMN_MAPPING.get(header, header.replace(" ", "_"))


# ---------------- Validate Row ----------------
def validate_row(row):
    for column in REQUIRED_COLUMNS:
        if column not in row or row[column] == "":
            raise ValueError(f"Missing required field: {column}")

    try:
        row["price"] = float(row["price"])
    except ValueError:
        raise ValueError("Invalid price value")

    return True


# ---------------- Process Single Vendor File ----------------
def process_vendor_file(file_path, seen_products):
    clean_records = []
    bad_records = []

    with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        reader.fieldnames = [
            standardize_header(header)
            for header in reader.fieldnames
        ]

        for row_number, row in enumerate(reader, start=2):
            try:
                clean_row = {}

                for key, value in row.items():
                    clean_row[key] = value.strip() if value else ""

                validate_row(clean_row)

                product_id = clean_row["product_id"]

                if product_id in seen_products:
                    continue

                seen_products.add(product_id)

                for column, default_value in DEFAULT_VALUES.items():
                    if clean_row.get(column, "") == "":
                        clean_row[column] = default_value

                final_row = {
                    column: clean_row.get(column, "")
                    for column in FINAL_COLUMNS
                }

                clean_records.append(final_row)

            except Exception as error:
                row["error"] = str(error)
                row["source_file"] = file_path
                row["row_number"] = row_number
                bad_records.append(row)

                logging.info(f"Bad row in {file_path}, row {row_number}: {row}")

    return clean_records, bad_records


# ---------------- Main Ingestion Utility ----------------
def ingest_product_catalogs(input_files, output_csv, bad_rows_file):
    all_clean_records = []
    all_bad_records = []
    seen_products = set()

    for file_path in input_files:
        clean_records, bad_records = process_vendor_file(
            file_path,
            seen_products
        )

        all_clean_records.extend(clean_records)
        all_bad_records.extend(bad_records)

    with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FINAL_COLUMNS)
        writer.writeheader()
        writer.writerows(all_clean_records)

    with open(bad_rows_file, "w", encoding="utf-8") as json_file:
        json.dump(all_bad_records, json_file, indent=4)

    print("Product catalog ingestion completed")
    print(f"Clean records written to: {output_csv}")
    print(f"Bad rows written to: {bad_rows_file}")
    print(f"Total clean records: {len(all_clean_records)}")
    print(f"Total bad records: {len(all_bad_records)}")


# ---------------- Example Usage ----------------
vendor_files = [
    "vendor1.csv",
    "vendor2.csv",
    "vendor3.csv",
    "vendor4.csv",
    "vendor5.csv"
]

ingest_product_catalogs(
    input_files=vendor_files,
    output_csv="clean_product_catalog.csv",
    bad_rows_file="bad_rows.json"
)

