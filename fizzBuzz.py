#!usr/bin/env python
"""
fizzBuzz.py
"""

for i in range(1, 101):
    if i%15    == 0:
        print("Fizz Buzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

