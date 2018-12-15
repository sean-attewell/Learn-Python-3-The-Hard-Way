# The variables in your function are not connected to the variables
# in your script.
# Cheese_count for example has its own context or stack or frame.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(">>> cheese_count = ", cheese_count, "boxes_of_crackers = ", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket. \n")
    print("<<< exit cheese_and_crackers")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# We can give it straight numbers. We can give it variables. 
# We can give it math
# if you can use = to name something, you can usually pass it to a function 
# as an argument

def s3an_function(no_eggs, no_leaves):
    print(f"Breaking the fast with {no_eggs} eggs and {no_leaves} leaves.\n")

eggies = 20

s3an_function(eggies, 20 * 3)


# Does making the variable amount_of_cheese change the variable 
# cheese_count in the function? No, those variables are separate and 
# live outside the function. They are then passed to the function, 
# and temporary versions are made just for the function’s run. 
# When the function exits these temporary variables go away and 
# everything keeps working

# Is it bad to have global variables (like amount_of_cheese) with the same 
# name as function variables?
# Yes, since then you’re not quite sure which one you’re talking about. 
# But sometimes necessity means you have to use the same name, or you 
# might do it on accident. Just avoid it whenever you can

# Can you call a function within a function? Yes

# Functions keep your bugs in one place! (in the function)
# compared to copying the code each time

# Can't stare at code to see what it's doing, need to print.