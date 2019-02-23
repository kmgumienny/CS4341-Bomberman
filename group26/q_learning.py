import sys
import q_functions

sys.path.insert(0, "../")

from entity import *

NUM_WEIGHTS = 6

class QLearner:
    def __init__(self, weights):
        self.weights = weights

    #returns (dx, dy, bomb?)
    def bestMove(self, world, character):

        pass

    def updateWeights(self, prevWorld, newWorld, character):
        pass

    def q(self, world, character):
        sum = 0;
        sum += weights[0] / q_functions.f_to_exit(world, character) ** 2
        sum += weights[1] / q_functions.f_to_monster(world, character) ** 2
        sum += weights[2] / q_functions.f_to_bomb(world, character) ** 2
        sum += weights[3] / q_functions.f_to_wall(world, character) ** 2
        sum += weights[4] / q_functions.f_time_to_explosion(world, character) ** 2
        sum += weights[5] * q_functions.f_is_exploded(world, character)