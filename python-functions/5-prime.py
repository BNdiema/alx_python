#!/usr/bin/python3

#Prime Number Function

def is_prime(number):
    if number < 2:
        return(False)
    elif number == 2:
        return(True)
    elif number % 2 == 0:
        return(False)
    else:
        for i in range(3, number, 2):
            if number % i != 0:
                return(True)
            return(False)