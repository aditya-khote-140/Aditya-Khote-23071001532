# 17. Write a program to find the maximum and minimum value in the list taken by the user.

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

max = numbers[0]
min = numbers[0]

for num in numbers:
    # Update max_value  
    if num > max:
        max = num
    # Update min_value 
    if num < min:
        min = num

print("Maximum value:", max)
print("Minimum value:", min)

