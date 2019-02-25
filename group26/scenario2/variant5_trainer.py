# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.stupid_monster import StupidMonster
from monsters.selfpreserving_monster import SelfPreservingMonster

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner, NUM_WEIGHTS

qLearner = QLearner([0]*NUM_WEIGHTS)


for i in range(0, 100):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt', display=False)

    g.add_monster(StupidMonster("monster",  # name
                                "S",  # avatar
                                3, 5,  # position
                                ))
    g.add_monster(SelfPreservingMonster("monster",  # name
                                        "A",  # avatar
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