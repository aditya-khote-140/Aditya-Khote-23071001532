# 14. Write a program to check string is palindrome or not.

string = input("Enter a string: ")
is_palindrome = True

for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        is_palindrome = False
        break

print("Palindrome" if is_palindrome else "Not a palindrome")
