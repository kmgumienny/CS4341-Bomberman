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

# Current status: 100% success, trained values
qLearner = QLearner([f_to_exit, f_to_monster, f_is_exploded_now, f_time_to_explosion, f_bomb_to_wall], [90.77976324371679, 0.0, 7.520238703388388, 4.913100904773046, 17.162358880575766])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
print(g.world.scores)
