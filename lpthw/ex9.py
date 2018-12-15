# Here's some strange stuff, remember to type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"

# So here \n makes the next bit start on a new line
months = "Jan\nFeb\nMar\nApr\nMay\nJune\nJul\nAug"

# It's an escape sequence. It's a way to add formatting in a way that
# doesn't break python's processing of the string.
# Special characters, tab, vertical space etc
# After a backslash things are processed as either a special character 
# (like \n), or if it's not a special character, just the character like \"


print("Here are the days:", days)
print("Here are the months:", months)


# using """ seems to put things on different lines automatically
# If you code them that way. Also indents, all without escape sequences."
print("""
There's something going on here.
With the three double-quotes.
        We'll be able to type as much as we like.
Even 4 lines if we want to, or 5, or 6.
""")

# You can put double and single quotes inside tripple quotes!
# It will also take on any tabbed space automatically
# (no need for \t)

# If you open with two quotes, it just thinks an empty string has closed
# And then goes into python mode, trying to interperet your string as 
# python

