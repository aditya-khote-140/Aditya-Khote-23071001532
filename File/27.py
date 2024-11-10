'''Write a program to Display the Calendar of a given month, Display calendar of the
given year.'''
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
print("Calendar for month:", month, "Year:", year)
print(calendar.month(year, month))
print("Calendar for the year:")
print(calendar.calendar(year))
