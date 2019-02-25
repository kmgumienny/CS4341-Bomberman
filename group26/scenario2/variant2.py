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

# Current status: 93% success, partially trained (manually modified S2V1 weights)
qLearner = QLearner([0.9043513311209257, -0.1, -0.8860218004661995, 8.635303064871081, 2.182181865553322, 0.038618906534273134, 2.3215325131848874, 8.627992562604867, 0.0, 0.25230394177423937, 0.0])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
