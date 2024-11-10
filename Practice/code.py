# # L = [8, 9, 10, 11, 23]
# # L[1] = 17

# # L.extend([4, 5, 6])
# # L.pop(0)
# L = [x**2 for x in range(10)]


# print(L)


x = ['3', '2', '5']
y = ''
while x:
    y += x[-1]  # Append last element of x to y
    x = x[:-1]  # Remove last element from x
print(x)  # Output: []
print(y)  # Output: '523'
print(type(x), type(y))  # Output: (<class 'list'>, <class 'str'>)
