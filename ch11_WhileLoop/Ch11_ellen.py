"""-----------------Introduction to While Loops----------------------"""

# Basic while loop.

x = 33

while x >= 1:
    print(x, ':', end = '')
    x = x / 2
print(x)

###################################################################
######## Defining functions to return triangular numbers. #########
###################################################################

n = 20 #How many loops are we looping through? This will only continue until the subraction number = 1.

#Outside of function
while n > 0:
   triangle_no = triangle_no + n
   n = n - 1 #Reducing the value of the number we're subtracting by 1
   print (triangle_no)


def triangle(n):
   triangle_no = 0
   while n > 0:
       triangle_no = triangle_no + n
       n = n - 1 #Reducing the value of the number we're subtracting by 1
   print(triangle_no)
   return(triangle_no)


###################################################################
########## More while loop practice - grade calculator. ###########
###################################################################

def grade_calculator(score):
   while score >= 0:
       score = int(input('Please enter your mark: '))
       if score >= 85:
           print ('Your mark is {}. You achieved a First Class. Brilliant!'.format(score))
           return 'first_class'
       elif score >= 65:
           print ('Your mark is {}. You achieved a Second Class. Well done!'.format(score))
           return 'pass'
       elif score >= 50:
           print ('Your mark is {}. You achieved a Pass. Good work!'.format(score))
           return 'pass'
       elif score == 0:
           print ('This was a non-attempt. Please speak to your advisor if you haven\'t already.'.format(score))
           return 'non-attempt'
       else:
           print ('Your mark is {}. Unfortunately you\'ve failed.'.format(score))
           return 'fail'


did_you_pass = input('Did you pass? ')

while did_you_pass == 'Yes':
   score = int(input('What was your score? '))
   if score >= 85:
       print ('First class!')
   elif score >= 65:
       print ('Second Class')
   elif score >= 50:
       print ('Pass')
   

###################################################################
################# Introduction to break command. ##################
###################################################################
i = 200

while i > 10:
   print (i)
   i = i * 0.5
   if i == 25.0:
       break

while True:
   name = input('Enter your name: ')
   if name == 'no':
       break
   print ('Hello', name)

"""------------Converting If Else Statement in Ch. 10 phonebook dictionary to while loop. ---------"""

import random

phonebook = {}
count = 0

def get_input(count):

    max_run = 4

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

    while max_run > 0:
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


"""---------Creating random number guessing game with while loops --------------"""

from random import randint

def guess(attempts, range):
    number = randint(1, range) #Returns random number from 1 to the end of a specified range.
    no_of_guesses = 5
    print ("You need to defuse a bomb! Guess the number to save the city! ".format(attempts))
    while no_of_guesses <= attempts and no_of_guesses > 0:
        print ('You have {} guesses remaining.'.format(no_of_guesses))
        guess = int(input('Guess a number: '))
        if guess < number:
            print ('Oh no! Too low.')
        elif guess > number:
            print ('Oh dear! Too high.')
        elif guess == number:
            print ('You got it. The city is saved and the mayor wants to give you a medal!')
            break
        no_of_guesses = no_of_guesses - 1

        while no_of_guesses == 0:
            print ("BOOM.")
            print ("---------------------------------------------------------")
            print ("End of game. Thanks for playing!")
            print ("---------------------------------------------------------")
            break


"""---------------Creating dice game with while loops------------------------- """

def dice_game():

    play_on = input('Will the result be odd or even? If you don\'t want to play again, just type quit. ')

    dice_value  = randint(1,6) + randint(1, 6)
    if ((dice_value % 2) == 0) == True:
        dice_value = 'even'
    else:
        dice_value = 'odd'

    while play_on == 'odd':
        if dice_value == 'odd':
            print ('You win!')
            break
        else:
            print ('You lose!')
            break
    while play_on == 'even':
        if dice_value == 'even':
            print ('You win!')
            break
        else:
            print ('You lose!')
            break
    while play_on == 'quit':
        print ('Thanks for playing!')
        break
