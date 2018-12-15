# In Python, anonymous function is a function that is defined without a
# name.

# While normal functions are defined using the def keyword, in Python 
# anonymous functions are defined using the lambda keyword.
# Hence, anonymous functions are also called lambda functions.

# lambda arguments: expression

# Lambda functions can have any number of arguments but only one 
# expression. The expression is evaluated and returned. Lambda functions
# can be used wherever function objects are required.


# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))

# In the above program, lambda x: x * 2 is the lambda function. Here x is
# the argument and x * 2 is the expression that gets evaluated and
# returned.

# This function has no name. It returns a function object which is
# assigned to the identifier double. We can now call it as a normal
# function. The statement

# double = lambda x: x * 2

# is nearly the same as

def double2(x):
    return x * 2

print(double(6))
print(double2(6))
seveee = double2(7)
print(seveee)
print('\n')

# We use lambda functions when we require a nameless function for a short
# period of time.

# In Python, we generally use it as an argument to a higher-order function
# (a function that takes in other functions as arguments). 
# 
# Lambda functions are used along with built-in functions like filter(),
# map() etc.

# The filter() function in Python takes in a function and a list as
# arguments:


# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)



# The function is called with all the items in the list and a new list is
# returned which contains items for which the function evaluates to True.

# The map() function in Python takes in a function and a list.

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)


