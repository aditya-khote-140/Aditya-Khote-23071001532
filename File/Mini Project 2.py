# Mini Project- create a password Generator.

import random

# Simple sets of characters to choose from
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Ask the user for password length
length = int(input("Enter the password length: "))

# Generate a password by randomly selecting characters
password = ""
for _ in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
