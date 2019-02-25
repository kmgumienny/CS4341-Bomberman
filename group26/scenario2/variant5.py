# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner

# Create the game

g = Game.fromfile('map.txt')
g.add_monster(StupidMonster("monster", # name
                            "S",       # avatar
                            3, 5,      # position
))
g.add_monster(SelfPreservingMonster("monster", # name
                                    "A",       # avatar
                                    3, 13,     # position
                                    2          # detection range
))

qLearner = QLearner([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
