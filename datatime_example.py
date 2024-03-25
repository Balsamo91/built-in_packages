"""
Get current dat and time
add or subtract days from the current date
caluclate the difference between dates
format dates into more readable strings
Parse a string to a datetime object
"""

import datetime

# get current date time
now = datetime.datetime.now()
print(f"\nCurrent date and time: {now}\n")
print(type(now)) # the variable now it is an Object

# Add days to the current date
five_days_later = now + datetime.timedelta(days=5)
print(f"\nFive days from now: {five_days_later}")

# Subtract days from current date
five_days_earlier = now - datetime.timedelta(days=5)
print(f"\nFive days from now: {five_days_earlier}")

# Calculate the difference between 2 dates
some_day = datetime.datetime(2023, 1, 1)
difference = now - some_day
print(f"\ndifference since January 1, 2023: {difference.days / 365.25:.2f} years and {difference.days} days.\n")

# Change format into more readable strings ---> Site to check https://www.w3schools.com/python/python_datetime.asp
# strftime ---> String Formatting Time
formatted_date = now.strftime("%A, %B %d, %Y %H:%M:%S")
print(f"Formatted date and time: {formatted_date}\n")

# Parse string to datetime object
# strptime ---> String Parsing Time
date_string = "2024-03-21 12:00:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parese datetime object: {parsed_date}\n")



