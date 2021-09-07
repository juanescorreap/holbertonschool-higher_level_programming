#!/usr/bin/python3
import random
from typing import AbstractSet
number = random.randint(-10000, 10000)
if number < 0:
    x = -10
else:
    x = 10
if number % x > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, number % x))
elif number % x == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, number % x))
elif number % x < 6 and number % x != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, number % x))
