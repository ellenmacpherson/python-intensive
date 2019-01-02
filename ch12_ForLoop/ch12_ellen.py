#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:28:40 2018

@author: ellenmacpherson
"""
##-----------------------------------------------------------------------------------
#
##Syntax. The following x value should be a meaningful name, eg. 'item' or 'person' etc.
#
##-----------------------------------------------------------------------------------
#
##for x in name_of_thing_to_iterate_through: 
#    #do action
#
##----------------------------------------------------------------------------------
#    
## My first for loops. Task 1. 
#
##----------------------------------------------------------------------------------
#
#my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
#
#print ('\n-------- Printing each item in shopping cart list -----------\n')
#
#for item in my_shopping_cart: #item is a placeholder variable. can be anything.
#    print (item) # For every index of my_shopping cart, print the corresponding value. Will return all values listed in order. 
#    
#    
##----------------------------------------------------------------------------------
#    
##Task 2
#
##----------------------------------------------------------------------------------
#    
#values = [875, 23, 451]
#
#print ('\n-------- Printing each value in values -----------\n')
#
#for value in values:
#    print ('---> ' + str(value))
#
#print ('\n-------- Adding 50 to each value in values -----------\n')
#
#for value in values: 
#    print ('---> ' + str(value + 50))
#    
#    
#    
##----------------------------------------------------------------------------------
#    
##Task 3
#
##----------------------------------------------------------------------------------
#    
#print ('\n-------- Making my own lists and practicing  -----------\n')
#
#year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
#for months in year: 
#    print (months)
#
#
##----------------------------------------------------------------------------------
#    
##Task 4
#
##----------------------------------------------------------------------------------
#
#
#print ('\n-------- Looping through strings -----------\n')
#
#for char in "Yes":
#    print (char) #Will print each character on a separate line.
#
#for char in "Yes we can":
#    print (char) #Will also print white spaces as characters. 
#    
#print ('\n-------- Splitting strings to make list -----------\n')
#    
#for word in "Yes we can".split(' '): #Splits string into list separated by spaces  and prints whole words. 
#    print (word)
#
##----------------------------------------------------------------------------------
#    
##Task 5
#
##----------------------------------------------------------------------------------
#
#print ('\n-------- Looping through tuples -----------\n')
#
#friends = ('Janine', 'Rob', 'Jack', 'Andrew', 'Fabiana', 'Jennifer')
#
#for friend in friends: 
#    print (friend)
#    
##----------------------------------------------------------------------------------
#    
##Task 6 - salary dictionary
#
##----------------------------------------------------------------------------------
#    
#    
#
##----------------------------------------------------------------------------------
#    
##Task 7
#
##----------------------------------------------------------------------------------
#    
#print ('\n-------- Applying for loop to ch. 10 metals dictionary -----------\n')
#
#iron = [7.8, 1.70, 10]
#gold = [19.3, 88.52, 3]
#zinc = [7.13, 7.76, 9]
#lead = [11.4, 139.40, 33]
#
#densities = {'iron': iron, 'gold': gold, 'zinc': zinc, 'lead': lead}
#
#metals = list(densities.keys())
#
#print ('\n-------- Sorting dict and printing metals by share price(descending) -----------\n')
#
#metals_by_price_asc = sorted(densities.items(), key = lambda kv:kv[1][1])
#metals_by_price_desc = sorted(densities.items(), key = lambda kv:kv[1][1], reverse = True)
#    
#for item in metals_by_price_desc:
#    print(item) #Prints metals by dexcending price. 
#    
#print ('\n-------- Printing specific values from sorted dicts -----------\n')
#
#    
#for k, v in metals_by_price_desc:
#    if v[1] > 5:
#        print ('The share price of', k, 'is', v[1], 'dollars.') #prints metal = price.
#    else:
#        print ('The value of {} is lower than $5.'.format(k))
#    
##for metal in metals:
##    print ('{0:>8} = {1:2f}'.format(metal, densities[metal][1]))
##
##for metal in metals: 
##    if densities[metal][1] > 5:
##        print ('The value of {} is {}'.format(metal, densities[metal][1]))
##    else:
##        print ('The share price of {} is lower than $5.'.format([metal][0]))
#        
#        
##----------------------------------------------------------------------------------
#    
##Extra example - Restaurant Ratings
#
##----------------------------------------------------------------------------------
#        
#print ('\n-------- Printing restaurants dict soreted by rating -----------\n')
#
#rated_restaurants = {'San Remedio': 4.7, 
#                     'Dishoom': 4.6, 
#                     'Kiln': 4.3, 
#                     'Smoking Goat': 4.5, 
#                     'Charlotte\'s Bistro': 4.2, 
#                     'Misato': 3.9, 
#                     'Padella': 4.2,
#                     'Kelly\'s': 3.5,
#                     'The Hole in the Wall': 3.2}
#
#rating_desc = sorted(rated_restaurants.items(), key = lambda kv:kv[1], reverse = True) #rating restaurants from worst to best
#
##print (rating_desc)
#
#for k, v in rating_desc:
#    if v >= 4.5: 
#        print ('{} has a rating of {}. Advance booking recommended.'.format(k, v))
#    elif v > 4: 
#        print ('{} has a rating greater of {}. Advanced booking optional.\n'.format(k, v))
#    else: 
#        print ('{} has a rating lower than 4. Might be a good idea to give this one a miss.\n'.format(k))
#
#
#
##----------------------------------------------------------------------------------
#    
##Task 8
#
##----------------------------------------------------------------------------------  
#
#values = [3, 12, 9]
#total = 0 #After the first iteration, total = 3. Then total += 12, so total becomes 15. After final iteration (15 += 9), total = 24.
#for val in values:
#    total += val
#print ('TOTAL:' + str(total)) #Returns 'TOTAL: 24'
#
#print (len(values)) #Will return 3. 
#
#print (list(range(len(values)))) #Will print [0, 1, 2] - index values of list
#
#print ('\n-------- Creating sum functions -----------\n')
#
#
#
#
#
#for index in range(len(values)):
#    values[index] = values[index] * 2 #Will multiply the value at each index by 2
#print(values)
#
#for i in range(3, 10, 2): #Will print every second value from integers from 3 - 10
#    print(i)
#
#
#print ('\n-------- Salary example -----------\n')
#
#years = [2018, 2019, 2020, 2021, 2022]
#
#salary = 30000
#
#bonus = salary * 0.05
#
#for year in years: 
#    salary = salary * 1.03
#    print ('With the annual increase of 3%, your new salary is: {}'.format(round(salary,2)))
#    total_pay = bonus + salary
#    print ('Your total pay for the year, including your 5% bonus, is: {}.\n'.format(round(total_pay,2)))
#    
#print ('\n-------- Christmas present example -----------\n')
#
#christmas_list = {'chocolate': 2, 'jumpers': 5, 'book vouchers': 10, 'alcohol': 7, 'books': 9, 'DVDs': 6, 'music': 6, 'bath items': 3, 'gig tickets': 8}
#
#kv_list = sorted(christmas_list.items(), key = lambda kv:kv[1])
#
#for k, v in kv_list: 
#    if v < 5: 
#        print ('Ah, {}, that\'s a shame.'.format(k))
#    elif v >= 5 and v <= 7:
#        print ('{}, great!'.format(k.title()))
#    else: 
#        print ('Yes, {}! Just what I wanted!'.format(k))
#
#
#print ('\n-------- Revising range function -----------\n')
#
#print (list(range(10))) #Will print list with 0 - 9 as values. 
#
#print (list(range(1, 10)))#Will print list with 1 - 9 as values. 
#
#print (list(range(1, 10, 2))) #Will print [1, 3, 5, 7, 9].

values = [3, 12, 9, 5, 6, 23, 14, 7, 1, 8, 32, 22]


    
for index in range(0, len(values)):
    print (index)
    if values[index] == 1:
        print ('Found!')
        break #will print all indices until 8 then break.

numbers = [1, 5, 30, 200, 101, 100, 22]

for num in numbers:
    print (num)
    if num > 100:
        print ('Break: \n')
        break #Will list all values up to and including 200 and then break
    
for index in range(len(numbers)): #Note because we're not pronting the whole list, this will return 'Break: 200 with index 3' because 200 is the first value over 100 and sits at index 3. 
    if numbers[index] > 100:
        print ('Break:', numbers[index], 'with index', index)
        break 

#----------------------------------------------------------------------------------
    
# Counter

#----------------------------------------------------------------------------------  

colours = ['red', 'green', 'red', 'green', 'blue', 'green', 'green']

d = {}

for item in colours: #Counts the number of times a colour reoccurs in dictionary. 
    if item not in d:
        d[item]= 1
        print (d, 'first time')
    else: 
        d[item] += 1
        print (d)
        
#----------------------------------------------------------------------------------
    
# Nested loops

#----------------------------------------------------------------------------------  
        
outer_vals_list = [1, 2, 3]

inner_vals_list = ['A', 'B', 'C']

dict = {}

for outer_val in outer_vals_list:
    for inner_val in inner_vals_list:
        print (outer_val, inner_val)
        dict[outer_val] = inner_val #This will return [1: 'C', 2: 'C', 3: 'C']
        
for outer_val in outer_vals_list:
    for inner_val in inner_vals_list:
        print (outer_val, inner_val)
        dict[outer_val] = inner_val #This will return [1: 'C', 2: 'C', 3: 'C']
        print (dict)
            
