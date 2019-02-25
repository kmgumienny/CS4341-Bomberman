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


# Create the game
g = Game.fromfile('map.txt')

# Current status: unknown success rate, trained
qLearner = QLearner([0.07329931827878756, 0.0, -4.739669890677579, 7.157095990679528, 1.99471800916108, 13.169526383255644, 19.303965838014854, 7.14972908887264, 0.0, 0.2859332501784823, 0.0])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
print(g.world.scores)
