#! /usr/bin/env python3
"""
    problem_1.py - a simple program containing simple arithmetic functions
    Author: nideshchitrakar
    Date: 05/05/18
"""

# return sum of two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

# return difference between two numbers
def subtract_two_numbers(num1, num2):
    return num1 - num2

# multiply two numbers through addition
def multiply(num, times):
    number = 0
    for i in range(0, times):
        number = add_two_numbers(number, num)
    return number

# division via repeated subtraction
def divide(num, factor):
    quotient = 0
    remainder = 0
    while num - factor >= 0:
        num = subtract_two_numbers(num, factor)
        quotient += 1
        remainder = num
    return quotient,remainder


if __name__ == "__main__":
    print("The sum of 3 and 4 is {0}.".format(add_two_numbers(3,4)))
    print("The difference between 10 and 6 is {0}.".format(subtract_two_numbers(10,6)))
    print("The product of 5 and 3 is {0}.".format(multiply(5,3)))
    division_result = divide(21,4)
    print("When 21 is divided by 4, quotient is {0} and remainder is {1}.".format(division_result[0],division_result[1]))