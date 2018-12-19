#!usr/bin/env python3
#-*- coding: utf-8 -*-
"""
Created on Thu Nov 20 11:04:06 2018

@author: ellenmacpherson
"""
#The above is ignored by Python, but will be read by other languages and programs to read the following code as Python. Makes code more universal.

#-------------------------------PYTHON DAY 2-----------------------------------

#Simple Python calculations to get used to coding.
a = 5 - 6
b = 8 * 9
c = 6 / 2
d = 5 / 2
e = 5.0 / 2
f = 5 % 2
g = 2 * (10 + 3)
h = 2 ** 4

#age = 5
#age = 'almost three'
#age = 29.5
#age = 'I really don\'t know' #Backslash

#Assigning different data types to variables to test errors and learn how to repeat lines.
S1 = ('hello ' + 'world')
S2 = ('Joke ' * 3)
S3 = (str(5)) #Converts the integer 5 into a string.
S4 = ('hello'.upper()) #Converts string in upper case.
S5 = ('GOODBYE'.lower()) #Converts string in lower case.
S6 = ('the lord of the rings'.title()) #Converts string with capitalised letters at the beginning of each word.
S7 = ('\n') #New line break. Can be used mid-string to break up display of strings. See below.
S8 = ('Sorry for being late! \n' * 100) #Will print 'Sorry for being late!' 100 times.

#Converting data types
s1 = '4'
s2 = '6'
s3 = 8
result = (int(s1) + int(s2) + s3)

#Splitting strings
strExample = 'a b c d e f'
SplitStr = (strExample.split(' '))

#Formatting string variables.
age = 5
like = 'painting'

age_description = 'My age is {} and I like {}'.format(age, like) #Converts all variable data types to strings.

print(age_description)

#Alternate approach to printing a variable across multiple lines - not using a line break.
test = ("""Sorry for being late!
""" * 100)

print (test)
