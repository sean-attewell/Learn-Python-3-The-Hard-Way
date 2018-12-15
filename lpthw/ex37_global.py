# https://www.programiz.com/python-programming/global-keyword

# In Python, global keyword allows you to modify the variable outside
# of the current scope. It is used to create a global variable and make
# changes to the variable in a local context.


# When we create a variable inside a function, it’s local by default.
# When we define a variable outside of a function, it’s global by default.

# We use global keyword to read and write a global variable inside a
# function. Use of global keyword outside a function has no effect.

c = 1 # global variable

def add():
    print(c)

add()


print()

# c = 1 # global variable
    
# def add():
    # c = c + 2 # increment c by 2
    # print(c)

# add()

# UnboundLocalError: local variable 'c' referenced before assignment

# This is because we can only access the global variable but cannot 
# modify it from inside the function.

# The solution for this is to use the global keyword.


##### Changing Global Variable From Inside a Function using global ######

c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)



print()

####### Share a global Variable Across Python Modules ######

# Very interesting, check website.

# The module config.py stores global variables of a and b. 
# In update.py file, we import the config.py module and modify the values
# of a and b.
# in main.py file we import both config.py and update.py module. 


####### Global in Nested Functions ##########

def foo():
    x = 20 # This isn't set to global

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main : ", x)

# First two prints happen in foo, where x isn't global so doesn't get
# changed


# In the above program, we declare global variable inside the nested 
# function bar(). 
# Inside foo() function, x has no effect of global keyword.


# Before and after calling bar(), the variable x takes the value of 
# local variable i.e x = 20. 
#
# Outside of the foo() function, the variable x will take value defined in
# the bar() function i.e x = 25. This is because we have used global 
# keyword in x to create global variable inside the bar() function 
# (local scope).

# If we make any changes inside the bar() function, the changes appears 
# outside the local scope, i.e. foo().