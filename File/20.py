# 20. Write a program to take an input from user, store in dictionary and print the result.

n = int(input("How many entries do you want to add? "))
user_dict = []

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict += [[key, value]]

print("Dictionary:", user_dict)
