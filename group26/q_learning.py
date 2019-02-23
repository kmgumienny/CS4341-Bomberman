import sys
from q_functions import *

sys.path.insert(0, "../")

from entity import *

NUM_WEIGHTS = 6

from sensed_world import SensedWorld

POSSIBLE_MOVES = [(1, 0, 0), (1, 1, 0), (1, -1, 0), (-1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, -1, 0), (0, 1, 0),
                  (1, 0, 1), (1, 1, 1), (1, -1, 1), (-1, 0, 1), (-1, 1, 1), (-1, -1, 1), (0, -1, 1), (0, 1, 1)]

GAMMA = .9
ALPHA = .2

class QLearner:
    def __init__(self, weights):
        self.weights = weights

    #returns (dx, dy, bomb?)
    def bestMove(self, world, character):
        max_q = -9999999999
        max_a = None
        for move in POSSIBLE_MOVES:
            new_world = SensedWorld.from_world(world)
            new_world.characters[character.name].move(move[0], move[1])
            if move[2] == 1:
                new_world.characters[character.name].place_bomb()

            q = self.Q(new_world, new_world.characters[character.name])
            if q > max_q:
                max_q = q
                max_a = move

        return (max_a, max_q)

    def updateWeights(self, prevWorld, newWorld, character, reward):
        delta = (reward + GAMMA*self.bestMove(newWorld, character)[1]) - self.Q(newWorld, character)

        self.weights[0] += ALPHA * delta * f_to_exit(prevWorld, character)
        self.weights[1] += ALPHA * delta * f_to_monster(prevWorld, character)
        self.weights[2] += ALPHA * delta * f_to_bomb(prevWorld, character)
        self.weights[3] += ALPHA * delta * f_to_wall(prevWorld, character)
        self.weights[4] += ALPHA * delta * f_time_to_explosion(prevWorld, character)
        self.weights[5] += ALPHA * delta * f_is_exploded(prevWorld, character)

    def Q(self, world, character):
        sum = 0
        sum += self.weights[0] * f_to_exit(world, character)
        sum += self.weights[1] * f_to_monster(world, character)
        sum += self.weights[2] * f_to_bomb(world, character)
        sum += self.weights[3] * f_to_wall(world, character)
        sum += self.weights[4] * f_time_to_explosion(world, character)
        sum += self.weights[5] * f_is_exploded(world, character)

        return sum