# When you create a list, you can read its items one by one. Reading its
# items one by one is called iteration.
# Your list is an iterable.

# Everything you can use "for... in..." on is an iterable; lists, strings,
# files...

mylist = [1, 2, 3]
for i in mylist:
    print(i)

print('\n\n')

# These iterables are handy because you can read them as much as you wish,
# but you store all the values in memory and this is not always what you
# want when you have a lot of values.

# Generators are iterators, a kind of iterable you can only iterate over 
# once. Generators do not store all the values in memory, they generate
# the values on the fly

mygenerator = (x*x for x in range(3)) 
# remember mygenerator is not a list but a generator.

for i in mygenerator:
    print(i)

for i in mygenerator:
    print(i+1)


print('\n')

# It is just the same except you used () instead of []. BUT, you cannot 
# perform for i in mygenerator a second time since generators can
# only be used once: they calculate 0, then forget about it and
# calculate 1, and end calculating 4, one by one.

# Hence why the second one does nothing.

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i in mygenerator:
    print(i)


# I's handy when you know your function will return a huge set of values 
# that you will only need to read once

# The first time the for calls the generator object created from your 
# function, it will run the code in your function from the beginning
# until it hits yield, then it'll return the first value of the loop.
# Then, each other call will run the loop you have written in the
# function one more time, and return the next value, until there is
# no value to return

# I guess it's not storing it in a list each time.