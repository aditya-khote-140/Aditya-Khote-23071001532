# 28. Write a program to print year is leap or not and the leap days between 1950 and 2000.

start_year = 1950
end_year = 2000
leap_days = 0

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_days += 1

print("Leap days between 1950 and 2000:", leap_days)
