# 12. Write a program to find maximum number in the input value (for any type of value).

values = input("Enter numbers separated by space: ").split()
max_val = float(values[0])

for val in values:
    num = float(val)
    if num > max_val:
        max_val = num

print("Maximum value:", max_val)
