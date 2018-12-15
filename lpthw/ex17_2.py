from sys import argv; s, ff, tf = argv; open(tf, 'w').write(open(ff).read())




# Notice how there is no close() in this shorter script? That's because
# when opening and immediately reading/writing to the File Object
# (without storing a reference to that open File Object (as a variable
# or something)) then with some interpreters the files are closed for you.


# https://stackoverflow.com/questions/36046167/is-there-a-need-to-close-files-that-have-no-reference-to-them/36063184#36063184

# essentially it's because when opening a file, that file won't simly be closed,
# it'll continue to take up a system resource until the script ends or some
# garbage collection happens at some future unknown time.

# So, closing files is highly recommended to retain manual control of your
# script/files behaviour, prevent unexpected behaviour caused by
# unpredictable output buffer flushing and not relying on the script ending
# (imagine if it doesn't actually end) to do your dirty work for you.



# Using with close is more scalable, portable, and predictable, so always 
# use it, even if it seems like it works fine without it
#
# The pythonic way to deal with this is to use the with context manager:

# with open(from_file) as in_file, open(to_file, 'w') as out_file:
#    indata = in_file.read()
#    out_file.write(indata)


# Python uses the ; as a separator, not a terminator.
# You can also use them at the end of a line, which makes them look
# like a statement terminator, but this is legal only because blank
# statements are legal in Python -- a line that contains a semicolon
# at the end is two statements, the second one blank.
#
