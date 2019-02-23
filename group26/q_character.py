# This is necessary to find the main code
import sys
import heapq
from colorama import Fore, Back

sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity


class qCharacter(CharacterEntity):
    def __init__(self, name, avatar, x, y):
        CharacterEntity.__init__(self, name, avatar, x, y)
        self.exit = None
        self.bombed = None
        self.tiles = {}


    #Variables
    #   qLearner holds the weights
    #   isTraining is a boolean deciding if qLearner is updated
    #   interationNum keeps track of iteration # in learning.
    #   maxIterations holds the
    def do(self, world, qLearner, isTraining, iternationNum, maxIternations):

        if isTraining:
            randomChance = 1/(maxIternations-iternationNum)
