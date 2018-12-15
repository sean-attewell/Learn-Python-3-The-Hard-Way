# Dictionary (or ”dict”)

# you can only use numbers to get items out of a list.
# More options with a dictionary, it's more like a database

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}

print(stuff['name'])
# Zed
print(stuff['age'])
# 39
print(stuff['height'])
# 74
stuff['city'] = "SF"
print(stuff['city'])
# SF

print(stuff)

print("\n")
# You will see that instead of just numbers we’re using strings to say 
# what we want from the stuff dictionary. We can also put new things into
# the dictionary with strings. It doesn’t have to be strings though. We
# can also do this:

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
# Wow
print(stuff[2])
# Neato
print(stuff)
# {'name': 'Zed', 'age': 39, 'height': 74, 'city': 'SF', 1: 'Wow', 2: 'Neato'}
# So it's just making a new dictionary key with the number, rather than it
# being at the index position you'd think of with a list.

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

###############

# This example is mapping states to their abbreviations and then the 
# abbreviations to cities in the states. Remember, 'mapping' or 
# 'associating' is the key concept in a dictionary.

# Think how much easier this would be with a good var name like
# states_abbrev and abbrav_cities or something like that

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# Print out some states

print("-" * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Do it by using state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
# Here just start with innermost brackets. So you're looking up the
# abbreviation of Michigan first, which then gives you the inside of
# the square brackets 'MI' to look for the city in cities.


# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print(list(cities.items()))
# [('CA', 'San Francisco'), ('MI', 'Detroit'), ('FL', 'Jacksonville'), ('NY', 'New York'), ('OR', 'Portland')]

# Now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has cities {cities[abbrev]}")

print("-" * 10)
# Safely get an abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not Exist')
print(f"The city for the sate 'TX' is: {city}")

# dict in Python is just like a dictionary in the real world - you are
# mapping the word to its definition.

# Python dictionaries do not have an order

# Use a list for any sequence of things that need to be in order, and
# you only need to look them up by a numeric index

# you could call dictionaries 'look up tables.'

# A dictionary (or dict) is for matching some items (called keys) to
# other items (called values).

# What if I need a dictionary, but I need it to be in order? Take a 
# look at the collections.OrderedDict data structure in Python