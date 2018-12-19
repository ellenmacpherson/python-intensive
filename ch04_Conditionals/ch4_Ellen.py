

#------------------------ IF statements ----------------------------

number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer

if number > 10:
    print ("Too high!")
if number <= 0:
    print ("Too low!")

#------------------------ ELSE statements ----------------------------

#If none of the if conditions are met then we can return an else statement. In this case, since we have only specified what is to happen if we enter a number OUTSIDE the 1-10 range, it will print 'Great, thanks!' if the number is between 1 and 10.

if number > 10:
    print ("Too high!")
if number <= 0:
    print ("Too low!") #This is incorrect code. The else statement will only catch the second if statement. We should use an elif statement instead. See below.
else:
    print ("Great, thanks!")

#------------------------ ELIF statements ----------------------------


#elif is Python's way of saying "if the previous conditions were not true, then try this one". There should only ever be one else condition! If you have the urge to add another else statment, add elif instead.

if age < 13:
    print ('child')
elif age < 18:
    print ('teen')
elif age < 65:
    print ('adult')
else:
    print ('pensioner')
