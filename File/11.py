'''Write a program to sum the number provided by user (number can be positive or
negative)'''

sum = 0
print("Enter numbers to sum. Enter 0 to stop.")

while True:
    number = float(input("Enter a number: "))
    if number == 0:
        break
    sum += number

print("The sum of the numbers is:", sum)
