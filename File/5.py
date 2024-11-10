''' Write a program to calculate all the arithmetic operations on the different numeric data
type and show their results along with their error (if any exist). '''

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    # arithmetic operations
    c = a + b
    print("Addition (+):", c)

    c = a - b
    print("Subtraction (-):", c)

    c = a * b
    print("Multiplication (*):", c)

    # Modulus operation (error if b is 0)
    c = a % b
    print("Modulus (%):", c)

    # Floor division (error if b is 0)
    c = a // b
    print("Floor Division (//):", c)

    # Division (error if b is 0)
    c = a / b
    print("Division (/):", c)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric values.")