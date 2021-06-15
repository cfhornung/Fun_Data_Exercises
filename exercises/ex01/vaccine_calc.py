"""A vaccination calculator."""

__author__ = "720053793"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
# Your calculator should prompt the user for the following integer inputs:

# Population - the total number of people under consideration
# Doses administered - the total number of vaccine doses already given to the population 
#   (remember: 2x doses covers 1x person in the population)
# Doses per day - the total number of vaccine doses given each calendar day moving forward 
#   (remember: assume this is constant)
# Target percent vaccinated - an int input, out of 100, that represents the total percent of 
#   population your calculation is targetting (remember: unless doses administered is 0, 
#   some amount of progress toward this target has already been achieved)

# Input prompt
population: int = int(input("Population: "))
doses_ad: float = float(input("Doses administered: "))
# 2 doses = one person vaccinated
doses_ad = doses_ad / 2
doses_day: float = float(input("Doses per day: "))
# 2 doses = one person vaccinated
doses_day = doses_day / 2
target: int = int(input("Target percent vaccinated: "))

# Calculating how many days it would take to reach target percent vaccinated
days: float = float(
    ((target * population / 100) - doses_ad) / doses_day
)
# Now, I need to make sure these days ALWAYS round up, even if it is only 0.1 decimal
# Because, if you don't get to that 0.1% of a person until the next day, it will still take you another day
# to hit that percentage, regardless if they hit more than that targeted percentage later that day.
#  Therefore, I am going to import math and call the ceiling function.
# import math
# days = math.ceil(days)

# Rounding the days
days = round(days)

# Pulling todays date
today: datetime = datetime.today()
# Calculating time delta
time_delta: timedelta = timedelta(days)
# Calculating the date
date: datetime = today + time_delta
# Formatting the date
date_string: str = date.strftime("%B %d, %Y")
#  Print the statement 
print("We will reach {}% vaccination in {} days, which falls on {}." .format(target, days, date_string))
