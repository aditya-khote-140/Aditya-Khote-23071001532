# Write a program to take input from the user and print Quotient and reminder.
# Take input from the user
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

quotient = dividend // divisor
remainder = dividend % divisor

print("Quotient:", quotient)
print("Remainder:", remainder)
