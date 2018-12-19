#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:58:32 2018

@author: ellenmacpherson
"""
#Working with imported functions.

#Importing functions from external files. 
from ch3file1_ellen_function import * 


#Exploring what you can do with the input function
name = input('What\'s your name? ')
print ('Hello {}!'.format(name.title())) #Prints 'Hello Name' to console. .title ensures the first letter of name is capitalised.

age = input('How old are you? ')
print ('You\'re {}. Thanks for letting us know!'.format(age))

homeCountry = input('Where are you from? ')
print ('You\'re from {}? Wow!'.format(homeCountry.title()))


#Calling functions and user input

helloWorld()

#Task 5
centigrade = int(input('Temperature in centigrade: '))

temperature_conversion(centigrade)
kelvin_converter(centigrade)
