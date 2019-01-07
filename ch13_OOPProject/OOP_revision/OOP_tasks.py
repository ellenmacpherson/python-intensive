#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:15:36 2019

@author: ellenmacpherson
"""

###########################################################
##### Exercise 1: Defining and initialising a person class
###########################################################

class Person: 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print ('Gender not recognised!')
    #Exercises 2-3: Adding more functionality to the person class with functions.
    def greetingInformal(self):
        print ('Hi', self.name)
        
    def greetingFormal(self):
        if self.isMale:
            print ('Welcome, Mr.', self.name)
        else:
            print ('Welcome, Ms.', self.name)
    def greetingAgeBased(self):
        if self.age < 18: 
            print ('Welcome, young',self.name)
        elif self.age > 60: 
            print ('Welcome, venerable',self.name)
        else: 
            self.greetingFormal()
            
# Creating an Object and printing relevant infomation stored in person class.

p1 = Person('Ellen', 26, 'f')
p2 = Person('Margaret', 67, 'f')
p3 = Person('Tom', 17, 'm')

print (p1.name)
print (p1.isMale)
p1.greetingFormal() #Returns 'Welcome, Ms. Ellen'
p2.greetingAgeBased()
p3.greetingAgeBased()


###########################################################
##### Exercise 4: Creating subclasses
###########################################################

class Wizard(Person): 
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, 'm') #Exercise 5: Redefining init to take values from Person class.
    def greetingFormal(self):
        print ('Welcome,', self.name, end=' ')
        print ('- You\'re a fine wizard!') 
    #Exercise 6: Adding new methods to the Wizard class
    def spell(self):
        print ('Expelliarmus!')

#Creating an object from the Wizard class.        
p4 = Wizard('Harry', 12, 'm')
p5 = Wizard('Hermione', 13, 'f')

p4.greetingFormal()
p5.spell()