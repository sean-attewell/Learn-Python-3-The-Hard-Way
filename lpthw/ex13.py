# import allows you to add features 
# features are really called modules or libraries. e.g. the sys module. 
# Not giving all at once keeps # programs small. 
# Also acts as documentation for other programmers.

# argv is 'argument variable'. This variable holds the arugments you pass
# to your Python script when you run it (give them in powershell).
from sys import argv

# read the What You Should See section for how to run this
# this "unpacks" argv so that, rather than holding all the arguments, 
# it gets assigned to four variables you can work with: script, first, 
# second, and third
# It just says, ”Take whatever is in argv, unpack it, and assign it
# to all of these variables on the left in order.”
script, first, second, third = argv

# So you've imported the arguments from powershell (the first being 
# the script itself), then you've assigned them to the above variable 
# names in order

# They come in as strings, even if you typed numbers on
# the command line. Use int() to convert them just like with int(input()).

# Variable name has to come first. You are assigning it the input.
request = input("Give me one more now it's running ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("this variable was requested after running", request)

# Trying to run it normally you get:
# "ValueError: not enough values to unpack (expected 4, got 1)"
# you have to pass in three comand line arguments in addition to the script:
# python ex13.py first 2nd 3rd

# Can also get: ValueError: too many values to unpack (expected 4)
# If you input too many into powershell

# Everytime you don't know what's going on, print variables and messages 
# Which show the program running.

print(">>>>argv", repr(argv))
