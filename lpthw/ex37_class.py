# Classes and objects!

# https://www.programiz.com/python-programming/class

# Python is an object oriented programming language. Unlike procedure 
# oriented programming, where the main emphasis is on functions, 
# object oriented programming stress on objects.

# Object is simply a collection of data (variables) and methods (functions)
# that act on those data. 

# Class is a blueprint for the object. We can think of class as a sketch 
# (prototype) of a house. It contains all the details about the floors, 
# doors, windows etc.

# House is the object. As, many houses can be made from a description, we
# can create many objects from a class. 

# An object is also called an instance of a class and the process of 
# creating this object is called instantiation.

######################################################

# Defining a Class in Python


# Like function definitions begin with the keyword def,  
# we define a class using the keyword class.

# Keywords come up blue as well as purple then!

# The first string is called docstring and has a brief description 
# about the class. Although not mandatory, this is recommended.

class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass


# A class creates a new local namespace where all its attributes are 
# defined. Attributes may be data or functions.

# There are also special attributes in it that begins with double
# underscores (__). For example, __doc__ gives us the 
# docstring of that class.

print(MyNewClass.__doc__)

# As soon as we define a class, a new class object is created with
# the same name. This class object allows us to access the different
# attributes as well as to instantiate new objects of that class.

class MyClass:
	"This is my second class"

	a = 10

	def func(self):
	    print('Hello')

# Output: 10
print(MyClass.a)
# So this is the Myclass object being used, which was created when
# the class was defined.


# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)

print("\n\n")
######################################################

# Creating an Object in Python

# We saw that the class object could be used to access different 
# attributes.

# It can also be used to create new object instances (instantiation)
# of that class. The procedure to create an object is similar to
# a function call.

ob = MyClass()

# This will create a new instance object named ob. We can access
# attributes of objects using the object name prefix.

# Attributes may be data or method. Method of an object are corresponding
# functions of that class. Any function that is a class attribute
# defines a method for objects of that class.

# This means to say, since MyClass.func is a function object (attribute 
# of class), ob.func will be a method object.


# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()

# You may have noticed the self parameter in function definition inside
# the class but, we called the method simply as ob.func() without any 
# arguments. It still worked.

# This is because, whenever an object calls its method, the object itself
# is passed as the first argument. So, ob.func() translates into 
# MyClass.func(ob).

# In general, calling a method with a list of n arguments is equivalent
# to calling the corresponding function with an argument list that is 
# created by inserting the method's object before the first argument.

# For these reasons, the first argument of the function in class must
# be the object itself. This is conventionally called self. It can be
# named otherwise but we highly recommend to follow the convention.
print("\n\n")

######################################################

# Constructors in Python

# Class functions that begins with double underscore (__) are called
# special functions as they have special meaning.

# Of one particular interest is the __init__() function. This special
# function gets called whenever a new object of that class is instantiated.

# This type of function is also called constructors in Object 
# Oriented Programming (OOP). 
# 
# We normally use it to initialize all the variables.

class ComplexNumber:
    def __init__(self,r = 0,i = 0): # args default to zero
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
c1.getData()
# Output: 2+3j

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: 5, 0, 10
print(c2.real, c2.imag, c2.attr)

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# c1.attr

# In the above example, we define a new class to represent complex numbers.
# It has two functions, __init__() to initialize the variables 
# (defaults to zero) and getData() to display the number properly.

# An interesting thing to note in the above step is that attributes
# of an object can be created on the fly. We created a new attribute 
# attr for object c2 and we read it as well. But this did not create that
# attribute for object c1.

######################################################

# Any attribute of an object can be deleted anytime, using the 
# del statement

# del c1.imag
# del ComplexNumber.getData

# We can even delete the object itself, using the del statement
# del c1

# Actually, it is more complicated than that. When we do 
# c1 = ComplexNumber(1,3), a new instance object is created in
# memory and the name c1 binds with it.

# On the command del c1, this binding is removed and the name c1
# is deleted from the corresponding namespace. The object however
# continues to exist in memory and if no other name is bound to it,
# it is later automatically destroyed.

# This automatic destruction of unreferenced objects in Python 
# is also called garbage collection.

