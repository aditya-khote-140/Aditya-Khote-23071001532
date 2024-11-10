# 18. Write a Program to Perform Liner Search on the list of number taken by the user.

list = input("Enter list elements separated by space: ").split()
target = input("Enter the number to search: ")
found = -1

for index in range(len(list)):
    if list[index] == target:
        found = index
        break

print("Element found at index:" if found != -1 else "Element not found",found)
