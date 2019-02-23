# This is necessary to find the main code
import sys
import random
import heapq
from q_functions import *
from colorama import Fore, Back

sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity


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

        self.prevWorld = None


    #Variables
    #   qLearner holds the weights
    #   isTraining is a boolean deciding if qLearner is updated
    #   interationNum keeps track of iteration # in learning.
    #   maxIterations holds the
    def do(self, world):
        self.prevWorld = world

        if self.isTraining:
            randomChance = 1/(self.maxIterations - self.iterationNum)
            if random.random < randomChance:
                possibleStep = [-1, 0, 1]
                possibleBomb = [0, 1]
                if random.choice(possibleBomb) == 1:
                  self.place_bomb()
                self.move(random.choice(possibleStep), random.choice(possibleStep))
            else:
                self.qLearner.bestMove(world, self)

    def updateWeights(self, world, won, lost):
        reward = 0
        if won:
            reward = 1000
        if lost:
            reward = -1000
        reward = -1 + f_to_exit(world, self)

        self.qLearner.updateWeights(self.prevWorld, world, self, reward)