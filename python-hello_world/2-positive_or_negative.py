#!/usr/bin/python3
import random
number = random.randint (-10, 10)

# Code checking wether a number is positive or negative
if number > 0:
    print ('{:d} is positive' .format (number))
elif number == 0:
    print ('{:d} is zero' .format (number))
elif number < 0:
    print ('{:d} is negative' .format (number))
