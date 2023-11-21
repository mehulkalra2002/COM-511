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

def calculator(operator, x, y):
    result = None
    if operator == 1:
        result = add(x, y)
    elif operator == 2:
        result = subtract(x, y)
    elif operator == 3:
        result = multiply(x, y)
    elif operator == 4:
        result = divide(x, y)
    else:
        return "Invalid operator"
    return result

# Display menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Input choice and numbers
choice = int(input("Enter choice (1/2/3/4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation based on choice
result = calculator(choice, num1, num2)
print(f"Result: {result}")
