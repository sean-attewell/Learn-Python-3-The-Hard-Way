from sys import argv

script, filename = argv

# Language comes from tape drives, combined with printers!
# Have to wind the spool to 'seek' what you need for the read head.
# Have to rewind to get back to the beginning.

# You'd print to the printer before there were screens!!

# Using a new command 'open'
# Like other commands, open takes a parameter and returns a value you can
# set to your own variable

#function
txt = open(filename)

# Does txt = open(filename) return the contents of the file? No, it doesn’t.
# It actually makes something called a "file object."
# The DVD player is not the DVD the same way the file object is
# not the file’s contents

# I like to think of open as loading up the rollers with a tape file
# and read as the reading head actually looking at a part of it.


print(f"Here's your file {filename}:")

# We call a function on txt named read.
# What you get back from open is a file, and it also has commands
# you can give it
# You give a file a command by using the . (dot or period), the
# name of the command, and parameters, just like with open and input.
# "Hey txt! Do your read command with no parameters!"
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# "commands" here, but commands are also called "functions" and "methods."

# Can go into python from the command line and do the same thing
# Don't forget to make the filename a string by putting it in quotes

# You can open and read .py files this way - they're just text!
# printing ex15.py didn't work until you replaced double quotes with
# straight ones typed in rather than copied"
# They aren't standard UTF8 text

# txt.close() will close the file again, so if you try to 
# print(txt.read()) then it won't work
# ValueError: I/O operation on closed file
