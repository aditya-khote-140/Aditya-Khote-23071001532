# 16. Write a program to take two list by using input function and find the sum of list.

list1 = input("Enter elements of list 1 separated by space: ").split()
list2 = input("Enter elements of list 2 separated by space: ").split()

sum1 = 0
for num in list1:
    sum1 += int(num)

sum2 = 0
for num in list2:
    sum2 += int(num)

print("Sum of lists:", sum1 + sum2)
