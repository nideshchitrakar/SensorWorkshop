#! /usr/bin/env python3
"""
    problem_2.py - a simple program containing simple string functions
    Author: nideshchitrakar
    Date: 05/05/18
"""

# return grand total of ascii values of characters in a string
def get_ascii_total(string):
    total = 0
    for char in string:
        total += ord(char)
    return total


if __name__ == "__main__":
    print("ASCII total of \"{0}\" is {1}.".format('A', get_ascii_total('A')))
    print("ASCII total of \"{0}\" is {1}.".format('abcde', get_ascii_total('abcde')))