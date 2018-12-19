
####################################################
######### Introduction to using classes ############
####################################################

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
            raise RuntimeError("Amount greater than available balance.") #Raises error so customer does not go below 0 dollars.
        else:
            self.balance -= amount
            return self.balance
        

    def deposit (self, amount):
        #Returns the balance remaining when customer deposits amount.
        self.balance += amount
        return self.balance

grace = customer('Grace Hopper', 3000.0)
jason = customer('Jason Taylor', 1000.0)

print('-------Grace\'s balance.---------\n')
print (grace.balance)

print('-------Jason\'s balance.---------\n')
print (jason.balance)
jason.withdraw(600)

print('-------Jason\'s balance after withdrawal.---------\n')
print (jason.balance)


####################################################
############# Inheritance of classes ###############
####################################################


# Creating an animal class and various subclasses

class Animal():
    #Initialises a superclass called animal which has name and age attributes.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print ('Food, please?')

class Dog(Animal):
    def __init__(self, name, age):
      Animal.__init__(self, name, age)
    def bark(self):
        print('Woof!')

class Cat(Animal):
    def __init__(self, name, age):
      Animal.__init__(self)
    def meow(self):
        print('Meow!')
        
Snoopy = Dog('Snoopy', 7)

print('-------Snoopy barking.---------\n')
Snoopy.bark()


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
    
    def __init__(self,name,age):
        #This class contains 3 objects'
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Dog(name, age)
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


machineDog = SuperRobot('Socks', 3)
print('-------machineDog barking.---------\n')
machineDog.bark()

machineCook = SuperRobot('Martha Stewart', 77)
print('-------machineCook\'s specialty.---------\n')
machineCook.cook()
print('-------machineCook\'s name---------\n')
print (machineCook.name, '\n')

