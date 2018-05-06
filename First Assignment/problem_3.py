#! /usr/bin/env python3
"""
    problem_3.py - a simple program that checks if user's guess matches the string length
    Author: nideshchitrakar
    Date: 05/05/18
"""

# checks if user's length guess matches the string's length
def length_guesser(my_string, my_length_guess):
    difference = len(my_string) - my_length_guess   # calculate how much the guess is off from actual length

    # check if guess is correct or not
    if difference == 0:
        return 0    # return 0 if guess is correct
    elif difference > 0:
        return 1    # return 1 if guess is short
    else:
        return -1   # return -1 is guess is bigger


if __name__ == "__main__":
    print("String: \"{0}\", Guess: {1}, Result: {2}".format("hello", 5, length_guesser("hello",5)))
    print("String: \"{0}\", Guess: {1}, Result: {2}".format("hello world", 5, length_guesser("hello world", 10)))
    print("String: \"{0}\", Guess: {1}, Result: {2}".format("hello darkness my old friend", 5, length_guesser("hello", 50)))