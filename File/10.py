# Write a program print a table of 5.32 with formatting up to 2 decimal places.

number = float(input("Enter any float number for multiplication table : "))

print("Multiplication Table of", number)
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result:.2f}")
