print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "cheat_code":
        print("You win! Happy cheater?")
        print("GAME OVER")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("As your vision begins to clear, you see a golden chalice before you")
        print("""Drink from the chalice?
        1. Yes
        2. No""") # Funny that this text appears majorly indented.

        drink = input("> ")

        if drink == "1":
            print("Didn't you watch the film??")
            print("You experience a spooky death. GAME OVER.")
        elif drink == "2":
            print("Good self restraint!")
            print("Chicken dinner for you, thank you for playing.")
        else:
            print("I don't understand this action")
            print("Neither did Cthulu and he ends you.")
            print("GAME OVER.")

    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")


# Can you replace elif with a sequence of if-else combinations? You can 
# in some situations, but it depends on how each if/else is written. 
# It also means that Python will check every if-else combination, 
# rather than just the first false ones like it would with if-elif-else

# How do I tell whether a number is between a range of numbers? You have 
# two options: Use 0 < x < 10 or 1 <= x < 10, which is classic notation,
# or use x in range(1, 10).

# Goto makes spaghetti code. If elif else is structured clearly by indent.

# If I can't call if in if or elif, or call a function in if, then most
# programmers consider that broken.

# This concept of working things with other things is called 'orthogonal'.
# 2 things can do their own thing and be combined.
#
# I can do self similar things inside themselves.
# 
# Self similarity - the idea that i can make recursive structures, with
# ifs inside ifs inside ifs 

# Nice connection between a text based game and its code, because theyre
# both written in text. Rather than graphical.