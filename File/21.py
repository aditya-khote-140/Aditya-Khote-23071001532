''' Write a program to perform following action the predefined dictionary.
- Access the third element of dictionary
- Update the fourth index value in the dictionary
- Add a new item in the dictionary. '''

d = [['one', 1], ['two', 2], ['three', 3], ['four', 4]]

# Access third element
print("Third element:", d[2][1])

# Update the fourth index value
d[3][1] = 40
print("Updated dictionary:", d)

# Add a new item
d += [['five', 5]]
print("Dictionary after adding new item:", d)
