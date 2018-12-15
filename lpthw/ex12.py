# rewriting previous exercise using input to do all the prompting.
age = int(input("How old are you? "))
height = input(f"You're {age}? Nice. How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So you're {age} old, {height} tall and {weight} heavy.")

# Happy wit dat.

# In terminal: python -m pydoc input


# Doing this (below) doesn't assign the input to a variable.
# It also gives a blank input betfore printing the string and input
# once you've entered it.

# print("How old are you?" , input())


# The golden rule in programming: If you can do one thing, and you can
# Do another thing, you can usually combine them.
