# 🧮 Function-Based Calculator


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"
def calculator():
    print(" Welcome to Dhavasidharan's Function Calculator")
    print("Choose operation: add,sub,mul,div")
    op = input("Enter operator: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if op == 'add':
        result = add(a, b)
    elif op == 'sub':
        result = subtract(a, b)
    elif op == 'mul':
        result = multiply(a, b)
    elif op == 'div':
        result = divide(a, b)
    else:
        result = "Invalid operator!"
    print(f"Result: {result}")
calculator()