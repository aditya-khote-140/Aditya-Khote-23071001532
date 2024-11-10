# 25. Write a program to print your age by using datetime module.

from datetime import datetime

birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year
age = current_year - birth_year

print("Your age:", age)


# from datetime import datetime

# birth_year = int(input("Enter your birth year: "))
# current_year = datetime.now().year
# print("Your age:", current_year - birth_year)
