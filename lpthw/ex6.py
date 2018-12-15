# f string to include a variable
# Note that the f string is being set as a variable x
types_of_people = 10
x = f"There are {types_of_people} types of people."

# f string that includes two variables (again being set as another var)
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# straight printing variables here
print(x)
print(y)

# printing f strings like the last exercise
# So this is a way to print f strings in f strings
# Note that the second one prints the single quotes
print(f"I said: {x}")
print(f"I also said: '{y}'")

# False isn't in quotes here, because it's not a string, it's something else
# You can use normal strings in quotes and it works with .format()
hilarious = False
# joke_evaluation leaves a blank space for variables
joke_evaluation = "Isn't that joke so funny?! {}"

# Apply a format to an already created string
# So applying the hilarious format to the joke_evaluation string.
# This string had a space for a format in the empty braces
print(joke_evaluation.format(hilarious))


w = "This is the left side of..."
e = "a string with a right side"

# Adding variables which are strings concatenates them.
print(w + e)
