# You use the phrase is-a when you talk about objects and classes being
# related to each other by a class relationship. 
# 
# You use has-a when you talk about objects and classes that are related 
# only because they reference each other.
#
# OOP works beacuse that's how everyone agrees how it should work
# Computing could have gone in a different direction.

# In old python 2 code, Animal: was different to Animal(object):
# But now in Python 3 they're exactly the same.
# Python aesthetic rules from python zen - explicit is better than 
# Implicit

# If you put the below then you can say 'a car has wheels'

class car(object):

    def __init__(self):
        self.wheels = 4

# but if class car(FourWheelVehicle) then it inherits from a class
# with 4 wheels

# But the you have to make a class for every number of wheels.
# each is a database table.


# Class Toy has-a owner

class Toy(object):

    def __init__(self, owner):
        self.owner = owner

# makes more sense than 'Animals inherit from things that can have owners'

class OwnedCreature(object):

    def __init__(self, owner):
        self.owner = owner

class Animal(OwnedCreature):
    pass


# Its like how in english you know how to say 'big red ball' rather than
# 'red big ball', but you probably don't think about the rule in place.
# OOP is a languge everyone just kind of knows.

truck = Toy("Mike")

print(f"truck is owned by {truck.owner}")

cat = Animal("Sean")

print(f"cat is owned by {cat.owner}")


###########

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


###############

# https://www.youtube.com/watch?v=3fJ0z49bpFI 
# 

#
# You used to have to pass in arguments to the super keyword but you
# no longer have to do that.
# 
# super().__init__() 
#
# super refers to the parent base class. You don't have to explicitly call
# the base class by name.
#
# Above is for running __init__ from base parent class
#
# So you can tell it to call the parent and run its __init__ code first
# and then continue with your execution
