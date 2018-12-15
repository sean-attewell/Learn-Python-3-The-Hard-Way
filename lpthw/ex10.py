tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line"
# \\ just prints one backslash
backslash_cat = "I'm \\ a \\ cat."

# Interesting that within """ you can \n a new line,
# Even though you don't really need to.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# ASCII defines 128 characters, which map to the numbers 0–127.
# Unicode defines (less than) 221 characters, which, similarly, map to 
# numbers 0–221 (though not all numbers are currently assigned, and some 
# are reserved).

# Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning in ASCII as they have in Unicode. For example, the number 65 means "Latin capital 'A'".

# Because Unicode characters don't generally fit into one 8-bit byte, there are numerous ways of storing Unicode characters in byte sequences, such as UTF-32 and UTF-8.
# UTF stands for "Unicode Transformation Format


# Just makes a bell sound - for old printers
print("ASCII bell (BEL)\a") # \a

# Deletes the prior letter... For old printers
print("ASCII backspace\b(BS)")

# Form feed means advance downward to the next "page". It was 
# commonly used as page separators, but now is also used as 
# section separators. (It's uncommonly used in source code to
# divide logically independent functions or groups of functions.) 
# Text editors can use this character when you "insert a page 
# break". This is commonly escaped as "\f", abbreviated FF
# For old printers
print("ASCII formfeed\f(FF)")

# new line is called linefeed
print("ASCII \nlinefeed (LF)")

# don't get this one
# print("\N{name} this is the unicode char \'named name\'")

# move the position of the cursor to the first position on the same line
# so it overwrites the start portion
print("this is carriage \rreturn")

# easy one
print("here is \ta horizontal tab")

# So this 16-bit hex is an a with a thing over it
# Numeric code for unicode, think \u for unicode
print("16-bit hex \u0101")

# This doesn't seem to be displaying correctly
# Numeric code for unicode, think \u for unicode
print("32-bit hex \U00001011")

# Doesn't seem to like this one either
# Apparently the box on the output means it's so old that even powershell
# doesn't know what to do with it.
print("What's a\vvertical tab then?")

# I think this is an octal value? Makes an I
# Maybe 
print("What the heck is this \111?")

# Not a clue on this one, won't work.
# print("Character with hex value \xhh")

fat_cat_singles = '''
Is this
Realllly any different
to using double quotes?
Yeah you can do this """
'''
print(fat_cat_singles)

# Escape within var in fstring braces
print(f"Got an escape in the fstring braces {persian_cat}")

# Escape with using .format() to fill braces
formatter = "{} {}"
print(formatter.format("one \nfill", "two \tfill"))
