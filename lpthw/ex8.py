# setting a variable as 4 braces. 
# Interestingly not an 'f' string... not does it have .format immediately
# Solves the problem of having a string for a template that you want
# to apply variables to randomly or at a later date.
formatter = "{} {} {} {}"

# Interestingly printing with only three variables filled doesn't work
# 'tuple index out of range'
# But printing with only three brace holes but 4 variables to input
# Just ignores the last one

# Filling the braces in the string assigned to formatter
# Calling .format on the string formatter
# Telling this string to do a format
# The dot tells it to format
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# This prints the braces - but why wouldn't it?
# The f string usually is what stops braces being shown literally
print(formatter.format(formatter, formatter, formatter, formatter))


# This works too! .format in a .format.
# You've still got 4x the formatter variable, but each brace is filled. 
print(formatter.format(formatter.format(1, 2, 3, 4), 
formatter.format(1, 2, 3, 4), 
formatter.format(1, 2, 3, 4), 
formatter.format(1, 2, 3, 4)))


# Again just filling the braces with .format
# I suppose the thing here is that .format is read as if it
# is on one line, commas working as normal.

print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# Only triple quotes would achieve new lines without any \n

# If you miss the first comma it thinks "Try your own text here" is
# all one string. Therefore only three arguments being passed in and tuple
# error.

#Let's debug it

lines = ("Try your"
    "Own text here",
    "Maybe a poem",
    "Or a song about fear")


# repr is the representation that python has (raw)
# Strange that both print out the brackets which aren't within the quotes
print(">>>>lines", lines)
print(">>>>lines", repr(lines))

# You could just print the strings being passed to formatter and see
# that the first two are smushed together.

print(">>>>", "Try your"
    "Own text here",
    "Maybe a poem",
    "Or a song about fear")

    # This one doesn't print the brackets
    # it's no longer calling the lines variable which has brackets
    
# Added >>>> to direct eyes to debugging bit
