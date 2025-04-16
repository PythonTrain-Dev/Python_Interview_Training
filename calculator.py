Readme_Data:

Requirements:

Create a basic calculator with the following operations:

Addition

Subtraction

Multiplication

Division

Take user input for two numbers and the operation.

Display the result.


# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Select operation: +, -, *, /")
operation = input("Enter operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == '+':
    print("Result:", add(a, b))
elif operation == '-':
    print("Result:", subtract(a, b))
elif operation == '*':
    print("Result:", multiply(a, b))
elif operation == '/':
    print("Result:", divide(a, b))
else:
    print("Invalid operation")

  
