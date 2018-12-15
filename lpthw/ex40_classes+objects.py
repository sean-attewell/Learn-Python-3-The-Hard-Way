# Classes are like Modules

# You can think about a module as a specialized dictionary that can store 
# Python code so you can access it with the . operator

# Python also has another construct that serves a similar purpose called 
# a class. A class is a way to take a grouping of functions and data and
# place them inside a container so you can access them with the . (dot) 
# operator.

class MyStuff(object): # object is the base class it inherits from.
# "Make a class named MyStuff that is an object."

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


# Here’s why classes are used instead of modules: You can take this
# MyStuff class and use it to craft many of them, millions at a time
# if you want, and each one won’t interfere with each other. When 
# you import a module there is only one for the entire program unless
# you do some monster hacks.



### Objects Are Like Import ###

# If a class is like a mini-module, then there has to be a concept
# similar to import but for classes. That concept is called 'instantiate', 
# which is just a fancy, obnoxious way to say 'create'.

# When you instantiate a class what you get is called an object.

# You instantiate a class by calling the class like it’s a function:

thing = MyStuff()
thing.apple()
print(thing.tangerine)

# 1. Python looks for MyStuff() and sees that it is a class you’ve defined.

# 2. Python crafts an empty object with all the functions you’ve specified
# in the class using def.

# 3. Python then looks to see if you made a ”magic” __init__ function, and
# if you have it calls that function to initialize your newly created
# empty object.

# 4. In the MyStuff function __init__ I then get this extra variable self,
# which is that empty object Python made for me, and I can set variables 
# on it just like you would with a module, dictionary, or other object.

# 5. In this case, I set self.tangerine to a song lyric and then I’ve 
# initialized this object.

# 6. Now Python can take this newly minted object and assign it to the 
# thing variable for me to work with.


# this is not giving you the class but instead is using the class as a 
# blueprint for building a copy of that type of thing.

# The truth is, classes and objects suddenly diverge from modules at 
# this point. Here is the truth:

# • Classes are like blueprints or definitions for creating new 
# mini-modules.

# • Instantiation is how you make one of these mini-modules and import it
# at the same time. "Instantiate" just means to create an object from the
# class.

# • The resulting created mini-module is called an object, and you then
# assign it to a variable to work with it.

# At this point objects behave differently from modules, and this should
# only serve as a way for you to bridge over to understanding classes and
# objects.




# I now have three ways to get things from things:

# dict style
# mystuff['apples']

# module style
# mystuff.apples()
# print(mystuff.tangerine)

# class style
# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)


### A first class example ###

# Two underscores is a dunderscore

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics: # line is just like using 'i', cus list.
            print(line)

happy_birthday = Song(["Happy birthday to you",
                       "I don't want to get sued",
                       "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_birthday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print()
print(happy_birthday.lyrics)

# Why do I need self when I make __init__ or other functions for classes?
  
# If you don’t have self, then code like cheese = 'Frank' is ambiguous. 
# That code isn’t clear about whether you mean the instance’s cheese
# attribute or a local variable named cheese.
 
# With self.cheese = 'Frank' it’s very clear you mean the 
# instance attribute self.cheese.




################# From the Video #################

# Importing a module like ex25 and then using a function like
# ex25.sort_sentence('This is a sentence')

# is actually accesing a dictionary in ex25
# ex25.__dict__.keys() to look at all the keys
# ex25.__dict__['sort_sentence']('this is a sentence')

# Python also uses a dinctionary internally to track all variables
# that you've made. globals()

