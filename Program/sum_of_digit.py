#  TAKE A INPUT FROM USER AND AND FIND THE SUM OF DIGITS IN THE NUMBER 

# num = input("Enter a number: ")
# sum_of_digit = 0

# for i in num:
#     sum_of_digit += int(i)

# print("Sum of digits:", sum_of_digit)

a=int(input("Enter Range : - "))
sum=0
for i in range (a):
    num = int(input("Enter Number : "))
    sum += num
print("Sum of digit :- ",sum)