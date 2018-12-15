# This one is like your scripts with argv

# First we tell Python we want to make a function using def for ”define”.
# On the same line as def we give the function a name "print_two"
# we tell it we want *args (asterisk args), which is a lot like your
# argv parameter but for functions
# That tells Python to take all the arguments to the function and then put
# them in args as a list.
# Then we end this line with a : (colon) and start indenting.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# After the colon all the lines that are indented four spaces will become
# attached to this name 'print_two'
# Our first indented line is one that unpacks the arguments, the same as
# with your scripts.

# In Python we can skip the whole unpacking arguments and just use the names
# we want right inside ().
# The commas effectively makes a list

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# This just takes one arguments
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("no arguments required")


print_two('bleh', 'ngi')
print_two_again('bean', 'bag')
print_one('bannanananan')
print_none()


# Straight line scripts are like a pole (goes straight down)
# We want a tree with branches.

# Functions are a way for python to pass arugments to itself...
# Similar to passing arguments in through powershell
# Have to be python data types (strings etc.)

# Conceptualise functions as mini scripts
# Think about the code jumping to the functions
# Functions and if statements can do pretty much everything

# ctrl+f find, then F3 to cycle

# Name undefined errors if you misspell functions (same as with variables)
# Argument missing errors if you don't give enough arugments to function
# Indentation error if no indent after a colon
# Unexected indent - expects lines to be indented by the same amount.