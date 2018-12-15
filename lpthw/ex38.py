mystuff = ["one", "two"]

mystuff.append('Broother')

# What happens, at the end of all this, is a function call that looks 
# like: append(mystuff, 'hello') instead of what you read, 
# which is mystuff.append('hello').

# If you try and do the append with both arguments, it will say append
# is not defined. I guess it's not a global function, but an attribute
# of the list which is why it comes after a period.

print(mystuff)
print('\n')
# you see how Python said test() takes exactly 1 argument (2 given). If
# you see this, it means that Python changed a.test("hello") to
# test(a, "hello") and that somewhere someone messed up and didn’t add
# the argument for a.


# Whenever you're using a . you're dealing with an object.
# You're using the dot to send the object a message.
#########################################################


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that last list. Let's fix that.")

stuff = ten_things.split(' ')

print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee",
                 "Corn", "banana", "Girl", "Boy"]

print(more_stuff)
print('\n')

# Some functions are called like len instead of with a .
while len(stuff) != 10:  
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are now {len(stuff)} items now")

print("There we go: ", stuff)
print("leaves more_stuff looking like", more_stuff)

print('\n')

print(stuff[1]) 
print(stuff[-1]) 
print(stuff.pop()) # prints the same as above, but now stuff has lost that
print(' '.join(stuff))
print('#'.join(stuff[3:5])) # so it uses the string to join the elements
# of a list
# Join is a function that works on strings (an attribute)


