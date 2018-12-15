# We still use the older idea of a linear tape with a read/write head
# that must be moved

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Input not assigned to a variable, purely used to pause program
input("?")

print("Opening the file...")
# open tries to be safe by making you explicitly say you want to
# write a file. Like old tape systems.
target = open(filename, 'w')
# interesting that w for write has to be in quotes.

# With truncate(), you can declare how much of the file you want to remove,
# based on where you're currently at in the file. Without parameters,
# truncate() acts like w, whereas w always just wipes the
# whole file clean. So, these two methods can act identically,
# but they don't necessarily.

# What write does, is it creates the file... So if you open a file
# that doesn't exist in write mode, it makes it.

print("truncating the file. Goodbye!")
# Imagine truncate as moving the read head to the beginning and erasing
# all the data.
target.truncate()

# Interestingly the file needs to be open in write mode to be able
# to use truncate. It's a write option.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

# Target is the open file - not a .read() file.
target.write(f"{line1}\n{line2}\n{line3}\n")


print("And finally, we close it.")
target.close()

# You should close all your files at the end. This is because, if you
# forget to close them, you'll leak files and your computer will
# eventually crash.

# For now your program is so simple that when your program exits, it will
# save the data... but further down the line you'll have to tell it to
# save. I think the close operation saves it before closing.

# What modifiers to the file modes can I use? The most important one to
# know for now is the + modifier, so you can do 'w+', 'r+', and 'a+'.
# This will open the file in both read and write mode and,
# depending on the character use, position the file in different ways.
