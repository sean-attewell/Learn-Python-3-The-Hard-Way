# An interpreter is a program that reads and executes code. This 
# includes source code, pre-compiled code, and scripts. Common 
# interpreters include Perl, Python

# With statement allows you to extract away dealing with system resources.
# e.g an open file is a system resource you need to aquire and release.
# (so it doesn't have to keep track of it)

# With an expression as a variable do:

with open('new.txt', 'r') as f:
    print(f.read())

# Can work with variable f in the with block, but as soon as python 
# leaves the block, it will close the file.
# Otherwise you'd have to use 'try' and 'finally' to write and close.




