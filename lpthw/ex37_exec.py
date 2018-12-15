# https://www.programiz.com/python-programming/methods/built-in/exec

# Seems to mean execute

# you can run a string as Python.

# The exec() takes three parameters:

# object - Either a string or a code object
# globals (optional) - a dictionary
# locals (optional)- a mapping object. Dictionary is the standard
# and commonly used mapping type in Python

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

# Here, the string object program is passed to exec() which executes the
# program. globals and locals are omitted in this case.


program = input('Enter a program:')
exec(program)

# The user can input a program, such as:
# [print(item) for item in [1, 2, 3]]
# not sure why in square brackets. Also different use of for.
# Well you can't do a normal for loop with a colon and indent, so maybe
# that's why


# If you want to take Python code from the user which allows multiline
# code (using '\n'), you can use compile() method before using exec().
# https://www.programiz.com/python-programming/methods/built-in/compile


#### Be careful while using exec() ####

# Consider a situation, you are using a Unix system (macOS, Linux etc)
# and you have imported os module. The os module provides portable way
# to use operating system functionalities like: read or write a file.

# If you allow users to input a value using exec(input()), the user may
# issue commands to change file or even delete all the files using
# command os.system('rm -rf *').

# If you are using exec(input()) in your code, it's a good idea to
# check which variables and methods the user can use. You can see
# which variables and methods are available using dir() method.

from math import *
exec('print(dir())')


# More often than not, all the available methods and variables used in 
# exec() may not be needed, or even may have a security hole. 
# You can restrict the use of these variables and methods by passing 
# optional globals and locals parameters (dictionaries) to the exec() 
# method.

# If both parameters are omitted (as in our earlier examples), the 
# code expected to be executed by exec() is executed in the current scope.

# If the locals dictionary is omitted, it defaults to globals dictionary.
# Meaning, globals will be used for both global and local variables

print()



from math import *
exec('print(dir())', {})

# This code will raise an exception:
# exec('print(sqrt(9))', {})

# If you pass an empty dictionary as globals, only the __builtins__ are 
# available to the object (first parameter to the exec()). Even though 
# we have imported math module in the above program, trying to access 
# any of the functions provided by the math module will raise an exception.

#### Making Certain Methods available ###

from math import *
exec('print(dir())', {'sqrt': sqrt, 'pow': pow})

# object can have sqrt() module
exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})

# Here, the code that is executed by exec() can also have sqrt() and pow()
# methods along with __builtins__.

print()

# You can restrict the use of __builtins__ by giving value None to 
# the '__builtins__' in the globals dictionary.

from math import *

globalsParameter = {'__builtins__' : None}
localsParameter = {'print': print, 'dir': dir}
exec('print(dir())', globalsParameter, localsParameter)


# Here, only two built-in methods print() and dir() can be executed by 
# the exec() method.

# It's important to note that, exec() executes the code and doesn't return
# any value (returns None). Hence, you cannot use return and yield 
# statements outside of the function definitions.

