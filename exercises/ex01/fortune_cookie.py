"""Program that outputs one of at least four random, good fortunes."""

__author__ = "720053793"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# # Begin your solution here...
# # This is what I would do if I wasn't given specific instructions on using if....
# cookie = ["A beautiful, smart, and loving person will be coming into your life",\
#     "A dubious friend may be an enemy in camouflage.",\
#     "A faithful friend is a strong defense.",\
#     "A feather in the hand is better than a bird in the air.",\
#     "A fresh start will put you on your way.",\
#     "A friend asks only for your time not your money",\
#     "A friend is a present you give yourself.",\
#     "A gambler not only will lose what he has, but also will lose what he doesn’t have.",\
#     "A golden egg of opportunity falls into your lap this month.",\
#     "A good friendship is often more important than a passionate romance."]

# print("Your fortune cookie says...\n{}\nNow, go spread positive vibes!" .format(cookie[randint(0,9)]))
# print()
# print()


# However, I know you guys want to see if I can use if statements....
fortune = randint(1, 4)
# print("Your fortune cookie says...")
# if fortune == 1:
#     print("Be careful or you could fall for some tricks today.")
# elif fortune == 2:
#     print("Beauty in its various forms appeals to you.")
# elif fortune == 3:
#     print("Believe in yourself and others will too.")
# elif fortune == 4:
#     print("Change is happening in your life, so go with the flow!")
# print("Now, go spread positive vibes!")
# print()
# print()


# or NESTED if statements would look like...
print("Your fortune cookie says...")
if fortune == 1:
    print("Be careful or you could fall for some tricks today.")
else:
    if fortune == 2:
        print("Beauty in its various forms appeals to you.")
    else:
        if fortune == 3:
            print("Believe in yourself and others will too.")
        else:
            print("Change is happening in your life, so go with the flow!")

print("Now, go spread positive vibes!")