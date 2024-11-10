# 13. Write a program to convert decimal number to binary number.

number = int(input("Enter a decimal number: "))
binary = ""
n = number

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print("Binary representation:", binary)
