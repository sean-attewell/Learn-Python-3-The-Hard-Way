# Most of the uses of inheritance can be simplified or replaced with composition, 
# and multiple inheritance should be avoided at all costs


# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent. 


# 1. Implicit Inheritance

print("Implicit Inheritance")

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# even though I’m calling son.implicit() on line 13 and even though Child does not
# have an implicit function defined, it still works, and it calls the one defined
# in Parent

# if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child)
# will automatically get those features.
# Very handy for repetitive code you need in many classes.

print()

# 2. Override Explicitly

print("#2 Override Explicitly")

# sometimes you want the child to behave differently.
# In this case you want to override the function in the child, effectively replacing
# the functionality.
# To do this just define a function with the same name in Child.

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# because son is an instance of Child and Child overrides that function 
# by defining its own version

print()

print("#3 Alter before or after")

# 3. Alter before or after

# a special case of overriding where you want to alter the behavior before or after
# the Parent class’s version runs. (aka change what the same name function does
# but still get the parent version to run at some point)

# You first override the function just like in the last example, but then you use a
# Python built-in function named super to get the Parent version to call.

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        # "call super with arguments Child and self, then call the function altered
        # on whatever it returns."
        # Also works without any parameters in super
        # Guess super is green because it relates to class names
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()        

dad.altered()
print()
son.altered()



#class SuperFun(Child, BadStuff):
    #pass

# "Make a class named SuperFun that inherits from the classes Child and BadStuff at
# the same time."

# In this case, whenever you have implicit actions on any SuperFun instance, Python 
# has to look-up the possible function in the class hierarchy for both Child and
# BadStuff, but it needs to do this in a consistent order. To do this Python uses
# "method resolution order" (MRO) and an algorithm called C3 to get it straight.

# Because the MRO is complex and a well-defined algorithm is used, Python can’t leave 
# it to you to get the MRO right. 
# Instead, Python gives you the super() function, which handles all of this for you 
# in the places that you need the altering type of actions as I did in Child.altered.
# With super() you don’t have to worry about getting this right, and Python will find
# the right function for you. Hence why you can run it without specifying the parent.


# Using super() with __init__

# The most common use of super() is actually in __init__ functions in base classes.
# This is usually the only place where you need to do some things in a child, then 
# complete the initialization in the parent.

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff

        super(Child, self).__init__()


# This is pretty much the same as the Child.altered example above, except I’m setting 
# some variables in the __init__ before having the Parent initialize with its 
# Parent.__init__.

# So super().__init__ is just like saying Parent().__init__ except it finds the
# class for you 



class Person(object):

    def __init__(self, name):
        
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        
        self.salary = salary

jimmy = Person("Jimmy")

print(jimmy.name)
print(jimmy.pet)


bud = Employee("bud", "bare bucks")

print(bud.name)
print(bud.pet)
print(bud.salary)


# So in the above you put all paramaters into the employee class init, and
# then use one when calling the Person class init with super().
print()


### Composition ### - solves reusable code by giving you modules and the 
### capability to call functions in other classes.

# In this code I’m not using the name Parent, since there is not a parent-child 
# is-a relationship. This is a has-a relationship, where Child has-a Other that it
# uses to get its work done.

class Other(object):

    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other() # initialising it with an instance of another class to use

    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()

# Note that you are instantiating an instance of class other in the __init__
# for the Child class. The instance is called self.other

# Inheritance is useful, but another way to do the exact same thing is just to use
# other classes and modules (as above), rather than rely on implicit inheritance
# We're just calling functions in a module.

# You can see that most of the code in Child and Other is the same to accomplish the 
# same thing. The only difference is that I had to define a Child.implicit function to 
# do that one action. I could then ask myself if I need this Other to be a class, 
# and could I just make it into a module named other.py?


# In Python, classes act as templates that "mint" new objects


# The question of "inheritance versus composition" comes down to an attempt to solve 
# the problem of reusable code.

# Inheritance solves this problem by creating a mechanism for you to have implied 
# features in base classes. Composition solves this by giving you modules and the 
# capability to call functions in other classes.

# Which one is appropriate in which situations?

# 1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. 
# If you’re stuck with it, then be prepared to know the class hierarchy and spend time
# finding where everything is coming from.

# 2. Use composition to package code into modules that are used in many different 
# unrelated places and situations.

# 3. Use inheritance only when there are clearly related reusable pieces of code that
# fit under a single common concept or if you have to because of something you’re using.



## READ THIS https://www.python.org/dev/peps/pep-0008/ ##