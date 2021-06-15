"""An exercise in remainders and boolean logic."""

__author__ = "720053793"


# # Begin your solution here...
# When evenly divisible by 2, print “TAR”.
# When evenly divisible by 7, print “HEELS”.
# When evenly divisible by both 2 and 7, print “TAR HEELS” instead of just “TAR” or “HEELS”
# When none of the above conditions are met, print “CAROLINA”

number: int = int(input("Enter an int: "))

if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
elif number % 2 == 0:
    print("TAR")
elif number % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")
