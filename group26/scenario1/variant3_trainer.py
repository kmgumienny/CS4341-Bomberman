# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner
from q_functions import *

#Current status: 80% win rate, totally trained
qLearner = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [169.12117250971846, -77.31912800315031, -10.034113316375368, 8.897468734450623, 101.24816974980446, 72.63951738531733, 3.167600184843277])

count = 0
wins = 0

for i in range(0, 100):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt', display=False)

    g.add_monster(SelfPreservingMonster("monster",  # name
                                "M",  # avatar
                                3, 9,  # position
                                1))

    g.add_character(qCharacter("me", # name
                                  "C",  # avatar
                                  0, 0,  # position
                               qLearner,
                               False,
                               i,
                               1000))
    # Run!
    g.go()
    print(qLearner.weights)
    print(g.world.scores["me"])
    count += 1
    if g.world.scores["me"] > 0:
       wins += 1

print("Won " + str(wins/count) + " percent of the time")