from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

### Now using composition! - just referring to a different class rather than
### having it as parameter
class Engine(object):

    def __init__(self):
        self.scene_map = Map('central_corridor')
        # self.a_map = scene map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        # current_scene = self.a_map.opening_scene()
        # current scene is the instance of the scene class, so you can call
        # enter on it below
        
        last_scene = self.scene_map.next_scene('finished')
        # last_scene = self.a_map.next_scene('finished')
        # last_scene is the instance of the finished scene.
        # 
        # Both of the above return 'val' from the next scene function in map.
        # val being the class name of a scene.

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            # runs enter() function of current_scene, and which scene is returned
            # at the end of the current scene is assigned to next_scene

            current_scene = self.scene_map.next_scene(next_scene_name)
            # current_scene then becomes the next scene (found in dict)
            # and it repeats the while loop, running enter on the new current scene


        # When the while loops ends, you enter the 'finished' scene.
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your Mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this.",
         "You're worse than your Dad's jokes."

    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
             The Gothons of Planet Percal #25 have invaded your ship and
             destroyed your entire crew.  You are the last surviving
             member and your last mission is to get the neutron destruct
             bomb from the Weapons Armory, put it in the bridge, and
             blow the ship up after getting into an escape pod.

             You're running down the central corridor to the Weapons
             Armory when a Gothon jumps out, red scaly skin, dark grimy
             teeth, and evil clown costume flowing around his hate
             filled body.  He's blocking the door to the Armory and
             about to pull a weapon to blast you.
             """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon.  His clown costume is flowing and
                  moving around his body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This completely ruins his brand new costume his mother
                  bought him, which makes him fly into an insane rage
                  and blast you repeatedly in the face until you are
                  dead.  Then he eats you.
                  """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                  Like a world class boxer you dodge, weave, slip and
                  slide right as the Gothon's blaster cranks a laser
                  past your head.  In the middle of your artful dodge
                  your foot slips and you bang your head on the metal
                  wall and pass out.  You wake up shortly after only to
                  die as the Gothon stomps on your head and eats you.
                  """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                  Lucky for you they made you learn Gothon insults in
                  the academy.  You tell the one Gothon joke you know:
                  Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                  fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
                  not to laugh, then busts out laughing and can't move.
                  While he's laughing you run up and shoot him square in
                  the head putting him down, then jump through the
                  Weapon Armory door.
                  """))
            return 'laser_weapon_armory'

        elif action == "import":
            import ex43_imp # This is OK because saved in same directory
            ex43_imp.main()
            exit(1)
            
            # could have done from ex43_imp import main, and then just run main()
            # without specifying where it was locatd in the prefix


        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              You do a dive roll into the Weapon Armory, crouch and scan
              the room for more Gothons that might be hiding.  It's dead
              quiet, too quiet.  You stand up and run to the far side of
              the room and find the neutron bomb in its container.
              There's a keypad lock on the box and you need the code to
              get the bomb out.  If you get the code wrong 10 times then
              the lock closes forever and you can't get the bomb.  The
              code is 3 digits.
              """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                  The container clicks open and the seal breaks, letting
                  gas out.  You grab the neutron bomb and run as fast as
                  you can to the bridge where you must place it in the
                  right spot.
                  """))
            return 'the_bridge'
        else:
            print(dedent("""
                  The lock buzzes one last time and then you hear a
                  sickening melting sound as the mechanism is fused
                  together.  You decide to sit there, and finally the
                  Gothons blow up the ship from their ship and you die.
                  """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              You burst onto the Bridge with the netron destruct bomb
              under your arm and surprise 5 Gothons who are trying to
              take control of the ship.  Each of them has an even uglier
              clown costume than the last.  They haven't pulled their
              weapons out yet, as they see the active bomb under your
              arm and don't want to set it off.
              """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                  In a panic you throw the bomb at the group of Gothons
                  and make a leap for the door.  Right as you drop it a
                  Gothon shoots you right in the back killing you.  As
                  you die you see another Gothon frantically try to
                  disarm the bomb. You die knowing they will probably
                  blow up when it goes off.
                  """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                  You point your blaster at the bomb under your arm and
                  the Gothons put their hands up and start to sweat.
                  You inch backward to the door, open it, and then
                  carefully place the bomb on the floor, pointing your
                  blaster at it.  You then jump back through the door,
                  punch the close button and blast the lock so the
                  Gothons can't get out.  Now that the bomb is placed
                  you run to the escape pod to get off this tin can.
                  """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
              You rush through the ship desperately trying to make it to
              the escape pod before the whole ship explodes.  It seems
              like hardly any Gothons are on the ship, so your run is
              clear of interference.  You get to the chamber with the
              escape pods, and now need to pick one to take.  Some of
              them could be damaged but you don't have time to look.
              There's 5 pods, which one do you take?
              """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent("""
                  You jump into pod {guess} and hit the eject button.
                  The pod escapes out into the void of space, then
                  implodes as the hull ruptures, crushing your body into
                  jam jelly.
                  """))
            return 'death'
        else:
            print(dedent("""
                  You jump into pod {guess} and hit the eject button.
                  The pod easily slides out into space heading to the
                  planet below.  As it flies to the planet, you look
                  back and see your ship implode then explode like a
                  bright star, taking out the Gothon ship at the same
                  time.  You won!
                  """))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# After that I have my Map class, and you can see it is storing each
# scene by name in a dictionary, and then I refer to that dict with
# Map.scenes. This is also why the map comes after the scenes because the
# dictionary has to refer to the scenes, so they have to exist.


# This instance of map means you can run opening_scene and next_scene
# Next scene returns the actual specific scene class, which you can assign to 
# a variable to make an instance of.

a_game = Engine()
# You can run opening_scene/next_scene from a_map within the class
# that has the play function

a_game.play()
# Now you can assign the result of the next_scene function to an instance
# called 'current_scene', and another instance called 'last scene'.


# Finally I've got my code that runs the game by making a Map, then
# handing that map to an Engine before calling play to make the game work.

# Build code up slowly running code over and over again

# You can't figure out by looking, just print print print.

# "I can see you spend a week or two on this..."


# Remember that you need to make an instance of a class to run the function
# from that instance

# you just have to return the next scene, and map maps the scene to a class


# Lesson from this that it's hard to grok the big picture of code someone else has 
# written. You can figure out bits at a time, but without knowing their vision
# for how it all flows together, it's not too easy to figure out.
# Perhaps if you tried it yourself first you may have more of a clue.


# Map is a class with a function that returns scene classes from a dictionary.
# 
# The Engine class takes an instance of the map class as a parameter so that it can 
# run said functions from the instance of the map class.
# 
# Engine has a function that makes instances of the scene classes by running the
# function from the map class, and then runs the enter() function from the scene 
# classes it has instantiated.
# 
# It loops round, instantiating the scene returned at the end of the last one,
# and then running enter from the new scene, until you're at the last scene.



# A finite-state machine (FSM) is a mathematical model of computation. 
# It is an abstract machine that can be in exactly one of a finite number of states
# at any given time. The FSM can change from one state to another in response to
# some external inputs; the change from one state to another is called a transition.
# An FSM is defined by a list of its states, its initial state, and the conditions 
# for each transition

# The behavior of state machines can be observed in many devices in modern society 
# that perform a predetermined sequence of actions depending on a sequence of events
# with which they are presented. Simple examples are vending machines, which dispense
# products when the proper combination of coins is deposited, elevators, whose 
# sequence of stops is determined by the floors requested by riders, traffic lights,
# which change sequence when cars are waiting, and combination locks, which require
# the input of combination numbers in the proper order.

# The finite state machine has less computational power than some other models of 
# computation such as the Turing machine. The computational power distinction means 
# there are computational tasks that a Turing machine can do but a FSM cannot.
# This is because a FSM's memory is limited by the number of states it has


