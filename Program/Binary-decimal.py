# CONVERT DECIMAL TO BINARY
'''
Steps:
	1.	Get a decimal number from the user.
	2.	Convert it to binary.
'''
decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)[2:]

print("Binary:", binary)