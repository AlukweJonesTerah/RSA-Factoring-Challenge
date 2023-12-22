#!/usr/bin/python3
"""
This module is used to factorie numbers
"""
from sys import argv

def factorize(value):
    """
    function that factors numbers
    :param value: print a simple decomposition of an integer > 1."
    :return:
    """
    i = 2

    if value < 2:
        return

    print()
    print(value, "<- value-bef")

    while value % i:
        i += 1

    print("{:.0f}={:.0f}*{:.0f}".format(value, value / i, i))
    print(value, "<- value-aft")
    print()

if len(argv) != 2:
    exit("Usage: {} ".format(argv[0]))

try:
    with open(argv[1]) as file:
        for line in file:
            value = int(line.strip())
            factorize(value)
except FileNotFoundError:
    exit("File not found: {}".format(argv[1]))
except Exception as e:
    exit("An error occurred: {}".format(e))
