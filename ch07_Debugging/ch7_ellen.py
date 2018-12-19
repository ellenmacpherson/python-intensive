#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:44:08 2018

@author: ellenmacpherson
"""
#Code for debugging.

user_input = input('Please give a number: ')

def simpleOperation(user_input):
    intInput = int(user_input)
    result = intInput - 2
    return result

def nestedOperation(result):
    result = simpleOperation(user_input)
    result2 = result + 2
    return result2

result = simpleOperation(user_input)
result2 = nestedOperation(result)
print (result2)


"""
Use the print function! You can keep track of how your code is running and spot any errors as they happen.

A breakpoint is an intentional stopping or pausing place in a program, put in place for debugging purposes.

Debug mode:
- First button runs code until break point
- Second button runs code line by line until breakpoint
- Third button is for stepping into sections where you want to see deeper into what's going on. e.g. classes and functions
- Fourth button allows you to go to the next breakpoint if you have multiple
- Last button is the stop button. Exits debugging mode.

"""
