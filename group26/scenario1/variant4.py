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
qLearner = QLearner([f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now, f_bomb_exists, f_within_two_of_monster],
[8.467997328611984, -4.2234323520984125, -0.44748429577882354, -7.117769978109375, 7.499998201995708, -100])
#[0.048529037847486856, -0.062131540631778726, -0.04838883024711721, -7.47749227917601, 5.537531792830999])
# HC1: 65% (100) [3.4548531092794423, -3.4435123193923878, -0.46429283428596524, -7.47749227917601, 5.537531792830999])
# Trained: 64.4% (1000)  [3.8857210122489385, -3.8672653906612733, -0.46429283428596524, -7.47749227917601, 5.537531792830999])


for i in range(0, 100):
    g = Game.fromfile('map.txt', display=False)
    g.add_monster(SelfPreservingMonster("monster", # name
                                        "M",       # avatar
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
