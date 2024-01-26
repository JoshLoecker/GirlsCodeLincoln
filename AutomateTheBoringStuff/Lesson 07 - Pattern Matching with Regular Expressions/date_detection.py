"""
Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it’ll have a leading zero (i.e., January is ‘01’).

The regular expression doesn’t have to detect correct days for each month or for leap years
it will accept nonexistent dates like 31/02/2020 or 31/04/2021

Store these strings into variables named month, day, and year

Write additional code that can detect if it is a valid date
April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days.
February has 29 days in leap years
    Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400

Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
"""

import re

input_date = input("Enter a date in the format DD/MM/YYYY: ")

date_search = re.search(r"(\d\d)/(\d\d)/(\d\d\d\d)", input_date)
while len(date_search.groups()) != 3:
    input_date = input("Enter a date in the format DD/MM/YYYY: ")
    date_search = re.search(r"(\d\d)/(\d\d)/(\d\d\d\d)", input_date)

day = int(date_search.group(1))
month = int(date_search.group(2))
year = int(date_search.group(3))

if month in [4, 6, 9, 11]:
    if day > 30:
        print("Invalid date")
elif month == 2:
    if year % 4 == 0:
        if day > 29:
            print("Invalid date")
    else:
        if day > 28:
            print("Invalid date")
else:
    if day > 31:
        print("Invalid date")
