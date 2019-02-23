import sys
import q_functions

sys.path.insert(0, "../")

from entity import *

class QLearner:
    def __init__(self, weights):
        self.weights = weights

    def bestMove(self, world, character):
        pass

    def updateWeights(self, prevWorld, newWorld, character):
        pass
