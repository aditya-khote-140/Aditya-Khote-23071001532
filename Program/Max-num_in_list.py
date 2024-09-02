# MAXIMUM NUMBER IN THE INPUT VALUE (FOR ANY TYPE OF VALUE) :
'''
Steps:
	1.	Get a list of numbers from the user.
	2.	Find the biggest number.
'''

numbers = input("Enter numbers separated by space: ").split()

numbers = [int(num) for num in numbers]

max_value = max(numbers)

print("Maximum value:", max_value)