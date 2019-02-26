# This is necessary to find the main code
import sys
import random, math
import heapq
from q_functions import *
from colorama import Fore, Back

sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity
from sensed_world import SensedWorld


class qCharacter(CharacterEntity):
    def __init__(self, name, avatar, x, y, qLearner, isTraining, iterationNum, maxIterations):
        CharacterEntity.__init__(self, name, avatar, x, y)
        self.exit = None
        self.bombed = None
        self.tiles = {}

        self.qLearner = qLearner
        self.isTraining = isTraining
        self.iterationNum = iterationNum
        self.maxIterations = maxIterations

        self.randomChance = 1 / (self.iterationNum + 1) ** .25
        #print(self.randomChance)

        self.prevWorld = None

    def do(self, world):
        self.prevWorld = world
        self.tiles = {}

        if self.isTraining:
            if random.random() < self.randomChance:
                possibleStep = [-1, 0, 1]
                possibleBomb = [0, 1]

                if random.choice(possibleBomb) == 1:
                    self.place_bomb()

                dx = random.choice(possibleStep)
                dy = random.choice(possibleStep)

                self.move(dx, dy)
            else:
                move, _ = self.qLearner.bestMove(world, self)
                dx, dy, bomb = move

                self.move(dx, dy)

                if bomb == 1:
                    self.place_bomb()
        else:
            move, _ = self.qLearner.bestMove(world, self)
            dx, dy, bomb = move
            self.move(dx, dy)

            if bomb == 1:
                self.place_bomb()

    def updateWeights(self, world, won, lost):
        if self.isTraining:
            if won:
                reward = 10
            elif lost:
                reward = -5
            else:
                reward = (f_to_exit(world, self)**.1)*10

            self.qLearner.updateWeights(self.prevWorld, world, self, reward)
