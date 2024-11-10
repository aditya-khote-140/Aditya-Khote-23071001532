# 17. Write a program to find the maximum and minimum value in the list taken by the user.

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    # Update max_value  
    if num > max_value:
        max_value = num
    # Update min_value 
    if num < min_value:
        min_value = num

print("Maximum value:", max_value)
print("Minimum value:", min_value)

