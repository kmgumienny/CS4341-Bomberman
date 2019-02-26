import sys
from q_functions import *

sys.path.insert(0, "../")

from entity import *
from events import Event

from sensed_world import SensedWorld

POSSIBLE_MOVES = [(1, 0, 0), (1, 1, 0), (1, -1, 0), (-1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, -1, 0), (0, 1, 0), (0, 0, 0),
                  (1, 0, 1), (1, 1, 1), (1, -1, 1), (-1, 0, 1), (-1, 1, 1), (-1, -1, 1), (0, -1, 1), (0, 1, 1), (0, 0, 1)]

GAMMA = .9
ALPHA = .2

class QLearner:
    def __init__(self, functions, weights=[]):
        self.functions = functions
        if weights == []:
            self.weights = [0]*len(self.functions)
        else:
            self.weights = weights

    #returns (dx, dy, bomb?)
    def bestMove(self, world, character):
        max_q = -9999
        max_a = (0,0,0)
        for move in POSSIBLE_MOVES:
            new_world = SensedWorld.from_world(world)

            if new_world.me(character) is None:
                continue

            new_world.me(character).move(move[0], move[1])
            if move[2] == 1:
                new_world.me(character).place_bomb()

            new_world, events = new_world.next()

            if new_world.me(character) is None:
                for event in events:
                    if event.tpe == Event.BOMB_HIT_CHARACTER or event.tpe == Event.CHARACTER_KILLED_BY_MONSTER:
                        q = -9999
                    if event.tpe == Event.CHARACTER_FOUND_EXIT:
                        q = 9999
            else:
                q = self.Q(new_world, new_world.me(character))

            if q > max_q:
                max_q = q
                max_a = move

        return (max_a, max_q)

    def updateWeights(self, prevWorld, newWorld, character, reward):
        delta = (reward) - self.Q(newWorld, character)

        for i in range(len(self.functions)):
            self.weights[i] += ALPHA * delta * self.functions[i](newWorld, character)

    def Q(self, world, character):
        sum = 0

        for i in range(len(self.functions)):
            sum += self.weights[i] * self.functions[i](world, character)

        return sum
