

#------------------------ IF statements ----------------------------

number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer

if number > 10:
    print ("Too high!")
if number <= 0:
    print ("Too low!")

#------------------------ ELSE statements ----------------------------

if number > 10:
    print ("Too high!")
if number <= 0:
    print ("Too low!")
else:
    print ("Great, thanks!") #This else statement will only catch the second if statement. We should use an elif statement instead. 

#------------------------ ELIF statements ----------------------------

#The above statements are bad form. Any if statements following an original statement should be 'elif' - else if. Python's way of saying "if the previous conditions were not true, then try this one".

if age < 13:
    print ('child')
elif age < 18:
    print ('teen')
elif age < 65:
    print ('adult')
else:
    print ('pensioner')
