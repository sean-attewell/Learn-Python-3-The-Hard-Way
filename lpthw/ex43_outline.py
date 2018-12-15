class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# This is top down approach, starting with the concepts and refining into
# code.

# Bottom up - I find this process is better once you're more solid at
# programming and are naturally thinking in code about problems.

# Breaking it down in little pieces and exploring with code then helps
# you slowly grind away at the problem until you've solved it.
# However, remember that your solution will probably be meandering and 
# weird, so that's why my version of this process involves going back and
# finding research, then cleaning things up based on what you've learned.

