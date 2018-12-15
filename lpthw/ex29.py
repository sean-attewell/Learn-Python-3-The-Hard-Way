people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")


# in ex23.py you indented 4 spaces for defining a function, then another
# 4 below the if within the function. 

# If the boolean operator is true then it does the intented bit below
# the If. Goes into the branch.  

# If not true then do whatever is at the level of the previous indent
# e.g. the function indent.

# Invalid syntax if you forget the colon