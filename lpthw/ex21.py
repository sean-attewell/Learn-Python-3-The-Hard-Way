def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# When the function ends, any line that runs it will be able to
# assign this a + b result to a variable

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some maths with just functions!")

# Assigning what the function returns to the variable
# Note that it still prints the statements in the functions.
# But does not print what is returned. Not til you print the variable it
# was assigned to

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Got this right - start with most inner brackets.
# You can tell python works it out from the inner brackets first because
# the divide function prints first, then the multiply etc.
# Printing the steps is cool.

# I’m taking the return value of one function and using it as the
# argument of another function

print("That becomes: ", what, "Can you do it by hand?")



# Remember int(input())? The problem with that is then you can’t enter 
# floating point, so also try using float(input()) instead.

extra = subtract(add(24, divide(34, 100)), 1023)

print(f"Extra puzzle returns {extra}")
