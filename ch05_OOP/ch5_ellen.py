

#Task 1 - using classes

class customer (object):
    # A customer of our bank with a checking account. The class 'customer' has the following list of attributes:
    # name: A string representing the name of the customer
    # balance: a float that tracks the money available in the customer's account

    def __init__ (self, name, balance = 0.0): # Retuens a customer whose name is 'name' and whose balance is 'balance'
    #Self provides intructions to use on instances of the class (ie. grace)
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        #Returns the remaining balance after the amount in variable 'amount' is taken out.
        if amount > self.balance:
            raise RuntimeError("Amount greater than available balance.") #Raises error so customer does not go < 0 dollars.
            self.balance -= amount
            return self.balance

    def deposit (self, amount):
        #Returns the balance remaining when customer deposits amount.
        self.balance += amount
        return self.balance

grace = customer('Grace Hopper', 3000.0)
jason = customer('Jason Taylor', 1000.0)

print (grace.balance)
print (jason.balance)


#----------------- Exploring inheritance in classes -------------------



# Creating an animal class and various subclasses

class Animal():
    #Initialises a superclass called animal which has name and age attributes.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print ('Food, please?')

class Dog(Animal):
    def bark(self):
        print('Woof!')

class Cat(Animal):
    def meow(self):
        print('Meow!')

pickles = Cat('Pickles', 3) #An instance of the cat subclass.
pickles.meow() #subclass method. Will print 'Meow' to the console.

#Creating a robot class and various subclasses

class Robot():
    def move(self):
            print('Zooooooom')

class CleanRobot(Robot): #Inherits the move function from the superclass, as well as having its own vaccum function
    def clean(self):
        print('I vacuum dust')

class CookRobot(Robot):
    def cook(self):
        print ('My specialty is Italian food!')




#Robot superclass using above main functions. Association.
class SuperRobot():
    def __init__(self):
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
        self.o4 = CookRobot()

    def playGame(self): #New function specific to SuperRobot class
        print('alphago game')

    def move(self):
        return self.o1.move()

    def bark(self):
        return self.o2.bark()

    def eat(self):
        return self.o2.eat()

    def clean(self):
        return self.o3.clean()

    def cook(self):
        return self.o4.cook()



robotDog = SuperRobot('Snoopy', 7)
robotDog.move()
robotDog.bark()
robotDog.eat()
