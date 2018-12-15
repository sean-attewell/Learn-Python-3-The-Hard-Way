# Python has many built-in exceptions which forces your program to output
# an error when something in it goes wrong.

# When these exceptions occur, it causes the current process to stop and
# passes it to the calling process until it is handled. If not handled, 
# our program will crash.

# For example, if function A calls function B which in turn calls function 
# C and an exception occurs in function C. If it is not handled in C,
# the exception passes to B and then to A.

# If never handled, an error message is spit out and our program come
# to a sudden, unexpected halt.

# exceptions can be handled using a try statement.
# A critical operation which can raise exception is placed inside the
# try clause and the code that handles exception is written in except
# clause

# It is up to us, what operations we perform once we have caught the
# exception. Here is a simple example.


# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2, 4]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break

    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print() # I think blank print it just to get a newline space.
print("The reciprocal of",entry,"is",r)

# In this program, we loop until the user enters an integer that has a 
# valid reciprocal. The portion that can cause exception is placed inside
# try block.

# If no exception occurs, except block is skipped and normal flow 
# continues. But if any exception occurs, it is caught by the except block.

# Here, we print the name of the exception using exc_info() function inside
# sys module and ask the user to try again. We can see that the value 'a'
# causes ValueError and '0' causes ZeroDivisionError.


# In the above example, we did not mention any exception in the 
# except clause

# This is not a good programming practice as it will catch all exceptions
# and handle every case in the same way. We can specify which exceptions
# an except clause will catch.

# A try clause can have any number of except clause to handle them 
# differently but only one will be executed in case an exception occurs.

# We can use a tuple of values to specify multiple exceptions in an
# except clause. Here is an example pseudo code.

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass



############ Raising Exceptions ################

# In Python programming, exceptions are raised when corresponding errors 
# occur at run time, but we can forcefully raise it using the keyword
# raise.

# We can also optionally pass in value to the exception to clarify why
# that exception was raised.

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)



############## finally ##############

# The try statement in Python can have an optional finally clause. This
# clause is executed no matter what, and is generally used to release
# external resources.

# For example, we may be connected to a remote data center through the
# network or working with a file or working with a Graphical User
# Interface (GUI).

# In all these circumstances, we must clean up the resource once used,
# whether it was successful or not. These actions (closing a file, GUI
# or disconnecting from network) are performed in the finally clause to 
# guarantee execution.

# Here is an example of file operations to illustrate this.

try:
   f = open("new.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()


# This type of construct makes sure the file is closed even if an 
# exception occurs.