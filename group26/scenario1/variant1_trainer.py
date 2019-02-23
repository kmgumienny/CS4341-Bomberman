# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner




#qLearner = QLearner([1000, 1, 1, -7, 1, 1])
#qLearner = QLearner([988799.7073695898, -31368.22053567095, -22769.275594463747, 32488.45804630133, 48718.55666450353, 117976.40578311047])
qLearner = QLearner([1191500.9765959792, 0.0, -16790.98185023866, 96725.92374673924, 32921.7416130828, -1118.9297071856752])

for i in range(0, 0):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt', display=False)

    g.add_character(qCharacter("me", # name
                                  "C",  # avatar
                                  0, 0,  # position
                               qLearner,
                               True,
                               i,
                               1000))
    # Run!
    g.go()
    print(g.world.scores["me"])
    print(qLearner.weights)

# Create the game
g = Game.fromfile('map.txt', display=True)

g.add_character(qCharacter("me",  # name
                           "C",  # avatar
                           0, 0,  # position
                           qLearner,
                           False,
                           0,
                           1000))

# Run!
g.go()

print(qLearner.weights)