# Write a program to take input from the user and check number is divisible by 2 or 8.

number = float(input("Enter a number "))
if number % 2 == 0:
    print("Number is divisible by 2")  
elif number % 8 == 0:
    print("Number is divisible by 8")
else:
    print("Number is not divisible by 2 and 8")