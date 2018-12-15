# 1st second third are ”ordinal” numbers, 
# because they indicate an ordering of things

# A cardinal number is a number such as 1, 3, or 10 that tells you 
# how many things there are in a group but not what order they are in

# Programmers, however, can’t think this way because they can pick any 
# element out of a list at any point. To programmers, the list of animals 
# is more like a deck of cards.

# This need to pull elements out of lists at random means that they need
# a way to indicate elements consistently by an address, or an ”index”. 
# This kind of number is a "cardinal" number and means you can pick at
# random, so there needs to be a 0 element.

# you translate this "ordinal" number to a "cardinal" number by 
# subtracting 1.
# The "third" animal is at index 2 and is the penguin

# Famous OFF BY ONE error 

# Don't have to worry when doing a for loop.
# for bug in bugs

# Can do negative indexes to start from the end of the list
# 0 and -0 are the same thing though. I guess because 0 can't be negative.

hello = "Hello world how are you today"
new_list = hello.split(' ')
print(new_list[2])
# this prints how (the third word)

print(new_list[-1])
# This prints "today"
