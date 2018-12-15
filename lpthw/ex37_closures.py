# https://www.programiz.com/python-programming/closure

# A function defined inside another function is called a nested function.
# Nested functions can access variables of the enclosing scope.

# In Python, these non-local variables are read-only by default and we
# must declare them explicitly as non-local (using nonlocal keyword) in
# order to modify them

# If we don't declare a variable in a nested function is nonlocal,
# a new local variable with the same name is created, but the non-local
# variable is not modified
# https://www.programiz.com/python-programming/keyword-list#nonlocal


# Following is an example of a nested function accessing a non-local
# variable (which it can do as read-only)

def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")

# We can see that the nested function printer() was able to access the
# non-local variable msg of the enclosing function.
# I'd call this accessing a non-local argument really.


# what would happen if the last line of the function print_msg() returned
# the printer() function instead of calling it? 

def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

another = print_msg("Hello")
another() # Output: Hello


# So just running print_msg("hello") wouldn't cause it to print anything
# because it just returns the printer function
# 
# but it returns the printer function with hello in it...
# So if you assign the returned printer function to a new variable,
# that will now be a name for the printer function with hello in it.
# so you can run it argument free as above

# The print_msg() function was called with the string "Hello" and the
# returned function was bound to the name another. On calling another(),
# the message was still remembered although we had already finished 
# executing the print_msg() function.

# This technique by which some data ("Hello") gets attached to the 
# code is called closure in Python

# This value in the enclosing scope is remembered even when the variable 
# goes out of scope or the function itself is removed from the current
# namespace.

del print_msg
another()
#still works

# The criteria that must be met to create closure in Python are
# summarized in the following points:

# We must have a nested function (function inside a function).

# The nested function must refer to a value defined in the enclosing
# function.

# The enclosing function must return the nested function.

print("\n")



########### When to use closures? #############

# Closures can avoid the use of global values and provides some form of 
# data hiding. It can also provide an object oriented solution to the 
# problem.

# When there are few methods (one method in most cases) to be implemented
# in a class, closures can provide an alternate and more elegant solutions.
# But when the number of attributes and methods get larger, better
# implement a class.

# Here is a simple example where a closure might be more preferable than
# defining a class and making objects. But the preference is all yours.

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

###############################################
print("\n")

# On a concluding note, it is good to point out that the values that get
# enclosed in the closure function can be found out.

# All function objects have a __closure__ attribute that returns a tuple
# of cell objects if it is a closure function. Referring to the example
# above, we know times3 and times5 are closure functions.

print(make_multiplier_of.__closure__)
print(times3.__closure__)

print("\n")

# The cell object has the attribute cell_contents which stores the closed
# value.

print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)



