from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()


print(f"The input file is {len(indata)} bytes long")

# This returns True if a file exists, based on its name in a string as an
# argument. It returns False if not.
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Opening to_file in write mode creates it
out_file = open(to_file, 'w')

# print(">>>> out_file:", repr(out_file))

# You then write to your new (and open) file the data from the
# .read() original file.
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()



# In powershell you can make a new text file with:
# echo "Test made with echo" > echo.txt


# Programming may not ”click” for you until maybe even Exercise 36,
# or it might not until you finish the book and then
# make something with Python.

# The import statement combines two operations; it searches for the named
# module, then it binds the results of that search to a name in the local 
# scope

# printing repr(out_file) will tell you info about that file.
# print(">>>> out_file:", repr(out_file))
# >>>> out_file: <_io.TextIOWrapper name='anova.txt' mode='w' encoding='cp1252'>
