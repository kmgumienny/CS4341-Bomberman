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

# Current status: 100% success, untrained values
qLearner = QLearner([100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

g.add_character(qCharacter("me", # name
                              "C",  # avatar
                              0, 0,  # position
                               qLearner,
                               False,1,1))

# Run!
g.go()
print(g.world.scores)
