#  TAKE A INPUT FROM USER AND AND FIND THE SUM OF DIGITS IN THE NUMBER 

num = input("Enter a number: ")
sumof = 0

for i in num:
    sumof += int(i)

print("Sum of digits:", sumof)


# a=int(input("Enter Range :-  "))
# sum=0
# if a > 0:
#  for i in range (a):
#     num = int(input("Enter Number : "))
#     sum += num
#  print("Sum of digit :- ",sum)
# else:
#  print("Enter invalid number")
