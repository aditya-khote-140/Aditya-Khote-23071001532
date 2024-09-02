# SUM OF POSTIVE AND NEGATIVE NUMBER

numbers = input("Enter numbers With space: ").split()

''' Split () function '''
''' •   split() breaks up a string into a list of words.
'''

positive_sum = 0
negative_sum = 0

for num in numbers:
    num = int(num)
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num

print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)