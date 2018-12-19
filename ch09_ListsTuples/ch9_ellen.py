#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:41:02 2018

@author: ellenmacpherson
"""

#########################################################
### LISTS ###
#########################################################

#My first list
my_favourite_fruit = ['apple', 'orange', 'banana']
print (my_favourite_fruit[0])
print (my_favourite_fruit[1])
print (my_favourite_fruit[2])
print (my_favourite_fruit[2][0])

print ('\n')

#Lists can be comprised of different data types.
x = ['this', 55, 'that', my_favourite_fruit]
print (x[0:4])
print (x[0])
print (x[1])
print (x[2])
print (x[3])
print (x[-1]) #Uses a negative index to get the last item in the list. More convenient than having to know the index number at the end of the list.

print ('\n')
#Removing items from lists. This can be done by naming the actual value or accessing it via its index.
#x.remove(x[3])
x.remove(my_favourite_fruit)
print (x)

#Update list item value by accessing its index and assigning it a new value.
x[1] = 'and'
print (x)

print ("\n")
#Add a new value to the end of a list.
x.append('again')
#x.extend('again') - NOT the same as .append. Will return ['a','g','a','i','n'] rather than ['again']
print (x)
append_value = x
append_value = append_value.append("hello")
print (append_value)

#Add a new item to the list at a particular index
x.insert(3, 'once')
print (x)

#Extending a list - merging two lists into one. If you were to use the append function instead, courses_2 would appear as a single list item
courses = ['Maths', 'Chemistry', 'Biology', 'CompSci']
courses_2 = ['Art', 'History', 'Philosophy', 'PolSci']
courses.extend(courses_2)
print (courses)

#Deleting a an item in a list
del x[0]
print (x)

#pop removes the specific index and returns it
return_value = x.pop(1)
print (x)
print (return_value)

#Concatenation of lists
x = ['the', 'cat', 'sat']
y = ['on', 'the', 'mat']
z = x + y
a = set(x + y)
print (z)
print (a)

b = ['a', 'a', 'b', 'b']
c = set(b)
print (c)

print('\n')
#Join string function
print (' '.join(z)) #joins string elements in a list. The prefix determines how the elements are joined together. In this case, they it is a space. In the next example, it's a hypen.
print ('-'.join(z))

#Further operators
print (set(x + y)) #set changes the list datatype to a dictionary.

#Slicing a list
x = ['this', 'and', 'that', 'once', 'again']
print (x[0:4]) #First index number is inclusive, second is not. Thus to include the last element you want, take it's index and +1.
print (x[2:]) #Goes from the first index all the way to the end of the list.
print (x[1], x[2], x[4])
print (x[-3:-1])
print (x[-3:])

print ("\n")

#Sort and sorted.
x = [7, 11, 3, 9, 2]
y = sorted(x) #Produces a sorted copy of list x.
print (y)
x.sort() #Sorts the list in place. Be careful with this because you're working with the original dataset.
print (x)

#Reverse sorting is also possible.
x = [7, 11, 3, 9, 2]
print (sorted(x, reverse=True))

a = ['f', 'x', 'h', 'g', 'b', 'd', 'o']
print (a)
a.sort()
print (a)
a.sort(reverse = True)
print(a)

b = ['a', 'l', 'h', 'x', 'y', 'd', 'e']
print (b)
c = sorted(b)
print (c)
print (sorted(c, reverse = True))

d = [15, 204, 43, 3, 7, 67, 410]
print (d)
d.sort()
print (d)

e = [1, 78, 13, 98, 703, 20, 4]
print (e)
f = sorted(e)
print (f)
print (sorted(f, reverse = True))

print ("\n")
print ("\n")
print ("\n")

#########################################################
### TUPLES ###
#########################################################

#You cannot delete an item inside a tuple or assign a new value to an existing index. Cannot append either. Tuples have fewer advantages than lists, but they are more memory efficient which can be handy in some projects. Likely not useful for us at the moment.

t = (1, 2, 3, 4, 5, 6)
print (t)

#These will throw errors as tuples cannot be modified:
"""
del t[1]
t[2] = 10
t.append(50)
t.remove(4)
t.insert(5, 'null')

"""

#########################################################
### LAMBDA FUNCTIONS AND SORTING ###
#########################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:19:39 2018

@author: ellenmacpherson
"""
#f = lambda x, y: x * y
#print (f(3, 4))

"""
above is equivalent to:
    def f(x, y):
        return x * y
        """
a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["aa", "vb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)


x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]

print (sorted(x2, key=lambda s:s[2][1])) #returns x2 ordered first by the values in the 2nd position, then in the 1st position. The key is how python understands how to sort the data


employees = [('Janine', 'Saunders', 50000, 'UX Designer', 10),
     ('Robert', 'Webster', 90000, 'Senior Engineer', 10),
     ('Jack,', 'Murning', 40000, 'Junior Web Developer', 7),
     ('Jen', 'Burns', 30000, 'Content Creator', 5),
     ('Hannah', 'Beth', 40000, 'Communications Specialist', 6)]

print (sorted(employees, key = lambda bonus:bonus[-1], reverse = True))


a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["ipswich", "bristol", "cardiff", "belfast"]
z = ["london", "glasgow", "ediburgh", "manchester"]
y = sorted(x)

#this list includes 3 tuples. each contains a string, a number and a variable
x2 = [('Kate', 3, z), ('Joanna', 1, y), ('Betty', 5, x)]

print("------print(x2)------")
print (x2)
print()
print("------print(sorted(x2, key=lambda s:s[1]))------")
print(sorted(x2, key=lambda s:s[1]))
# this is organized by what is at the first position in the tuple - number in this case


print()
print ("------print(sorted(x2, key=lambda s:s[2]))------")
print(sorted(x2, key=lambda s:s[2]))
#this is organized by what is at the second position in the tuple - this is the list of cities and take the first city on this list

print()
print("------print(sorted(x2, key=lambda s:s[0]))------")
print(sorted(x2, key=lambda s:s[0]))
##this is organized by what is at the zero position in the tuple - this is name in this case
