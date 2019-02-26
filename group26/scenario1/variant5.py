# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

# TODO This is your code!
sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner
from q_functions import *

qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists],
                    [4.461871799497596, -2.214658827136486, -0.5153270948384178, -8.324788954040265, 5.269938302682641])

# Create the game
for i in range(0, 100):
    g = Game.fromfile('map.txt', display=False)
    g.add_monster(StupidMonster("monster", # name
                                "S",       # avatar
                                3, 5,      # position
    ))
    g.add_monster(SelfPreservingMonster("monster", # name
                                        "A",       # avatar
                                        3, 13,     # position
                                        2          # detection range
    ))



    g.add_character(qCharacter("me", # name
                                  "C",  # avatar
                                  0, 0,  # position
                                   qLearner,
                                   False,1,1))

    # Run!
    g.go()
    print(g.world.scores["me"])
