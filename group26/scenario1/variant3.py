# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner
from q_functions import *

# Create the game

g = Game.fromfile('map.txt')
g.add_monster(SelfPreservingMonster("monster", # name
                                    "M",       # avatar
                                    3, 9,      # position
                                    1          # detection range
))

# Current status: 80% win rate, totally trained
qLearner = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [169.12117250971846, -77.31912800315031, -10.034113316375368, 8.897468734450623, 101.24816974980446, 72.63951738531733, 3.167600184843277])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
