people = 30
cars = 29
trucks = 30


if cars > people: # If this is true, do this branch and run the block
    print("We should take the cars")
elif cars < people: # Else if another thing is true, then go down this branch
    print("We should not take the cars")
else: # If nothing was true, then do this branch
    print("We can't decide.")
# Three potential branches. Like going left right or middle.

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
    



# An if-statement creates what is called a ”branch” in the code.

# "If this Boolean expression is True, then run the code under it, 
# otherwise skip it."

# A colon at the end of a line is how you tell Python you are going to 
# create a new ”block” of code, and then indenting four spaces tells 
# Python what lines of code are in that block

# What happens if multiple elif blocks are True? 
# Python starts at the top and runs the first block that is True, 
# so it will run only the first one.