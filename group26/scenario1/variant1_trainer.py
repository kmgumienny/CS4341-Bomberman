# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner
from q_functions import *
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

#qLearner = QLearner([138.94790400859497, 0.0, -6.058183653409202, -41.180237244748874, 6.751411859902882, -0.2741834327385298])
qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_time_to_explosion, f_bomb_to_wall], [100.9243050471354044, 0.0, 2.0589987424427694, -80.13135317752685, 18.42263380373319, 0.4662978781043048])

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