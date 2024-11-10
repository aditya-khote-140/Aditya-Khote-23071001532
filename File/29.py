'''Write a code to accept two numbers and display the quotient. Appropriate exception
should be raised if the user enters the second number (denominator) as zero (0).'''

a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))

if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", a / b)
