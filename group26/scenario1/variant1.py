# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

# TODO This is your code!
sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner
from q_functions import *


# Create the game
g = Game.fromfile('map.txt')

# Current status: 100% success, untrained values
qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_time_to_explosion, f_bomb_to_wall], [114.54112122711332, 0.0, 4.114992302174889, -91.48558332791764, 6.079886312409335, 0.835050529831396])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
print(g.world.scores)
