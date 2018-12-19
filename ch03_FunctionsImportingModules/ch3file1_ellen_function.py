#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:21:10 2018

@author: ellenmacpherson
"""
###############################################################################
######################### Basic functions ################################
###############################################################################

def birthday_message_2args(a, b):
    print('{} {}'.format(a, b))

def hello_world_4args(a, b, c, d):
    print ('{} {} {} {}'.format(a, b, c, d))
    
def addition(): #Adds 2+2
    four = 2 + 2
    print ('Your fun fact for today is...\n2 + 2 is {}!'.format(four))
    
def add_two_numbers(n1, n2):
    answer = n1 + n2
    return (str(n1) + ' plus ' + str(n2) + ' is ' + str(answer))

###############################################################################
######################### Converting functions ################################
###############################################################################

def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    return ('{} miles is equal {} kilometers.'.format(miles, kilometers))


def kelvin_converter(centigrade):
    kelvin = centigrade + 273.15

    return kelvin

def fahrenheit_converter(centigrade):
     fahrenheit = (centigrade * 9.0) / 5.0 + 32

     return fahrenheit

def temperature_conversion(centigrade):
    kelvin1 = kelvin_converter(centigrade)
    fahrenheit = ((kelvin1 * 9) / 5) - 459.67
    return ('{} degrees is equal to {} degrees in kelvin and {} degrees in fahrenheit.'.format(centigrade, kelvin1, fahrenheit))

###############################################################################
######################### Functions with Input ################################
###############################################################################


def printName(): #Asks for name input, then prints name in title format and 'fun fact' addition function.
    name = input('Enter your name: ')
    print('Hello {} \n'.format(name.title()))
    addition()

def mathsInputs(): #Asks for the user to input two separate numbers, then multiplies them.
    firstInputNumber = input('Want more maths? Enter a number here: ')
    secondInputNumber = input('Now enter a second number: ')
    result = (int(firstInputNumber) * int(secondInputNumber))
    print ('\nYour numbers multiplied to make {}!'.format(result))


def helloWorld(): #Prints hello world and combines all above functions. Call this one for full functionality!
    print('\nHello world!'.title())
    printName()
    mathsInputs()