from sys import exit

# On many operating systems a program can abort with exit(0), and the 
# number passed in will indicate an error or not. If you do exit(1) then
# it will be an error, but exit(0) will be a good exit. The reason it’s
# backward from normal Boolean logic (with 0==False) is that you can use
# different numbers to indicate different error results. You can do
# exit(100) for a different error result than exit(2) or exit(1).

def gold_room():
    print("This room is full of gold.  How much do you take?")

    try:
        how_much = int(input("> "))
    except:
        dead("Man, learn to type a number.")
    # allows you to catch errors. (get error if user enters string).
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
    # if the first if is true, goes to the second if on same level.

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
            # because it's while true, it just goes back to the top of
            # the function when you change bear_moved or type rubbish.


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice: # This is cool
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        print("Cthulhu make a gargling noise")
        cthulhu_room() # Alternative to while True for restarting funcion


def dead(why):
    print(why, "Good job!") # does leave a space between variable and string
    exit(0)
    # Only exits the game if you actually die (and therefore run dead)
    # Or if you win!


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
# leaving the else blank or writing pass both just cause the program to end


start()

# He sugguests starting with it copied as a skeleton.
# Break large programming problems into small problems.
# You could track bear_moved between 'while true:' loops
# by printing it out every loop.