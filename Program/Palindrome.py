''' PALINDROME NUMBER
-->COUNT THE NUMBER OF DIGITS
-->PRINT THE REVERSE OF NUMBER
-->CHECK NUMBER IS PALINDROME NUMBER
'''

# Taking input
num = int(input("Enter a number: "))

num_digits = len(str(num))

reversed_num = 0
temp_num = num

# Loop chalu

while temp_num > 0:
    last_digit = temp_num % 10
    reversed_num = reversed_num * 10 + last_digit
    temp_num = temp_num // 10

if num == reversed_num:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")

print("Number of digits:", num_digits)

print("Reversed number:", reversed_num)