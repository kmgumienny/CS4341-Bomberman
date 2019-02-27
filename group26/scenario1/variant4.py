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
                    [6.677040814273156, -2.8712762824080875, 0.0007472148776999527, -0.9223685778177153, 4.6431419153438666e-05, -0.05143683159538506]) # About 78-80%

# Approximately 64%:
#[35.8728849892065, -14.346449697338242, 0.001407066566348685, -2.0042848170312517, 3.458804337251596e-05, -0.10134020470912834])

# Approximately 62-64%:
#[35.8728849892065, -13.837356743173592, 0.0016751148444334532, -1.627936404499567, 3.766290174603711e-05, -0.0826268186315153])

#[8.467997328611984, -4.2234323520984125, -0.44748429577882354, -7.117769978109375, 7.499998201995708, -100])
#[0.048529037847486856, -0.062131540631778726, -0.04838883024711721, -7.47749227917601, 5.537531792830999])
# HC1: 65% (100) [3.4548531092794423, -3.4435123193923878, -0.46429283428596524, -7.47749227917601, 5.537531792830999])
# Trained: 64.4% (1000)  [3.8857210122489385, -3.8672653906612733, -0.46429283428596524, -7.47749227917601, 5.537531792830999])
wins = 0
for i in range(0, 1000):
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

    if g.world.scores["me"] > 0:
        wins += 1
    print("{}, {:.2f}%".format(g.world.scores["me"], wins/(i+1)*100))
