#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:46:59 2018

@author: ellenmacpherson
"""




""" Dictionaries are the most powerful data type in Python """

#Demonstrating the syntax of a dictionary
a = {'key1': 'value1', 'key2': 'value2'}

print (a['key1']) # Returns 'value1'

# Assigning a value to a new key
a['key3'] = 'value3'
print (a)

a['key4'] = 'value4'
print (a)


"""-------------------Creating new dictionary--------------------"""
salary = {'JS': 70000, 'JM': 50000, 'RW:': 90000}
print (salary)

"""-------------------Adding new item to dictionary--------------------"""
salary['MM'] = 35000
print (salary)

"""-------------------Adding new item to dictionary--------------------"""
salary['MB'] = 68000
print (salary)

"""-------------------Updating value of item to dictionary-----------------"""
salary['MB'] = 72000
print (salary)

"""-------------------Updating value of item to dictionary-----------------"""
salary['MM'] += 2000
print (salary)


tel = {'Fabiana': 628, 'Jennifer': 736, 'Ellen': 680}
tel['Muna'] = 9856 #Adding a new value to the end of a dictionary
tel ['Ellen'] = 3680 # Updating number of key 'Ellen'
tel['Jennifer'] = 2736 # Updating number of key 'Jennifer'
tel['Fabiana'] = 4628 # Updating number of key 'Fabiana'
print (tel)

k = 'Dave' #Assigning variable to key we're searching for in order to make it more changeable
if k in tel: # If this key is in the dictionary...
    print (k, ':', tel[k]) # Then print the key name and it's value
else:
    print(k, 'not found!') #else print the key name and not found.



salary_band_1 = 20000
salary_band_2 = 27000
salary_band_3 = 34000
salary_band_4 = 41000
salary_band_5 = 48000
salary_band_6 = 55000
salary_band_7 = 62000
salary_band_8 = 69000
salary_band_9 = 76000
salary_band_10 = 83000

employees = {'RW': salary_band_4, 'JS': salary_band_7, 'JM': salary_band_2, 'RM': salary_band_1, 'GW': salary_band_9}

print (employees)

del employees['RM']
print (employees)

print (employees.keys())
print (employees.values())

# Must convert to list to amend and retrieve information by index in the dict_key or dict_value function
emp_keys = list(employees.keys())
emp_values = list(employees.values())

print (emp_keys)
print (emp_values)

#------------------------- Metals Dictionary: More sorting ------------------------

#assigning lists to variables to make them easier to manipulate later on and for readability in the dictionary
iron = [7.8, 1.70, 10]
gold = [19.3, 88.52, 3]
zinc = [7.13, 7.76, 9]
lead = [11.4, 139.40, 33]

densities = {'iron': iron, 'gold': gold, 'zinc': zinc, 'lead': lead}

metals = list(densities.keys()) #creates list of keys from dictionary

item_list = list(densities.items()) #creates new list of key-value items in dictionary
print (metals)

def top_share_price():
    k_by_shareprice = sorted(metals, key = lambda k: densities[k][1])
    print (k_by_shareprice)
    top_by_shareprice = k_by_shareprice[0:3] #The square bracket outside the brackets displays only the 2nd value in the list.
    print ('\n The current top two metals by share price are: \n {}'.format(top_by_shareprice))
for item in kv_by_shareprice:



k_by_experiments = sorted(metals, key = lambda k: densities[k][2])
print (k_by_experiments) # Returns keys ordered by position 2 in value tuple

kv_by_experiments = sorted(densities.items(), key = lambda kv:kv[1][2])
print (kv_by_experiments) #Returns dict key-value items ordered by position 2 in value tuple

metals.sort(key = lambda k:densities[k][2]) #Sorts dictionary in place according to position 2 in value tuple

item_list.sort(key = lambda kv:kv[1][2]) #Sorts list of key-values in place according to position 2 in value tuple



print('\n')
print('\n')
print('\n')

print ('The current shareprice of iron, zinc, gold and lead are as follows: {}.'.format(kv_by_shareprice))

print ('\n The current shareprice of iron, zinc, gold and lead are as follows: \n')
for item in kv_by_shareprice:
   print (item) #listing items by shareprice using loop function - more readability.


#-------------------------Creating a phonebook dictionary----------------------------
import random

phonebook = {}
count = 0

def get_input(count):

    max_run = 3

    name = input('Please enter your name: ')
    phone = input('Please enter your phone number: ')
    three_digits = int(phone[-3:]) #Selects the last three numbers in any phone numberreturn this as the variable in the dictionary
    number = int(input('Please give a number: '))
    lucky_no = random.randint(1,number) #Calculates random lucky number. return this as the variable in the dictionary
    postcode = input('Please enter a valid postcode: ')
    city = input('Please enter the city or town in which you currently reside: ')
    age = int(input('Please enter your age: '))
    queen_age = 92 - age # Determines the difference between the queen's age and person listed.

    #if else statement to repeat until three key-value sets have been added.
    if count < max_run:
        get_input(count + 1)
        phonebook[name] = (three_digits, lucky_no, postcode, city, queen_age)
        return phonebook
    elif count == max_run:
        phonebook[name] = (three_digits, lucky_no, postcode, city, queen_age)
        f = open("phonebook.txt","w")
        f.write( str(phonebook) )
        f.close()
        return phonebook

# function to contain sorted dictionaries.
def sorted_functions():
    get_input(1)
    phonebook_kl = list(phonebook.keys())
    phonebook_by_name = sorted(phonebook.items(), key = lambda kv: kv[0])
    phonebook_by_city = sorted(phonebook.items(), key = lambda kv: kv[1][3])
    phonebook_by_luckyno = sorted(phonebook.items(), key = lambda kv: kv[1][1])
    print (phonebook_by_name)
    print (phonebook_by_city)
    print (phonebook_by_luckyno)
    return phonebook


#f = open("phonebook.txt","w")
#f.write( str(phonebook) )  #To commit things to a text file, everything must be in string format, so make sure you cast your dictionary first!
#f.close()



#------------------------- Extra Practice ---------------------------

sydney = {"pop" : 4741874, "average annual income" : 82436, "homicide rate" : "6.2 per 100,000", "average temperature" : 22.9, "median house price" : 1111124}

aus_cities = {"Sydney" : 4741874,
                  "Melbourne" : 4677157,
                  "Brisbane" : 2326656,
                  "Perth" : 2004696,
                  "Adelaide" : 1315346,
                  "Canberra" : 447457,
                  "Hobart" : 208324,
                  "Darwin" : 132708}


print (aus_cities["Melbourne"])

print (aus_cities["Sydney"])

cities_klist = list(aus_cities.keys())

aus_cities_sorted = sorted(cities_klist, key = lambda k:aus_cities[k], reverse = True)
print (aus_cities_sorted[0:3])
