# For loops:
# for each element in list, assign its value to a variable called i and do:

# For loops are hard to break! will skip the list if nothing in it.
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")
# variable named number is assigned the value of each element of the_count
# the for loop is doing the = for you to assign the variable each time.

# same as above
for fruit in fruits:
    print(f"A fruit of type {fruit}")
# variable named fruit is assigned each element of fruits

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it!!!
for i in change:
    print(f"I got {i}")
# i is shorthand for first level loops, j for second level loops.

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function *that lists understand*
    elements.append(i)
    # append also comes in the for loop block, so it loops for all i

print(">>>> after range: i=", i)
# So the variable i isn't stuck in the for loop. And it's set to the last
# thing in the loop. In other languages that variable goes away.
# So you can use a variable from a for loop in python.
# Which maybe you want to.

# now we can print them out too
for i in elements:
    print(f"Elements was: {i}")

print(fruits[0])
print(fruits[2])


# Normal for index to start at 0 (allows certain maths)
# If you're thinking ordinally: "First position, second position" that 
# indicates that you have to go through them all. But this is random 
# access - you can jump to where ever you want.

# below math get's you a zero (becuase no remainder. The zero based
# indexing makes sure the answer falls within the list (doesn't have
# to have a lower limit of 1 to get a result)
i = 1000000
print(fruits[i % len(fruits)])

# list index out of range if you go beyond the length of your list


# for loops are guaranteed to end. While loops are not.


# range([start], stop[, step])
# looks like square brackets means optional.

# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.

# All parameters must be integers. 
# All parameters can be positive or negative
# Unfortunately the range() function doesn't support the float type.

# if you just put one parameter in, it will take that as the stop.
# two parameters will be start, stop
# three will be start, stop, step

# going backwards, the end is just before the start.
for i in range(0, -10, -2):
    print(i)


my_list = ['one', 'two', 'three', 'four', 'five']
my_list_len = len(my_list)

print(my_list_len)

# Why doesnt this just print the first four?
for i in range(0, my_list_len):
    print(my_list[i])


# It's because you're printing list items from zero to 4
# which is a total of 5 items


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) 


bro_list = list(("apple", "banana", "cherry")) 
# note the double round-brackets
bro_list.append("damson")
bro_list.remove("banana")
print(bro_list)


# In classic terms a list is very different from an array because of 
# how they’re implemented. In Ruby though they call these arrays. 
# In Python they call them lists.

# Why is a for-loop able to use a variable that isn’t defined yet? 
# The variable is defined by the for-loop when it starts, initializing
# it to the current element of the loop iteration each time through.



# https://docs.python.org/3/tutorial/datastructures.html


# to copy a list, copy the full range

howdy = thislist[:]
print(howdy)

print(howdy[1:2]) # ['blackcurrant']
print(howdy[1:3]) # ['blackcurrant', 'cherry']

# howdy[1:] means everything from 1 onwards
# Each time you do that it's making a new list


# Range on its own is just a counter
# You go through a fixed set of numbers
# list(range(0, 100))
# printing that gets you a list from 0 to 99 