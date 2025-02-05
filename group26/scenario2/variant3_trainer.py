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

qLearner = QLearner([f_to_exit, f_is_exploded_now, f_to_monster, f_monster_to_bomb, f_bomb_to_wall, f_to_wall, f_time_to_explosion], [169.5792884684401, -89.43359914000227, -9.055797124970724, 5.3165976373538, 100.30312257082886, 71.41381770528874, 4.911815807943525])

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
                               True,
                               i,
                               1000))
    # Run!
    g.go()
    print(qLearner.weights)
    print(g.world.scores["me"])