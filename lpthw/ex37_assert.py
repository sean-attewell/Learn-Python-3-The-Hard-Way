
# Python has built-in assert statement to use assertion condition in the 
# program. assert statement has a condition or expression which is 
# supposed to be always true. If the condition is false assert halts
# the program and gives an AssertionError.

# Assert (ensure) that something is true.


def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

# Note that you didn't assign the function to a variable to store what
# was returned, you just straight printed the function and it printed
# what was returned.

mark1 = []
print("Average of mark1:",avg(mark1))

# Average of mark2: 78.0
# AssertionError: List is empty.

# Purple are Keywords