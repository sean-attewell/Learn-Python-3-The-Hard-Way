# Rules for If-Statements

# Every if-statement must have an else.
# Prove to yourself why you don't need it.
# Without one the program just ends.

# If this else should never run because it doesn’t make sense, then you 
# must use a die function in the else that prints out an error message
# and dies. This will find many errors.

# Never nest if-statements more than two deep and always try to do them 
# one deep.

# Treat if-statements like paragraphs, where each if-elif-else grouping is 
# like a set of sentences. Put blank lines before and after.

# Your Boolean tests should be simple. If they are complex, move their 
# calculations to variables earlier in your function and use a good name
# for the variable


# ------------------------------------------

# Rules for Loops

# Use a while-loop only to loop forever, and that means probably never. 
# This only applies to Python; other languages are different.

# Use a for-loop for all other kinds of looping, especially if there is a 
# fixed or limited number of things to loop over.

# ------------------------------------------

# Tips for Debugging

# Do not use a ”debugger.” A debugger is like doing a full-body scan on 
# a sick person. You do not get any specific useful information, and you
# find a whole lot of information that doesn’t help and is just confusing.

# The best way to debug a program is to use print to print out the values 
# of variables at points in the program to see where they go wrong.

# Make sure parts of your programs work as you work on them. Do not write 
# massive files of code before you try to run them. 
# Code a little, run a little, fix a little.

# ------------------------------------------

# The best way to work on a piece of software

# write a list of tasks you need to complete to finish the
# software. This is your to do list.

# Pick the easiest thing you can do from your list.

# Write out English comments in your source file as a guide.

# Write some of the code under the English comments.

# Quickly run your script so see if that code worked.

# Keep working in a cycle of writing some code, running it to test it,
# and fixing it until it works.

# Cross this task off your list, then pick your next
# easiest task and repeat.

# This process will help you work on software in a methodical and 
# consistent manner. As you work, update your list by removing tasks
# you don’t really need and adding ones you do.

# ------------------------------------------

# pass

# It is used when a statement is required syntactically but you do not 
# want any command or code to execute. The pass statement is a
# null operation; nothing happens when it executes.

# The pass is also useful in places where your code will eventually go, 
# but has not been written yet (e.g., in stubs for example).

# ------------------------------------------


# break

# The break statement is used for premature termination of the current 
# loop. After abandoning the loop, execution at the next statement is 
# resumed

# https://www.tutorialspoint.com/python3/python_break_statement.htm


for letter in 'Python':     # First Example
    if letter == 'h':
        break
    print ('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
    print ('Current variable value :', var)
    var = var -1
    if var == 5:
        break

print ("Good bye!")



print("\n\n")
####### Python continue statement #######

#

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

# If the string is "i", we don't execute the rest of the block.
# Instead we 'continue' back to the loop.
# Hence, we see in our output that all the letters except "i"
# get printed.

