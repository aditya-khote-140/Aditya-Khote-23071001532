# Write a program to caught a specific error with a modified error message for user.

try:
    num = int(input("Enter a number: "))
except:
    print(" File /Users/adityakhote/Desktop/Python Repo/File/30.py, line 5 \n\t\texcept \n\t\t\t^ \n\tSyntaxError: expected ':'")
    print("Error: Please enter a valid integer.")


