# Modules, Classes, and Objects

# Dictionaries map one thing to another:

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# Keep this idea of get X from Y in your head, and now think about modules.
# You import a Python file with some functions or variables in it
# And you can access the functions or variables in that module with the
# . (dot) operator.

########################

# Imagine I have a module that I decide to name mystuff.py and I put a 
# function in it called apple, and a variable called tangerine.

# This goes in mystuff.py
def apple():
    print("I AM APPLES!")

tangerine = "Living reflection of a dream"

# I can then use the module mystuff with import and then access the apple
# function:
# 

import mystuff
mystuff.apple() # Have to reference where the apple function comes from
# I think before you were importing 'thing as thing' to make it shorter
print(mystuff.tangerine)


# Let's compare syntax:

mystuff['apple'] # get apple from dict
mystuff.apple() # get function apple from the module
mystuff.tangerine # same thing, it's just a variable

# This means we have a very common pattern in Python:
# 1. Take a key=value style container.
# 2. Get something out of it by the key’s name.

# In the case of the dictionary, the key is a string and the syntax is
# [key].

# In the case of the module, the key is an identifier, and the syntax 
# is .key. Other than that they are nearly the same thing.

container['key']
container.key()
cointainer.key

# You can think about a module as a specialized dictionary that can store 
# Python code so you can access it with the . operator

