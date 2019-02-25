# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner, NUM_WEIGHTS
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

#qLearner = QLearner([169.97432332086225, 0.0, -8.324417085654472, 0.3083237664564956, -0.14125928750336977, -2.2854681098275593, 2.8822516279032158, 0.3083237664564956, 0.0, -6.862096724380629, 0.0, -93.94080055651418])
qLearner = QLearner([0]*NUM_WEIGHTS)

for i in range(0, 100):
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