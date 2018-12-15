# Namespace

# Name (also called identifier) is simply a name given to objects. 
# Everything in Python is an object. Name is a way to access the 
# underlying object

# For example, when we do the assignment a = 2, here 2 is an 
# object stored in memory and a is the name we associate it with.
# We can get the address (in RAM) of some object through the built-in 
# function, id(). Let's check it.



# Note: You may get different value of id
a = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

a = a+1

# Output: id(a) = 10919456
print('id(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2

# Output: id(2)= 10919424
print('id(2) =', id(2))

# This is efficient as Python doesn't have to create a new duplicate object
# a name could refer to any type of object (number, string, list)
# Functions are objects too, so a name can refer to them as well

def printHello():
    print("Hello")     

a = printHello()

a
# Output: Hello
# Our same name a can refer to a function and 
# we can call the function through it.


# namespace is a collection of names

# A namespace containing all the built-in names is created when we start
# the Python interpreter and exists as long we don't exit.
# This is the reason that built-in functions like id(), print() etc. are
# always available to us from any part of the program. 
# 
# Each module creates its own global namespace.
# These different namespaces are isolated. Hence, the same name that
# may exist in different modules do not collide.

# Modules can have various functions and classes. A local namespace is
# created when a function is called, which has all the names defined in it.


# Scope is the portion of the program from where a namespace can be accessed
# directly without any prefix

# At any given moment, there are at least three nested scopes.

# Scope of the current function which has local names
# Scope of the module which has global names
# Outermost scope which has built-in names

# When a reference is made inside a function, the name is searched in the
# local namespace, then in the global namespace and finally in the 
# built-in namespace.

# If there is a function inside another function, a new scope is nested 
# inside the local scope.

def outer_function():
    b = 20
    def inner_func():
        c = 30

a = 10

# Here, the variable a is in the global namespace. Variable b is in the 
# local namespace of outer_function() and c is in the nested local 
# namespace of inner_function().

# When we are in inner_function(), c is local to us, b is nonlocal and 
# a is global. We can read as well as assign new values to c but can only
# read b and a (think it means a) from inner_function()

# If we try to assign as a value to b, a new variable b is created in the 
# local namespace which is different than the nonlocal b. Same thing
# happens when we assign a value to a.

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10

outer_function()
print('a =',a)


print("\n\n")

# I guess python just moves what the function points to at this point!
def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10

outer_function()
print('a =',a)

# Here, all reference and assignment are to the global a due to 
# the use of keyword global.

# I suppose the golbal space a = 10 has run BEFORE the inner function
# changes everything to 30. Likewise the outer function a = 20
# was assigned before the global a = 30.

#