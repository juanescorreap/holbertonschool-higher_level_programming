#!/usr/bin/python3
import random
from typing import AbstractSet
number = random.randint(-10000, 10000)
abs = abs(number)
if number % 10 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(
        number, abs % 10))
elif number % 10 == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, abs % 10))
elif number % 10 < 6 and number % 10 != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(
        number, abs % 10))
