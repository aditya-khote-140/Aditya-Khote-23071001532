#  TAKE A INPUT FROM USER AND AND FIND THE SUM OF DIGITS IN THE NUMBER 

num = input("Enter a number: ")
sum_of_digit = 0

for digit in num:
    sum_of_digit += int(digit)

print("Sum of digits:", sum_of_digit)