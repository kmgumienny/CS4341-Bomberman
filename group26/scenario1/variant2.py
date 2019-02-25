# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster

# TODO This is your code!
sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner

# Create the game

g = Game.fromfile('map.txt')
g.add_monster(StupidMonster("monster", # name
                            "M",       # avatar
                            3, 9       # position
))

# Current status: 100% in 5 attempts, untrained values
qLearner = QLearner([100, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
