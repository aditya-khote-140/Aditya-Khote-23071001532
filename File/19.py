# 19. Write a Program to remove all occurrences of a specific item from a list.

lst = input("Enter list elements separated by space: ").split()
item = input("Enter the item to remove: ")
result = []

for elem in lst:
    if elem != item:
        result += [elem]

print("Updated list:", result)
