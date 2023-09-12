#  addition
def add(x, y):
    return x + y

#  subtraction
def subtract(x, y):
    return x - y

#  multiplication
def multiply(x, y):
    return x * y

#  division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# input of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# list of operations
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# select operation
choice = input("Enter your choice (1/2/3/4): ")

# calculation 
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    result = "Enter the right choice"

print("Result:", result)
