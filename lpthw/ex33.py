# while-loops. What they do is simply do a test like an if-statement,
# but instead of running the code block once, they jump back to the "top"
# where the while is, and repeat. A while-loop runs until the expression
# is False. 
# This is unbounded looping. A for loop is bounded.
# when you sit down to write a while loop, the first question is if you
# should ask is if you can be writing a for loop.
# Then write the incrementer/test to make sure it does end.


def while_function(less_than_this, increment):
    
    i = 0
    numbers = []
    
    while i < less_than_this:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")
    return i * 2 

new_i = while_function(10, 2)

print("This is new_i: ", new_i) # this works, it's printed in the middle

# print(while_function(10, 2))
# Commenting out the above line, the while_function stil prints
# So it must run in assigning it to the new_i variable.
# This is exactly how we run in in ex 21 - just run by 
# assigning to variables
# If you then use the new variable (new_i), that doesn't need to run
# the function again, beacuse it already has it returned to it.

# not sure why this prints out 'none' at the end when done in a function.

# print(f"Does i survive outside function & while loops? {i}", i)
# Seems to survive outside while loops, but not functions
# but clearly you can return it from the function and assign to a variable
# as we have done.

# print("The numbers: ")

# for num in numbers:
    # print(num)

# This last bit doesn't work because the list numbers doesn't exist outside
# the function. I guess you'd need to return it!

numbers2 = []

for i in range(0, 10, 2):
    print(f"At the top i is {i}")
    numbers2.append(i)
    print("numbers2 now: ", numbers2)
    print(f"At the bottom i is {i}")

# Don't need to incrementer in the middle anymore
# The difference with using range is that i doesn't go up at the end
# but only on the next iteration of range.


# While True when you want to make something run forever like a videogame.
# While True:
#     print("OOO", end="")
 
       