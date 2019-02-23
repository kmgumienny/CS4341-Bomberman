# This is necessary to find the main code
import sys
import heapq
from colorama import Fore, Back
from world_utilities import *

sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity

NUM_FEATURES = 11

ACTIONS = [(1, 0, 0), (1, 1, 0), (1, -1, 0), (-1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, -1, 0), (0, 1, 0),
           (1, 0, 1), (1, 1, 1), (1, -1, 1), (-1, 0, 1), (-1, 1, 1), (-1, -1, 1), (0, -1, 1), (0, 1, 1)]

ALPHA = .1
GAMMA = .8

class QCharacter(CharacterEntity):
    def __init__(self, name, avatar, x, y, weights=None):
        CharacterEntity.__init__(self, name, avatar, x, y)

        if weights is not None:
            self.weights = weights
        else:
            self.weights = []
            for i in range(NUM_FEATURES):
                self.weights.append(1.0)

        self.last_action = (0, 0, 0)

    def do(self, world):
        pass

    def Q(self, world, a):
        world.characters[self.name] = self

        self.move(a[0], a[1])
        if a[2] == 1:
            self.place_bomb()

        new_world = world.next()

        return self.weights[0] * x_distance_to_exit(new_world, self) + \
        self.weights[1] * y_distance_to_exit(new_world, self) + \
        self.weights[2] * x_distance_to_monster(new_world, self) + \
        self.weights[3] * y_distance_to_monster(new_world, self) + \
        self.weights[4] * x_distance_to_bomb(new_world, self) + \
        self.weights[5] * y_distance_to_bomb(new_world, self) + \
        self.weights[6] * x_distance_to_wall(new_world, self) + \
        self.weights[7] * y_distance_to_wall(new_world, self) + \
        self.weights[8] * num_walls(new_world) + \
        self.weights[9] * a_star_next_x(new_world, self) + \
        self.weights[10] * a_star_next_y(new_world, self)
