# https://www.programiz.com/python-programming/object-oriented-programming

# Python is a multi-paradigm programming language. Meaning, it supports
# different programming approach.

# One of the popular approach to solve a programming problem is by 
# creating objects.

# An object has two characteristics:
# attributes
# behavior

# Parrot is an object,
# name, age, color are attributes
# singing, dancing are behavior

# The concept of OOP in Python focuses on creating reusable code. 
# This concept is also known as DRY (Don't Repeat Yourself).

#####################################################################

# A class is a blueprint for the object.

class Parrot:
    pass

# Here, we use class keyword to define an empty class Parrot. From class,
# we construct instances. An instance is a specific object created 
# from a particular class

#####################################################################

# An object (instance) is an instantiation of a class.

# When class is defined, only the description for the object is defined. 
# Therefore, no memory or storage is allocated.

obj = Parrot()
# Here, obj is object of class Parrot.


class Parrot: # we create a class with name Parrot

    # class attribute (the same for all instances of a class.)
    species = "bird" 

    # instance attribute
    def __init__(self, name, age): # init is initialise, runs first
        self.name = name
        self.age = age
    # The attributes are a characteristic of an object.
    # instance attributes are different for every instance of a class


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
# blue and woo are objects of class Parrot.
# we create instances of the Parrot class. 
# Here, blu and woo are references (value) to our new objects.



# access the class attributes
# we access the class attribute using __class __
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))


# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

print(blu.name)
print(blu.__class__.species)
print("\n\n")


#####################################################################

# Methods are functions defined inside the body of a class. 
# They are used to define the behaviors of an object.


class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'")) # oh that's where the quotes come from.
print(blu.dance())

# In the above program, we define two methods i.e sing() and dance().
# These are called instance method because they are called on an instance
# object i.e blu.
# (maybe there are class methods?)

print("\n\n")

#####################################################################

# Inheritance is a way of creating new class for using details of existing
# class without modifying it. 

# The newly formed class is a derived class (or child class).
# Similarly, the existing class is a base class (or parent class).

# parent class
class Bird:
    
    # instance attributes
    def __init__(self):
        print("Bird is ready")

    # instance method
    def whoisThis(self):
        print("Bird")

    # instance method
    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function - runs __init__ from superior!
        # So it says 'bird is ready' as well as the below.
        super().__init__() # no self written here... super must pull from parent
        print("Penguin is ready")

    def whoisThis(self): # don't need super to overwrite method?
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# In the above program, we created two classes i.e. Bird (parent class)
# and Penguin (child class). 

# The child class inherits the functions of parent class. 
# We can see this from swim() method. 
# 
# The child class modified the behavior of parent class. 
# We can see this from whoisThis() method. 
# 
# Furthermore, we extend the functions of parent class,
# by creating a new run() method.


# We use super() function before __init__() method. 
# This is because we want to pull the content of __init__() method
# from the parent class into the child class.
print("\n\n")

#####################################################################

# Encapsulation

# Using OOP in Python, we can restrict access to methods and variables.
# This prevent data from direct modification which is called encapsulation.
# 
# In Python, we denote private attribute using underscore as prefix 
# i.e single "_" or double "__".

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()
# I guess you can't do it this way beacuse it's encapsulated with __.

# using setter function
c.setMaxPrice(1000)
c.sell()
# I guess you can using a method (behaviour) of the class to do it.

# We tried to modify the price. However, we can’t change it because Python
# treats the __maxprice as private attributes. To change the value, we
# used a setter function i.e setMaxPrice() which takes price as parameter.

print("\n\n")

#####################################################################

# Polymorphism is an ability (in OOP) to use common interface for multiple
# form (data types).

# from Greek πολύς, polys, "many, much" and μορφή, morphē, "form, shape"

# Suppose, we need to color a shape, there are multiple shape option
# (rectangle, square, circle). However we could use same method to color
# any shape. This concept is called Polymorphism.

# the provision of a single interface to entities of different types.

# Polymorphism is the ability to call the add method on an object
# without knowing what kind of a number it is

# For example the add method (or + operator) in the Integer class
# might perform integer addition, while the add method in the Float 
# class performs floating-point addition

# is the ability to perform certain operations on an object 
# without caring about its precise type.

# In some languages that lack polymorphism you find yourself in 
# situations where you want to perform what is conceptually the same 
# operation on different types of objects

# speak() --> gets quack, woof, meow depending on the type of object.

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


# In the above program, we defined two classes Parrot and Penguin. 
# Each of them have common method fly() method. 
# However, their functions are different. 
# 
# To allow polymorphism, we created common interface i.e flying_test()
# function that can take any object. 
# 
# Then, we passed the objects blu and peggy in the flying_test() function,
# it ran effectively.


# Key Points to Remember:
# The programming gets easy and efficient.
# The class is sharable, so codes can be reused.
# The productivity of programmars increases
# Data is safe and secure with data abstraction.
