# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner, NUM_WEIGHTS
#from q_learning import *

#below is a fun one
#qLearner = QLearner([f_to_exit, f_to_monster, f_is_exploded_now, f_time_to_explosion, f_bomb_to_wall, between_monster_bomb, is_in_corner, f_to_bomb_explosion, race_to_exit, bomb_to_wall], [150.44431831927005, -150.61243510629386, -74.06910280278274, 5.06822743380701, 61.62139531929878, -8.956675428553227, -5.443310138992995, 2.888611051263018, 300, 0])
qLearner = QLearner([0]*NUM_WEIGHTS)


for i in range(0, 100):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt', display=False)

    g.add_monster(SelfPreservingMonster("monster",  # name
                                        "M",  # avatar
                                        3, 13,  # position
                                        2  # detection range
                                        ))

    g.add_character(qCharacter("me", # name
                                  "C",  # avatar
                                  0, 0,  # position
                               qLearner,
                               True,
                               i,
                               1000))
    # Run!
    g.go()
    print(qLearner.weights)
    print(g.world.scores["me"])