# 24. Write a program to implemented calculator using module.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

if operation == 'add':
    result = a + b
elif operation == 'subtract':
    result = a - b
elif operation == 'multiply':
    result = a * b
elif operation == 'divide' and b != 0:
    result = a // b
else:
    result = "Invalid operation or division by zero."

print("Result:", result)
