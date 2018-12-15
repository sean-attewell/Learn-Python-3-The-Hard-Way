def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # calling pop on a list here not a string.
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# going into python mode on powershell and typing
# import ex25 (don't need .py)
# No different to import sys! Just importing a python script.

# Try doing this: help(ex25) and also help(ex25.break_words)

# Typing ex25.break_words() is annoying. You're saying, inside ex25 I
# want to get break_words(). 
# A shortcut is to do your import like this: from ex25 import * 
# which is like saying, ”Import everything from ex25.”
# Now you can just type functions without ex25. preceeding them. 

# The return from a function gives the line of code that called the
# function a result. You can think of a function as taking input through
# its arguments and returning output through return. The print is
# completely unrelated to this and only deals with printing output 
# to the terminal

# Can do debug printing in and exit from each function to do the audit 
# trail - so you'd see it go in one and call and leave another before
# leaving the original.

#sorted = sort_sentence('pear apple orange')
#print(sorted)
