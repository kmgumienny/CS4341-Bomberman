import sys
from q_functions import *

sys.path.insert(0, "../")

from entity import *
from events import Event

NUM_WEIGHTS = 6

from sensed_world import SensedWorld

POSSIBLE_MOVES = [(1, 0, 0), (1, 1, 0), (1, -1, 0), (-1, 0, 0), (-1, 1, 0), (-1, -1, 0), (0, -1, 0), (0, 1, 0)]
                  #(1, 0, 1), (1, 1, 1), (1, -1, 1), (-1, 0, 1), (-1, 1, 1), (-1, -1, 1), (0, -1, 1), (0, 1, 1)]

GAMMA = .9
ALPHA = .2

class QLearner:
    def __init__(self, weights):
        self.weights = weights

    #returns (dx, dy, bomb?)
    def bestMove(self, world, character):
        max_q = -9999
        max_a = None
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
                        q = -999
                    if event.tpe == Event.CHARACTER_FOUND_EXIT:
                        q = 999
            else:
                q = self.Q(new_world, new_world.me(character))

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

    def f_values(self, world, character):
        f = [0,0,0,0,0,0]

        f[0] = f_to_exit(world, character)
        f[1] = f_to_monster(world, character)
        f[2] = f_to_bomb(world, character)
        f[3] = f_to_wall(world, character)
        f[4] = f_time_to_explosion(world, character)
        f[5] = f_is_exploded(world, character)

        return f