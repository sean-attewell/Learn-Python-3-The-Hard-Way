from sys import argv

script, input_file = argv

# prints what's inside f
def print_all(f):
    #print(">>>print_all: f =", f)
    print(f.read())
    #print("<<<print_all: f = ", f)

# rewinds f to the beginning
# The code seek(0) moves the file to the 0 byte (first byte) in the file.
def rewind(f):
    #print(">>>rewind: f =", f)
    f.seek(0)
    #print("<<<rewind: f =", f)

# prints whatever number you give to line_count
# prints one line from f
# going back to the tape anaology, readline() reads until the end of the
# current line. When it is called a second time, it's already at the end
# of the first line (from the first time it was called), so it reads the
# second line and stops before the third.
def print_a_line(line_count, f):
    #print(">>>print_a_line: f =", f)
    print(line_count, f.readline(), end = "")
    #print("<<<print_a_line: f =", f)

# Inside readline() is code that scans each byte of the
# file until it finds a \n character, then stops reading the file to
# return what it found so far
# Note that without end = " " the \n will be printed

# The file f is responsible for maintaining the current position in the
# file after each readline() call, so that it will keep reading each line.

current_file = open(input_file)

# When you pass current_file into the functions (into argument
# f), changes you make in the function will impact the file. 
# You are not copying it, you are passing it by reference.

print("First let's print the whole file:\n")

print_all(current_file)

print("Now lets rewind, kind of like a tape.")

# You have to rewind after that print_all to get back to the start
# and start printing the lines one by one
rewind(current_file)

print("Let's print three lines:")
# The readline() function returns the \n that’s in the file at the
# end of that line.
# Add a end = "" at the end of your print function calls to avoid
# adding double \n to every line.

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


# Remember you figured this out by hovering over readline() to get docs.

# pydoc file has a section on seek
# pydoc file.seek just shows the relevant part

# += adds another value with the variable's value and assigns the new 
# value to the variable.
#>>> x = 3
#>>> x += 2
#>>> print(x)
#5

# this is kind of like a contraction for the
# two operations = and +. That means x = x + y is the same as x += y.

# -=, *=, /= does similar for subtraction, multiplication and division.